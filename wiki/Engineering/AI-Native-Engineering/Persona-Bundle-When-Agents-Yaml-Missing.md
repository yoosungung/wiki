---
id: persona-bundle-when-agents-yaml-missing
title: "agents.yaml 없을 때 persona_bundle로 ConfigMap 재구성"
status: canonical
owner: km
updated: "2026-08-20"
last_updated: "2026-08-20"
review_after: "2026-11-20"
sources:
  - ticket:1046
tags: ["Engineering", "AI-Native", "Kubernetes", "Persona", "Deploy"]
type: "wiki"
---

# agents.yaml 없을 때 persona_bundle로 ConfigMap 재구성

`deploy/k8s/agents.yaml`이 gitignore되어 로컬에 없으면 full `render-agents.sh`가 막힌다. merge SHA의 `deploy/personas`에서 **persona_bundle**로 ConfigMap을 재구성한 뒤 apply·STS restart로 스킬 버전을 올린다.

## 절차

```bash
# 개념: merge_sha 체크아웃 후
# 1) persona_bundle.build_persona_bundle("<role>", …) 로 ConfigMap 본문 생성
# 2) live roadmap-registry / *.pulled 보존 (덮어쓰지 않음)
# 3) kubectl apply -f <persona ConfigMap>
# 4) kubectl rollout restart sts/cursor-agent-<role>
```

## 검증

| 체크 | 기대 |
| :--- | :--- |
| ConfigMap skill 본문 | `version:` + Intent Pass(또는 해당 스킬) 문구 |
| Pod 파일 | `/cursor-home/.cursor/skills/<skill>/SKILL.md`가 동일 version |
| readyz | HTTP 200 |

merge만으로 live ConfigMap이 바뀌지 않는다. SA가 ConfigMap patch 불가하면 TA/인간 apply가 필요하다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Intent-Pass-Diff-First-Merge.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
