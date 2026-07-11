---
title: "개발 환경 구성 - Part 2 - Linux와 Poetry"
related_raw: ["[[wiki/Engineering/Development-Environment/개발 환경 구성 - Part 2 - Linux와 Poetry.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment', 'dev_setup_guides']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# 개발 환경 구성 - Part 2 - Linux와 Poetry

# 3. Linux 환경 설정
- 설치한 Linux 배포판을 시작합니다.  
VSCode에서 Remote - WSL을 설정한 경우 ```ctl-j```를 눌러 WSL의 터미널을 열고, 그 환경에서 작업을 진행 합니다. 아닌 경우 wsl 명령을 입력해 직접 터미널을 열 수 있습니다.  
    [Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)
- 기본적인 도구들을 설치합니다. sudo 암호틑 WSL 실치 시 등록한 암호를 입력 합니다.
    ```
    sudo apt update && sudo apt upgrade
    sudo apt install python3-pip python3-venv git -y
    ```
# 4. Poetry 설치
Poetry는 Python 프로젝트의 의존성 관리와 패키지 작성을 쉽게 도와주는 도구입니다.
- Poetry 공식 설치 스크립트를 사용하여 설치합니다:
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
- 설치 후, shell 설정 파일(.bashrc, .zshrc 등)에 PATH 추가:
    ```
    export PATH="$HOME/.local/bin:$PATH"
    ```
- 변경사항을 적용하기 위해 쉘을 재시작하거나 source 명령어를 사용합니다:
    ```
    source ~/.bashrc
    ```
- 프로젝트 별 가상환경을 config에 설정합니다.
    ```
    poetry config virtualenvs.in-project true
    ```
    [Basic usage](https://github.com/python-poetry/poetry/blob/main/docs/basic-usage.md)

---

## 이전

- [[wiki/Engineering/Development-Environment/개발 환경 구성]]

## 다음

- [[wiki/Engineering/Development-Environment/개발 환경 구성 - Part 3 - 프로젝트 설정]]
