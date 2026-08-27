---
tags:
  - inbox
type: wiki
status: published
---

# cpdown Webpage to Markdown

**cpdown**은 모든 웹페이지의 본문이나 YouTube 자막을 단 한 번의 클릭이나 단축키로 깔끔한 마크다운(Markdown) 형태로 복사해 주는 오픈소스 브라우저 확장 프로그램입니다.

## 주요 기능 및 특징
*   **본문 추출 및 정제**: Defuddle 또는 Mozilla Readability를 사용하여 스크립트, 스타일, iframe 등 불필요한 HTML 요소를 제거하고 순수한 텍스트 본문만 추출합니다.
*   **LLM 친화적**: 복사된 콘텐츠의 총 토큰(Token) 수를 표시해 주어, 복사한 텍스트를 LLM 프롬프트에 붙여넣기 전 용량을 가늠할 수 있게 도와줍니다.
*   **사용자 편의성**:
    *   Chrome 웹 스토어와 Firefox 애드온을 통해 쉽게 설치할 수 있습니다.
    *   복사된 마크다운을 백틱(```) 3개로 감싸는 기능, 성공 알림(Toast, Raycast Confetti) 표시 등의 옵션을 제공합니다.
    *   `bun`을 활용해 소스코드를 직접 빌드하고 수동으로 설치할 수도 있습니다.
