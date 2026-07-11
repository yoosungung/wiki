---
title: "AgentFS: SQLite 기반 에이전트 가상 파일 시스템 및 격리 샌드박스"
tags: ["Agents", "Implementation", "Memory", "AgentFS", "FUSE", "SQLite", "Sandbox"]
type: "wiki"
status: "published"
last_updated: "2026-06-28"
updated: "2026-06-28"
related_raw: ["[[2026-06-19-agentfs_sqlite_virtual_filesystem.md]]", "[[2026-06-21-agentfs-sqlite-isolated-sandbox-filesystem.md]]", "[[2026-06-26-agentfs_sqlite_virtual_filesystem.md]]", "[[2026-06-28-agentfs_sqlite_virtual_filesystem_sandbox.md]]"]
---

# 📁 AgentFS: SQLite 기반 에이전트 가상 파일 시스템

**AgentFS (Agent File System)**는 AI 에이전트의 안전한 파일 조작, 상태 지속성(Persistence), 그리고 작업 이력의 완벽한 감사(Auditability)를 제공하기 위해 Turso 팀에서 개발한 에이전트 네이티브 가상 파일 시스템 레이어입니다.

---

## 0. 개발 동기 (Motivation)

기존 에이전트 개발 방식에서는 메모리 데이터(벡터/관계형 DB), 파일 저장소(S3 등), 실행 로그(오딧 트레일)가 각각 별개의 파편화된 시스템으로 관리되어 에이전트 상태 관리가 매우 복잡했습니다. AgentFS는 이 문제를 해결하기 위해 **"유닉스 파일시스템"이라는 단일화된 추상화 레이어**를 제공합니다. 

*   **RAG의 한계 극복 (Navigation over Retrieval)**: 기존 RAG(Retrieval-Augmented Generation) 파이프라인의 단순 조각 정보 검색 방식은 복잡한 에이전트 행동을 제어하는 데 한계를 보입니다. 에이전트는 단순 질문-답변자가 아닌 주체적인 탐색자(Explorer)이므로, 파일시스템 내에서 `ls`, `cat`, `grep` 등 친숙한 POSIX 명령어를 사용해 데이터와 코드를 직접 탐색(Navigation)하고 상호작용하는 것이 논리적 직관성을 향상시킵니다.
*   **LLM 친화적 인터페이스**: 유닉스 셸 스크립트와 파일 조작 방식에 이미 풍부하게 사전 학습된 대규모 언어 모델(LLM)에게 가장 친화적이고 익숙한 형태의 추상화를 구축하여 에이전트 개발 효율을 획기적으로 향상합니다.

---

## 1. 아키텍처 및 동작 메커니즘

AgentFS는 에이전트가 작업하는 파일 디렉토리 전체를 하나의 **단일 SQLite 데이터베이스 파일**로 추상화하여 관리합니다. 이를 통해 호스트 운영체제(OS)의 물리적 파일 시스템과의 직접적인 접촉을 차단하고 완벽하게 격리된 환경을 제공합니다.

```
+-------------------------------------------------------+
|                 AI Agent (e.g., CLI tools)             |
+-------------------------------------------------------+
                           |
                           v (POSIX Syscalls: read, write, etc.)
+-------------------------------------------------------+
|           Host Kernel VFS (Virtual Filesystem)        |
+-------------------------------------------------------+
                           |
                           v (FUSE / NFS loopback)
+-------------------------------------------------------+
|               AgentFS Userspace Daemon                |
+-------------------------------------------------------+
                           |
                           v (SQL Queries)
+-------------------------------------------------------+
|               SQLite Database Backend                 |
|  (fs_inode, fs_dentry, fs_data, timeline tables)      |
+-------------------------------------------------------+
```

### 🛠️ 핵심 구성 기법
1. **FUSE & NFS 마운트 지원**:
   - **Linux**: FUSE (Filesystem in Userspace) 커널 모듈을 통해 커널 VFS 호출을 가로채 사용자 공간 데몬으로 전달한 뒤 SQL 질의로 매핑합니다.
   - **macOS**: FUSE 지원의 기술적 제약을 극복하기 위해 로컬 NFS 루프백 마운트를 연동하여 동일한 POSIX 가상 디렉토리 인터페이스를 제공합니다.
2. **커널 캐싱 및 쓰기 최적화**:
   - VFS-사용자 공간 데몬 간의 빈번한 컨텍스트 스위칭 지연을 보완하기 위해 Linux 커널 페이지 캐시를 활성화합니다.
   - 읽기 작업은 첫 로드 후 캐시에서 즉시 반환되며, 쓰기는 **Writeback 캐시** 기법을 통해 SQLite 데이터베이스 파일에 비동기적으로 대입되어 트랜잭션 오버헤드를 완화합니다.

---

## 2. 주요 혁신 기능

### 1) Copy-on-Write (CoW) 기반 파일 격리 샌드박스
- 에이전트가 실행을 시작할 때, 기존의 소스 코드 트리나 파일 구조(Base Layer)는 읽기 전용으로 보호됩니다.
- 에이전트가 코드를 빌드하거나 파일을 수정/작성하면 변경 사항만 SQLite의 **Delta Layer**에 작성됩니다.
- 물리적 호스트 파일을 일체 훼손하지 않으므로 에이전트가 파괴적인 시스템 명령(예: `rm -rf /`)이나 악성 코드 수정을 실행하더라도 안전합니다.

### 2) 데이터베이스 백엔드 스키마 표준화
AgentFS 내부 파일 구조는 아래와 같이 SQLite 테이블 형식으로 관리됩니다:
*   **`fs_dentry`**: 가상 디렉토리 트리 구조를 구성합니다. parent-child 관계를 트리 형태로 추적합니다.
    ```sql
    CREATE TABLE fs_dentry (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        parent_ino INTEGER NOT NULL, 
        ino INTEGER NOT NULL, 
        UNIQUE (parent_ino, name)
    );
    ```
*   **`fs_inode`**: POSIX 표준 메타데이터(크기, 권한, 수정 시간 등)와 삭제 마커(`whiteout`)를 저장합니다.
*   **`fs_data`**: 실제 파일 콘텐츠를 바이너리 또는 텍스트 델타 형식으로 관리합니다.

### 3) 스냅샷 기반의 재현성 (Reproducibility)
- 에이전트의 전체 상태(수정 파일, 생성 파일, 설정, 도구 실행 정보)가 단일 `.db` 파일로 존재하기 때문에 단순히 `cp agent.db snapshot.db`를 수행하는 것만으로 완벽한 스냅샷 백업이 가능합니다.
- 특정 비정상 작동 발생 시 해당 `.db` 파일 상태로 에이전트 런타임 환경을 롤백하거나 다른 기기로 즉시 복제하여 원격 디버깅을 실행할 수 있습니다.

### 4) SQL 기반 행동 감사 (Forensic Auditing)
- 에이전트가 실행한 모든 파일 쓰기, 읽기, 도구 호출 타임라인이 SQLite 내의 감사 로그 테이블에 영구 저장됩니다.
- 개발자는 에이전트 작동 후 아래와 같은 SQL 질의로 오동작 원인을 정밀 추적할 수 있습니다.
  ```sql
  SELECT timestamp, action_type, filepath, payload 
  FROM agent_audit_logs 
  WHERE status = 'error';
  ```

---

## 3. CLI 주요 명령어 및 사용 시나리오

AgentFS CLI는 에이전트 샌드박스 환경을 신속하게 부트스트랩하도록 지원합니다.

*   **가상 드라이브 초기화**:
    ```bash
    agentfs init my-session
    ```
*   **격리 공간에서 에이전트 명령 구동**:
    ```bash
    agentfs run -s my-session "npm run build && vitest run"
    ```
    (에이전트가 가상 공간 내 빌드 산출물과 테스트 스크립트를 변경해도 호스트 소스 트리는 오염되지 않음)
*   **가상 공간 디렉토리 마운트**:
    ```bash
    agentfs mount my-session ./workspace_debug
    ```
    (로컬 IDE나 터미널의 `git`, `grep`, `cat` 등으로 가상 경로 내부 파일 직접 탐색 가능)
*   **에이전트 행동 타임라인 출력**:
    ```bash
    agentfs timeline my-session
    ```

---

## 4. 타 플랫폼과의 연계 및 확장성

*   **[[wiki/Agents/Implementation/Supermemory-Architecture-and-MCP.md|Supermemory]] (SMFS)와의 차이점**:
    - **SMFS**: 에이전트가 기억하는 메모리를 가상 디렉토리 구조로 탐색하여 메모리 RAG의 성능과 탐색 효율을 극대화하는 인덱싱 기법에 특화.
    - **AgentFS**: 에이전트의 개발 환경 자체를 격리하고 가상 디스크 드라이브를 제공하여 안정성과 도구 실행 무결성을 확보하는 로컬/원격 샌드박스에 특화.
*   **[[wiki/Agents/Implementation/Deep-Agents-Sandbox.md|Deep-Agents-Sandbox]]**:
    - 외부 컨테이너 기반 샌드박스(E2B 등)와 달리, AgentFS는 로컬 파일 시스템에 마운트하여 컨테이너 오버헤드 없이 초고속으로 동작 가능.
*   **Turso Cloud 복제 및 영속성**:
    - 로컬 SQLite의 실시간 복제 기술을 통해 상태를 원격 Turso Cloud에 동기화할 수 있습니다.
    - 이를 통해 서버리스(Serverless) 함수 같은 에페머럴(Ephemeral, 휘발성) 컴퓨팅 인프라 환경에서도 에이전트의 구동 상태와 파일 데이터가 소실되지 않고, 다양한 기기나 환경을 넘나들며(cross-machine) 영속성을 유지할 수 있습니다.
*   **다국어 SDK 지원**:
    - CLI를 통한 격리 래핑 외에도, **TypeScript, Python, Rust용 SDK**를 제공합니다. 개발자는 커스텀 에이전트 프레임워크 빌드 시 가상 파일시스템, KV 저장소, 행동 감사 로그를 소스코드 단에서 직접 프로그래밍 방식으로 유연하게 제어할 수 있습니다.

---

**관련 문서**:
- [[wiki/Agents/Implementation/000_Implementation-MOC.md]]
- [[wiki/Agents/Implementation/Deep-Agents-Sandbox.md]]
- [[wiki/Agents/Implementation/Supermemory-Architecture-and-MCP.md]]
- [[wiki/Agents/Memory-and-Cognition/000_Memory-and-Cognition-MOC.md]]
