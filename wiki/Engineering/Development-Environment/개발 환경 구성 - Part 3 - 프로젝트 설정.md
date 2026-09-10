---
title: "개발 환경 구성 - Part 3 - 프로젝트 설정"
related_raw: ["[[wiki/Engineering/Development-Environment/개발 환경 구성 - Part 3 - 프로젝트 설정.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment', 'dev_setup_guides']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# 개발 환경 구성 - Part 3 - 프로젝트 설정

# 5. 프로젝트 설정
- 새 프로젝트 폴더를 만들고 해당 폴더로 이동합니다:
    ```
    mkdir mylangchainapp && cd mylangchainapp
    ```
- Poetry를 사용하여 새 Python 프로젝트를 초기화합니다:
    ```
    poetry init
    ```
- pyproject.toml 파일을 수정 합니다.  
    ```
    ...
    [tool.poetry.dependencies]
    python = "^3.11"
    langchain = "^0.1.13"
    pyhcx = { path="packages/pyhcx-0.9.2-py3-none-any.whl" }
    langchain-hcxai = { path="packages/langchain_hcxai-0.1.2-py3-none-any.whl" }
    ...
    ```  
- pyhcx와 langchain-hcxai 파일을 저장한 폴더와 파일명을 입력합니다. 2개의 파일은 Didim365 담당자에 수령합니다.  
    ```
    pyhcx: HyperCloverX python client
    langchain-hcxai: HyperCloverX labgchain lib
    ```
- 그 외의 필요한 패키지들을 Poetry를 통해 설치합니다.
psycopg2-binary 패키지를 예로 들면:
    ```
    poetry add psycopg2-binary
    ```
  
# 6. VSCode에서 프로젝트 작업
- VSCode를 열고, Ctrl+Shift+P를 눌러 Command Palette를 엽니다.
- "Remote-WSL: New Window"를 선택하여 WSL에서 새 창을 엽니다.
- 파일 > 폴더 열기...를 선택하고, 프로젝트 디렉토리를 선택합니다.
- VSCode에서 python 확장을 설치합니다. Python, Pylance, Python Debugger
- VSCode의 터미널에서 Poetry 환경을 활성화합니다:
    ```
    crl-shift-p "Python Interpreter" poetry환경 선택
    ```
    [VSCode: Adding Poetry Python Interpreter](https://www.markhneedham.com/blog/2023/07/24/vscode-poetry-python-interpreter/)
  
## 이제 WSL2, VSCode, Poetry를 사용한 LangChain 응용 프로그램 개발 환경이 준비되었습니다. 프로젝트 개발을 시작할 수 있습니다!

---

## 이전

- [[wiki/Engineering/Development-Environment/개발 환경 구성]]
- [[wiki/Engineering/Development-Environment/개발 환경 구성 - Part 2 - Linux와 Poetry]]
