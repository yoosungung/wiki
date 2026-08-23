---
title: "오픈소스로 공개한 DeepSeek Harness(dsh) 가 화제입니다."
related_raw: ["[[raw/오픈소스로 공개한 DeepSeek Harness(dsh) 가 화제입니다..md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# 오픈소스로 공개한 DeepSeek Harness(dsh) 가 화제입니다.

이제 AI 는 죽어서도 Preset 을 남긴다 DeepSeek 이 8월 13일 오픈소스로 공개한 DeepSeek Harness(dsh) 가 화제입니다. 공개 5일 만에 GitHub 스타 150,000개를 돌파하며 중국 뿐만 아니라 전 세계 개발자 커뮤니티의 주목을 받았습니다. 저 또한 이번 연휴 기간 가장 재밌게 살펴본 내용 중 하나였습니다. 그런데 이 프로젝트의 핵심은 모델이 아닙니다. README 첫 줄에 적힌 철학 한 줄, "Everything is a plugin." 이 원칙이 AGENT = MODEL + HARNESS 라는 공식에서 상당히 근본적인 설계 원칙이 됩니다. 하나씩 간단히 살펴보겠습니다. deepseek harness preset note: [https://lnkd.in/gcvGq-Wf](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2FgcvGq-Wf&urlhash=UzcO&trk=public_post-text) 1/ 특권을 가진 코어가 없다 모델 어댑터, 툴 레지스트리, 세션 로그, 에이전트 루프, 샌드박스, UI까지 전부 Cordis 플러그인이다. 하드코딩된 중심 없이, 설정 파일([cordis.yml](http://cordis.yml/?trk=public_post-text)) 하나로 어떤 레이어든 교체할 수 있다. 2/ Preset 은 Agent 의 배포 단위다 같은 플러그인 풀에서 조합만 바꾸면 완전히 다른 Agent가 된다. - Standard(풀 코딩 에이전트) - Code(모델이 TypeScript로 다중 툴 오케스트레이션) - Minimal(bash + 에디터만, 벤치마크용) - Creator(런타임을 탐색하고 새 Preset을 설계) 네 가지 모드가 전부 같은 코드베이스에서 나온다. 3/ Skill 과 Preset 의 결정적 차이 경쟁사 분석 Skill 은 Agent 에게 분석 방법을 가르친다. 하지만 경쟁사 분석 Preset 은 그 Skill 에 웹 검색, Browser, PDF, Python, Subagent, 리서치 Prompt, 컨텍스트 전략을 전부 조합해서 개봉 즉시 쓸 수 있는 Agent 를 통째로 건넨다. Skill 은 하나의 기술이고, Preset 은 완성된 애플리케이션이다. 4/ 두 개의 시장이 열린다 한 층은 Plugin / Skill Marketplace. 개발자와 고급 사용자가 Agent 를 직접 조립하는 시장이다. 다른 한 층은 Preset / Agent Marketplace. 일반 사용자에게 완성된 Agent 를 바로 건네는 시장이다. App Store 가 완성된 App을 보여주듯, Preset Marketplace 는 완성된 Agent 애플리케이션을 보여준다. 흥미로운 건 이 구조가 과거의 흐름을 정확히 반복한다는 점입니다. 'Everything is a plugin' 이라는 철학 아래 모든 것이 플러그인이면 모든 것이 조합 가능하고, 조합 가능하면 Preset 이라는 배포 단위가 자연스럽게 등장한다는 것이죠. 이 배포 단위 구축의 용이성에 따라 또 한 번 많은 정보가 재확산될 것으로 예상됩니다. 별개의 이야기이지만 deepseek-harness repo 를 꼭 읽어보셨으면 합니다. 한 명의 개인이 아닌 팀이 AI 와 함께 개발하는 모습이 가장 잘 드러난 저장소이기 때문입니다. 해당 repo 를 살펴보시면.agents 디렉토리 안에 notes/와 skills/가 체계적으로 정리되어 있는데, 아키텍처 결정이 Agent Note 로 기록되고 dsh-code-review, dsh-prose-standard, dsh-pre-push-checks 같은 내부 Skill 이 팀의 개발 워크플로우 자체에 녹아 있습니다. 하나의 조직이 컨텍스트를 어떻게 관리하고 축적하는지, 그 구조를 읽는 것만으로도 상당히 인상 깊습니다. 꼭 필요한 AI 정보를 지속적으로 업로드하고 있습니다. 저와 "1촌" 이 되면 유용한 정보를 놓치지 않을 거에요.

---
- **Source:** Unknown
