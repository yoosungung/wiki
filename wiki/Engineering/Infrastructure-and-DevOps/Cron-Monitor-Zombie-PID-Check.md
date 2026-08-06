---
id: cron-monitor-zombie-pid-check
title: "Cron 모니터: zombie PID를 살아있다고 보지 않기"
status: canonical
owner: km
updated: "2026-08-06"
last_updated: "2026-08-06"
review_after: "2026-11-06"
sources:
  - ticket:250
  - ticket:238
  - ticket:176
tags: ["Infrastructure", "DevOps", "Cron", "PID", "Launcher"]
type: "wiki"
---

# Cron 모니터: zombie PID를 살아있다고 보지 않기

`kill -0 $pid`는 `/proc/$pid` **State=Z(zombie)**에도 성공한다. 워커가 이미 끝났는데 모니터가 `running`으로 남겨 **exit 99**(process disappeared / empty worker.log)가 난다.

## 수정

```bash
# 잘못된 예
kill -0 "$pid" && echo running

# 권장: /proc/$pid/stat 또는 status에서 State!=Z (+ 존재)
is_pid_running() {
  local st
  st=$(awk '{print $3}' "/proc/$1/stat" 2>/dev/null) || return 1
  [[ "$st" != "Z" ]]
}
```

## 운영 축 분리

1. **Launcher 실행성**: PVC 0644 → `setsid bash` — [[wiki/Engineering/Infrastructure-and-DevOps/PVC-Nonexec-Script-Setsid-Bash.md]].
2. **ConfigMap reseed**: bare `nohup`/`exec "$@"`가 PVC hotfix를 덮어쓰면 빈 로그·exit 99 재발 → **repo `agent/cron/` SSoT**, skill 경로는 thin `exec` shim.
3. **로그 경로**: `/tmp/...`만 쓰면 Pod 재시작 시 유실 → durable state 경로.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/PVC-Nonexec-Script-Setsid-Bash.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agent-Runner-Zombie-Active-Run-Recovery.md]]
