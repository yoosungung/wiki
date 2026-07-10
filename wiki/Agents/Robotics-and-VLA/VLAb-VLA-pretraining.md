---
title: "VLAb-VLA-pretraining"
related_raw: ["[[wiki/Agents/Robotics-and-VLA/VLAb-VLA-pretraining.md]]"]
tags: ['wiki', 'agents_and_systems', 'robotics_&_physical_ai_(vla)']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# VLAb: VLA 사전 학습을 위한 연구실

VLAb는 로봇 공학 데이터셋에서 VLA(Vision-Language-Action) 모델을 사전 학습하기 위한 간소화된 라이브러리입니다. [LeRobot](https://github.com/huggingface/lerobot)에서 파생되었으며, 다중 GPU 설정 및 SLURM 클러스터 전반에 걸쳐 효율적인 사전 학습 워크플로우에 중점을 둡니다. SmolVLA의 공식 재현 키트로 간주될 수 있습니다.

주요 기능은 다음과 같습니다.
*   **사전 학습 중심 아키텍처**: 환경 설정 오버헤드 없이 실제 데이터셋에서 빠르게 반복할 수 있도록 내장된 아키텍처 및 데이터 처리 로직을 포함합니다.
*   **SmolVLA 재현**: SmolVLA 사전 학습을 위한 공식 재현 키트로, 원본 모델 학습에 사용된 것과 거의 동일한 데이터셋, 구성 및 워크플로우를 포함합니다.
*   **간단한 설정 및 종속성 감소**: `conda env create -f environmen[1]t.yml` 명령 하나로 환경을 생성할 수 있습니다.
*   **분산 학습**: Accelerate를 통한 다중 GPU 및 다중 노드 지원을 제공하며, 단일 머신 및 SLURM 클러스터에서 테스트되었습니다.
*   **다중 데이터셋 지원**: 구성 가능한 샘플링 전략을 통해 여러 데이터셋을 동시에 학습할 수 있습니다.

## 설치
1.  `conda env create -f environment.yml` 및 `conda activate vlab`를 사용하여 환경을 생성합니다.
2.  `export PYTHONPATH="${PWD}/src:${PYTHONPATH}"`를 사용하여 Python 경로를 설정합니다.
3.  `python tests/test_installation.py`를 실행하여 설치를 확인합니다.
4.  (선택 사항) HuggingFace Hub에서 데이터셋이나 모델을 다운로드하는 경우 `huggingface-cli login`으로 로그인합니다.

## SmolVLA 학습 재현
SmolVLA 사전 학습 데이터셋을 사용하고 SmolVLA 결과를 재현하려면 다음 커뮤니티 데이터셋을 사용합니다.
*   [Community Dataset v1](https://huggingface.co/datasets/HuggingFaceVLA/community_dataset_v1): 128개 데이터셋 (11.1K 에피소드, 5.1M 프레임, 46.9시간, 119.3GB)
*   [Community Dataset v2](https://huggingface.co/datasets/HuggingFaceVLA/community_dataset_v2): 340개 데이터셋 (6.3K 에피소드, 5M 프레임, 46.6시간, 59GB)

## LeRobot로 마이그레이션
VLAb의 체크포인트는 정규화 형식 업데이트로 인해 최신 LeRobot 버전과 직접 호환되지 않을 수 있습니다. 사전 학습된 모델을 LeRobot와 함께 사용하려면 [마이그레이션 스크립트](https://github.com/huggingface/lerobot/blob/f6b16f6d97155e3ce34ab2a1ec145e9413588197/src/lerobot/processor/migrate_policy_normalization.py#L4)를 사용하여 체크포인트를 변환하고, [LeRobot 미세 조정 가이드](https://huggingface.co/docs/lerobot/smolvla)를 따릅니다.

## 문제 해결
손상된 파일, 오래된 메타데이터 또는 지속적인 오류가 발생하는 경우 `rm -rf ~/.cache/huggingface/datasets`, `rm -rf ~/.cache/huggingface/hub`, `rm -rf ~/.cache/huggingface/tran[1]sformers` 명령으로 캐시를 수동으로 정리할 수 있습니다. SLURM 스크립트에서는 `CLEAN_CACHE=true`를 설정하여 학습 전에 캐시를 자동으로 정리할 수 있습니다.

## 추가 자료
*   [LeRobot GitHub](https://github.com/huggingface/lerobot)
*   [SmolVLA Fine-tuning Guide](https://huggingface.co/docs/lerobot/smolvla)
*   [LeRobot Installation](https://huggingface.co/docs/lerobot/en/installation)
*   [Accelerate Documentation](https://huggingface.co/docs/accelerate)

## 인용
이 라이브러리를 연구에 사용하는 경우 다음을 인용해 주십시오.
```bibtex
@misc{aubakirova2025vlab,
 author = {Dana Aubakirova, Mustafa[1] Shukor and Jade Cholgari and Leandro von Werra},
 title = {VLAb: Your Laboratory for Pretraining VLAs},
 year = {2025},
 publisher = {GitHub},
 journal = {GitHub repository},
 howpublished = {\url{https://github.com/huggingface/vlab}}
}
```
SmolVLA 논문:
```bibtex
@article{shukor2025smolvla,
 title = {SmolVLA: A vision-language-action model for affordable and efficient robotics},
 author = {Shukor, Mustafa and Aubakirova, Dana and Capuano, Francesco and Kooijmans, Pepijn and Palma, Steven and Zouitine, Adil and Arac[1]tingi, Michel and Pa[1]scal, Caroline and Russi, Martino and Marafioti, Andres and Alibert, Simon and Cord, Matthieu and Wolf, Thomas and Cadene, Remi},
 year = {2025},
 journal = {arXiv preprint},
 eprint = {2506.01844},
 archivePrefix = {arXiv},
 primaryClass = {cs.RO}
}
```

**라이선스:**
이 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](https://github.com/huggingface/VLAb/blob/main/LICENSE) 파일을 참조하십시오.

[출처](https://github.com/huggingface/VLAb/blob/main/README.md)