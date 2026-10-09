---
id: inbox-crewrp-docs-tab-emu-smoke
agent: crewrp
ticket_id: 512000ad-8c3f-4f06-8604-9511b81ca218
updated: 2026-10-09
status: inbox
sources:
  - ticket:512000ad-8c3f-4f06-8604-9511b81ca218
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
  - merge:d03ff30d2b30806191bd2d4dae2db9697fe00cd9
---

# CrewRP 자료실 목록→상세 에뮬 스모크

- Pixel_API_36 + ai-edu 로그인 세션에서 자료실: 파일·폴더 목록 + `이름·경로 검색` 필드 (칩+본문 split 없음).
- README.md 탭 → 상세(편집/삭제/닫기). `guides` 폴더 진입·`상위` 복귀. 검색 `readme` → README만.
- 폴더 검증용으로 `docs/guides/onboard.md`를 잠시 생성 후 삭제 시도. 에뮬 cold-boot는 셸 포그라운드 유지 필요(백그라운드 nohup이면 qemu가 죽음).
