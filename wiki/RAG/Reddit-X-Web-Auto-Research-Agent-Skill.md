# Reddit, X, Web 자동 리서치 에이전트 스킬 (/last30days)

## 핵심 주장 (Claims)
에디터가 아닌 사람들의 실제 관심사(Reddit 업보트, X 좋아요, Polymarket의 실제 투자금 등)를 바탕으로 최근 30일간의 트렌드와 정보를 검색하고 요약하는 AI 에이전트 스킬입니다. 구글 검색으로는 얻을 수 없는 분산된 플랫폼들의 리얼타임 반응과 컨센서스를 하나의 통합된 브리핑으로 제공합니다.

## 기능 및 디자인 (Design & Features)
- **병렬 검색**: Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub 등 다수의 플랫폼을 동시에 검색.
- **군중 기반 점수화(Scoring)**: 단순 SEO가 아닌 사람들의 실제 참여도(업보트, 조회수, 좋아요)에 따라 중요도를 평가.
- **다양한 소스 지원**:
  - Reddit: 실제 업보트가 반영된 댓글 및 필터링 안 된 여론.
  - X / Twitter: 최신 스레드와 실시간 반응.
  - YouTube: 영상 전체 트랜스크립트 파싱.
  - Polymarket: 실제 돈이 걸린 예측 시장 확률.
  - GitHub: PR 속도, 이슈 및 논의 사항.
- **통합 브리핑**: AI가 여러 소스의 데이터를 취합해 인용(citation)이 포함된 근거 있는 요약(brief)을 생성.

## 시스템 구조 (Architecture)
- **멀티 쿼리 확장**: 주제에 따라 인물, 회사, 제품 등으로 분해하여 최적의 해시태그, 서브레딧, 핸들을 찾아냄.
- **클러스터링 및 병합**: 서로 다른 플랫폼(예: Reddit, X, TikTok)에서 발생한 동일한 이벤트(예: 콘서트 취소)를 묶어서 중복을 제거.
- **플러그인 아키텍처**: OpenAI Codex, Claude Code, Cursor, Copilot, Gemini CLI 등 다양한 Agent Skills 호스트에서 구동 가능.

## 설치 및 CLI 커맨드
**Claude Code를 통한 설치 (권장)**:
```bash
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

**Agent Skills 호스트용 (Codex, Cursor 등)**:
```bash
npx skills add mvanhorn/last30days-skill -g
```

**사용 예시**:
```bash
/last30days Peter Steinberger
/last30days Listen Labs --hiring-signals
/last30days "AI coding agents" --emit=json
```
