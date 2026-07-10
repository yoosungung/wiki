---
title: "Enable S2 Attention"
related_raw: ["[[wiki/Models/SFT/Enable S2 Attention.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_options']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

"Use shift short attention proposed by LongLoRA"**는 LongLoRA라는 논문에서 제안된 Shift Short Attention 메커니즘을 사용하는 것을 의미합니다. LongLoRA는 대규모 언어 모델의 효율적인 학습과 추론을 위해 제안된 기법으로, 긴 시퀀스 데이터를 처리할 때 성능을 최적화하기 위해 설계되었습니다. Shift Short Attention은 이러한 긴 시퀀스에서의 주의(attention) 메커니즘을 개선하는 핵심 기법 중 하나입니다.

### Shift Short Attention의 개념

#### LongLoRA

LongLoRA는 "Long Sequence Learning via Low-Rank Adaptation"의 약자로, 긴 시퀀스를 학습하는 데 있어 효율성을 높이기 위한 여러 기법을 제안합니다. 이 논문에서는 특히 긴 시퀀스 데이터를 효과적으로 처리하기 위한 주의 메커니즘과 관련된 기법들을 다룹니다.

#### Shift Short Attention

Shift Short Attention은 긴 시퀀스를 처리할 때, 기존의 전역 주의(global attention)와 국소 주의(local attention)를 혼합하여 사용하는 방법입니다. 이는 모델이 긴 시퀀스를 보다 효율적으로 처리할 수 있도록 설계되었습니다.

1. **Global Attention**:
    
    - 시퀀스의 모든 토큰들 간의 상호작용을 고려하는 전통적인 주의 메커니즘.
    - 긴 시퀀스에서 연산 복잡도가 매우 높아질 수 있습니다.
2. **Local Attention**:
    
    - 시퀀스의 특정 창(window) 내의 토큰들 간의 상호작용만을 고려합니다.
    - 연산 복잡도를 줄이지만, 장기적인 종속성(long-term dependency)을 캡처하는 데 한계가 있습니다.
3. **Shift Short Attention**:
    
    - Local Attention의 창을 주기적으로 이동(shift)시켜, 모든 토큰이 한 번 이상 주의 메커니즘에 포함되도록 합니다.
    - 이 방법은 Local Attention의 효율성을 유지하면서도 장기적인 종속성을 캡처할 수 있게 합니다.

### Shift Short Attention의 작동 방식

1. **윈도우 설정**:
    
    - 시퀀스를 특정 길이의 창(window)로 나눕니다.
2. **윈도우 이동**:
    
    - 각 창을 일정 간격으로 이동시켜, 모든 토큰이 주의 메커니즘에 포함되도록 합니다.
3. **주의 계산**:
    
    - 각 창 내의 토큰들에 대해 주의 메커니즘을 적용합니다.
4. **결합**:
    
    - 각 창에서 계산된 주의 결과를 결합하여 최종 출력을 생성합니다.

### 예제 코드 (PyTorch)

아래는 PyTorch를 사용하여 Shift Short Attention을 구현하는 간단한 예제입니다. 실제 LongLoRA 논문에서 제안된 모든 최적화 기법을 포함하지는 않지만, 개념을 이해하는 데 도움이 됩니다.
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ShiftShortAttention(nn.Module):
    def __init__(self, embed_dim, num_heads, window_size, shift_size):
        super(ShiftShortAttention, self).__init__()
        self.window_size = window_size
        self.shift_size = shift_size
        self.attention = nn.MultiheadAttention(embed_dim, num_heads)

    def forward(self, x):
        bsz, seq_len, embed_dim = x.size()
        windows = []

        # Create windows with shifts
        for start in range(0, seq_len, self.shift_size):
            end = min(start + self.window_size, seq_len)
            window = x[:, start:end, :]
            if window.size(1) < self.window_size:
                padding = torch.zeros(bsz, self.window_size - window.size(1), embed_dim).to(x.device)
                window = torch.cat((window, padding), dim=1)
            windows.append(window)

        # Apply attention to each window
        attn_outputs = []
        for window in windows:
            attn_output, _ = self.attention(window, window, window)
            attn_outputs.append(attn_output)

        # Combine outputs
        combined_output = torch.cat(attn_outputs, dim=1)
        return combined_output[:, :seq_len, :]

# Parameters
embed_dim = 64
num_heads = 4
window_size = 10
shift_size = 5

# Model and data
model = ShiftShortAttention(embed_dim, num_heads, window_size, shift_size)
input_data = torch.randn(32, 100, embed_dim)  # Batch size 32, sequence length 100, embedding dimension 64

# Forward pass
output = model(input_data)
print(output.size())  # Expected output size: (32, 100, 64)
```