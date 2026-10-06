---
id: inbox-pm-unitutor-pwa-option-b-intent-pass
agent: pm
ticket_id: 2ed8b767-9598-4bf1-ac3b-7f4fe9f8771b
updated: 2026-10-07
status: inbox
sources:
  - ticket:2ed8b767-9598-4bf1-ac3b-7f4fe9f8771b
  - https://github.com/yoosungung/UniTutorAI/pull/31
  - inbox/uni-tutor/2026-10-07-unitutor-pwa-installable-shell.md
---

# UniTutor PWA Option B — Intent pass

- Scope locked **B**: docs + installable shell (`manifest`·icons·`display`); offline lecture/tutor cache · server Push · store apps = Non-goal.
- Merged: `yoosungung/UniTutorAI#31` → `0d205c195ada785dffbf0788aab16bc70ea16c67`.
- SW stays CardFaded notify-only (`caches.open|match` forbidden in test).
