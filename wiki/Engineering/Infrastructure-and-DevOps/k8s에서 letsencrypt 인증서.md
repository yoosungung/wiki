---
title: "k8s에서 letsencrypt 인증서"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/k8s에서 letsencrypt 인증서.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

google:search{queries:[kubernetes cert-manager letsencrypt setup guide,cert-manager nginx ingress letsencrypt setup,cert-manager ClusterIssuer vs Issuer,k8s ingress tls configuration example]} Kubernetes에서 Let's Encrypt 인증서를 적용하는 표준적인 방법은 **cert-manager**를 사용하는 것입니다. 다음은 3단계 요약입니다.

### 1. cert-manager 설치

클러스터에 인증서 관리 도구를 설치합니다.

Bash

```
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml
```

### 2. ClusterIssuer 생성

인증서를 발급해줄 주체(Let's Encrypt)를 정의합니다. 아래 내용을 `cluster-issuer.yaml`로 저장 후 적용(`kubectl apply -f ...`)하세요.

YAML

```
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    # Let's Encrypt 프로덕션 서버 주소
    server: https://acme-v02.api.letsencrypt.org/directory
    email: your-email@example.com  # 본인 이메일로 변경 (만료 알림용)
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx  # 사용 중인 인그레스 컨트롤러 클래스 (예: nginx)
```

### 3. Ingress 설정 수정

웹 앱의 Ingress 리소스에 `annotations`와 `tls` 설정을 추가합니다.

YAML

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-web-app-ingress
  annotations:
    # 위에서 만든 ClusterIssuer 이름 지정
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - my-app.example.com
    secretName: my-app-tls  # 인증서가 저장될 시크릿 이름 (자동 생성됨)
  rules:
  - host: my-app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-web-service
            port:
              number: 80
```

설정 후 잠시 기다리면 cert-manager가 자동으로 인증서를 발급하고 `my-app-tls` 시크릿을 생성하여 HTTPS를 활성화합니다.

---

[Kubernetes HTTPS with cert-manager and Let's Encrypt](https://www.youtube.com/watch?v=KAa2l0oycOk)

이 영상은 cert-manager 설치부터 Let's Encrypt 인증서 발급 및 적용까지의 전체 과정을 단계별 데모로 보여주어 이해를 돕습니다.