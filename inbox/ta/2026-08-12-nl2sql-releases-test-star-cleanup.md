---
id: inbox-ta-nl2sql-releases-test-star-cleanup
agent: ta
ticket_id: 549
updated: 2026-08-12
status: inbox
sources:
  - ticket:549
  - https://github.com/yoosungung/nl2sql-releases/releases
---

# nl2sql-releases: test-* Release 일괄 삭제 + Latest 복구

- `gh release delete <tag> --repo yoosungung/nl2sql-releases --yes --cleanup-tag`로 tip 오염 Release 제거.
- `gh release edit v0.1.3 --repo … --latest`로 Latest를 semver Prod 태그로 복구.
- tip 이미지는 GHCR/`build-ghcr-images`만 — public Release에 `test-*`를 두지 않음.
