---
title: "Blog"
related_raw: ["[[raw/Blog.md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Blog

[Pioneer](https://pioneer.ai/)

[GLiNER](https://gliner.ai/)

[Discord](https://discord.gg/fastino)

Open-weights models have seen a period of unusually rapid development this summer. New releases have arrived at a near-weekly pace, with several *reaching performance levels comparable to leading closed models* on independent benchmarks.

This has significant implications for users who want to reduce AI costs and ultimately own their own models. Open weights models can be downloaded and fine-tuned for specific tasks and domains, giving organizations full control over the resulting weights rather than dependence on a third-party API.

In this post, we’ll go over the difference between open-weights and open-source models, explain what LLM fine-tuning is, offer advice on when to fine-tune (and when not to), discuss some of the most popular open weights models available for fine-tuning, and talk about fine-tuning strategies, including generating data, choosing fine-tuning techniques, and evaluating your fine-tuned model.

## Open-weights vs. open-source models

Not all LLMs can be fine-tuned by the public, and the dividing line is access to the model weights. Proprietary, or "closed," models like the Claude and GPT families can't be fine-tuned in the traditional sense because their weights aren't publicly available. Open-weights and open-source models can be, since both release the parameters needed to modify them. While the two terms are often used interchangeably, they describe different degrees of openness in how a model is released.

An open-source model is one whose weights, training dataset, and training code are released under a license that lets anyone freely use, study, modify, and redistribute the model. [Nemotron 3 Ultra](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/) by [NVIDIA](https://www.nvidia.com/) is a recent example of a fully open-source family of models, released under the new [OpenMDW-1.1 license](https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.1/LICENSE.OpenMDW-1.1). OpenMDW stands for open model, data, and weights.

An open-weights model refers to a model whose weights are released to the public, but without the underlying training data or training code. The permitted usage of open-weights models can vary. For instance, [GLM 5.2](https://huggingface.co/zai-org/GLM-5.2) is an open-weights model released under the MIT license, making it free for anyone to download and run, with self-hosting unrestricted for commercial use. [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) is also open weights, but released under a more restrictive license that attaches revenue-triggered conditions for commercial operators rather than the unrestricted terms of MIT.

For the purposes of this article, we’ll focus on open-weights models.

## What is LLM fine-tuning?

Fine-tuning is the process of taking a pre-trained language model and continuing to train it on a smaller, targeted dataset so that it adapts to a specific domain, task, or style. This adjusts the model's existing weights rather than training from scratch, which lets it specialize while retaining the general capabilities it learned during pre-training.

![](https://framerusercontent.com/images/sQ8kaLXbCrNn2uppHVIo31T10E.png?width=3600&height=1890)

Fine-tuning open weights models offers several advantages over relying on a general-purpose API:

- **Better task performance.** A fine-tuned smaller model can match or beat larger generalist models on the specific task it was trained for, since it specializes rather than spreading capacity across everything.
- **Lower latency and cost.** Fine-tuning lets a smaller model reach the needed quality, and smaller models run faster and cheaper per call than large frontier ones.
- **Customization.** The model adapts to your domain, terminology, formatting conventions, and tone rather than defaulting to generic outputs.
- **Data control and privacy.** With open weights, fine-tuning can happen on self-hosted infrastructure, keeping sensitive training data in-house.
- **Ownership.** The resulting weights are yours to deploy, version, and reuse without depending on a provider's API or pricing.

### Choosing between fine-tuning, RAG, and prompt engineering

Fine-tuning is not the only option for adapting a language model's behavior to a specific task or domain without training a model from scratch. Lower-lift options include retrieval augmented generation (RAG), which supplies the model with relevant external knowledge at inference time, and prompt engineering, which shapes the model's instructions and examples in the input to steer its outputs.

Here are some guidelines for choosing between fine-tuning, RAG, and prompt engineering:

- Use **prompt engineering** when you can get the behavior you want from your LLM simply by changing the instructions, examples, or structure of the input alone. It's the fastest and cheapest option to iterate on and is usually the right first step for most tasks.
- Use **RAG** when your LLM needs access to specific, external, or frequently changing knowledge that isn't in its training data and when you need responses grounded in citations.
- Use **fine-tuning** when you need consistent, reliable outputs across many cases, when a task requires a specialized style or format that's hard to hold with prompting alone, or when you want a smaller model to match the quality of a larger one so you can cut latency and cost.

## Selecting open weights base models

Selecting a base model is one of the most important decisions in fine-tuning because the process adjusts what a model already knows rather than teaching it from scratch, so the base model sets the ceiling on what you can achieve. That choice is harder than ever, with more high-quality open-weights models to pick from across a range of sizes and architectures.

Your target task, use case, and deployment constraints should all play a role in selecting a base model:

- **Task.** What you want the fine-tuned model to do. Examples include text summarization, classification, extraction, and more.
- **Use case.** How you want to use the fine-tuned model. Will it be user-facing or internal, used in agentic pipelines or as a standalone API?
- **Deployment constraints.** Where and how you will deploy your model to production. For instance, can you deploy to the cloud via a model or inference provider, or do you need your model to run on device?

Another important consideration when choosing a base model is model size. Generally speaking, the larger a base model is, the more challenging and expensive it is to fine-tune. Models under 70 billion parameters can be fine-tuned using PEFT methods (like QLoRA) on a single 80GB GPU comfortably. Once you need more GPUs for fine-tuning, you start to enter distributed training territory, where your model needs to be sharded across multiple GPUs, which adds a significant layer of complexity.

### Top open-weights models for fine-tuning

The variety and quality of open-weights base models has exploded in 2026, meaning that users who wish to fine-tune have more options than ever before.

When it comes to open-weights models, several model families stand out: [Gemma](https://deepmind.google/models/gemma/), [Nemotron](https://developer.nvidia.com/topics/ai/nemotron), and [GLiNER](https://github.com/urchade/GLiNER).

**Gemma (Google DeepMind)**

[Gemma](https://deepmind.google/models/gemma/) models are known for a high density of intelligence per parameter, offering several small models that outperform ones several times their size on reasoning and coding. The current release is [Gemma 4](https://ai.google.dev/gemma/docs/core) (April 2026), which spans five sizes from the tiny E2B up to a 31B dense model, all under the Apache 2.0 license. These models are multimodal, with a 256K context window, and cover over 140 languages. Users often fine-tune Gemma models for on-device chat and summarization tasks.

**Nemotron (NVIDIA)**

[Nemotron](https://developer.nvidia.com/topics/ai/nemotron) models are built for agents rather than chat. NVIDIA designed them as building blocks for multi-agent systems, with a focus on throughput and efficiency. The most recent release is [Nemotron 3](https://research.nvidia.com/labs/nemotron/Nemotron-3/) in June 2026, with three tiers: Nano (~30B), Super (~120B), and Ultra (~550B). While the first two models are open weights, [Nemotron Ultra](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/) is fully open source, released under the [OpenMDW-1.1 license](https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.1/LICENSE.OpenMDW-1.1). Nemotron models are often fine-tuned for tool-use agents, long-horizon planning, and throughput-sensitive production pipelines.

**GLiNER (Fastino Labs)**

[GLiNER](https://github.com/urchade/GLiNER) is an encoder-based family of models that are both small and highly specializable for specific tasks. [GLiNER2](https://huggingface.co/collections/fastino/gliner2-family) models are 0.3B parameters in size and capable of performing text classification and extraction, with fine-tuned variants like [GLiGuard](https://huggingface.co/collections/fastino/gliner2-family) and [GLiNER2-PII](https://huggingface.co/collections/fastino/gliner2-family) matching and outperforming much larger models. All models from the GLiNER family are released under the Apache 2.0 license.

For more information on model performance and benchmarks, you can head to [Artificial Analysis](https://artificialanalysis.ai/) and [Arena](https://arena.ai/leaderboard/).

## Curating a dataset for fine-tuning

Fine-tuning adjusts the model toward the patterns in your training data, so the quality and balance of that dataset largely determine the quality of the result.

The most effective fine-tuning data usually reflects the task you want the model to perform, so real examples drawn from your own systems, such as support tickets, past queries, or existing documents, tend to be more valuable than generic datasets used off the shelf. Where real data is limited, it can be supplemented, either by writing examples by hand or by generating synthetic ones with a larger model, though synthetic data is generally better treated as a starting point than as a finished product. In all cases, each example should resemble the inputs and outputs the model will encounter in production, since that is what it is learning to reproduce.

Here are a few tips for turning raw and synthetic data into a usable training set:

- **Prioritize quality over volume.** The model learns from whatever it is given, so a mislabeled or inconsistent example teaches the wrong pattern. A few hundred to a few thousand clean examples often beats a much larger noisy set.
- **Seed synthetic generation with real examples.** Using a small set of high-quality real samples as seed or few-shot prompts keeps generated data grounded in your task, rather than drifting toward the generating model's generic defaults.
- **Filter synthetic output aggressively.** Generated data needs review before it enters the set, whether through automated checks, a judge model, or spot inspection. The filtering step often matters more than the generation step.
- **Balance the dataset and cover the cases that matter.** A model learns the proportions of a dataset as well as its contents, so aim for even coverage across the situations you care about, including rare edge cases. Synthetic generation is useful here, since you can deliberately prompt for cases that are scarce in real data.

## Fine-tuning strategies

A range of techniques exists for adapting a language model's behavior to a specific task or domain, varying in both complexity and the resources they require.

### Full fine-tuning vs. parameter-efficient fine-tuning (PEFT)

Full fine-tuning updates every weight in the model, requiring memory for the full parameter set, gradients, and optimizer states at once. This can be an incredibly resource-hungry technique and is usually only recommended if you need your model to absorb a large amount of new knowledge, rather than just adapt its style or behavior.

![](https://framerusercontent.com/images/nPl414pJDjeKaPM6otVkUBXPK8.png?width=4800&height=2780)

For most use cases, parameter-efficient fine-tuning (PEFT) methods will suffice. PEFT methods freeze the base model and train a small set of added parameters instead, typically around 1% of the total, capturing most of the quality of a full fine-tune at a fraction of the cost. Two of the most common PEFT methods are LoRA and QLoRA.

[LoRA](https://arxiv.org/abs/2106.09685), which stands for Low-Rank Adaptation, injects small, trainable low-rank matrices into the model's layers instead of updating the original weights directly and is best used when you want efficient, high-quality adaptation on hardware that can already hold the model in memory, since it adds little overhead and lets you keep separate lightweight adapters for different tasks.

Quantized Low-Rank Adaptation, or [QLoRA](https://arxiv.org/abs/2305.14314), adds 4-bit quantization of the frozen base model on top of LoRA, bringing large-model fine-tuning within reach of a single consumer GPU.

### Supervised fine-tuning (SFT) vs. reinforcement learning (RL)

**Supervised fine-tuning (SFT)** trains the base model on labeled examples of the desired output. You provide input-output pairs, a prompt, and the response you want, and the model learns to imitate them by minimizing the difference between its output and the target. It is called supervised because each example carries the correct answer, so the model is shown directly what to produce. SFT is a stable, well-understood, and relatively inexpensive technique that can be used for fine-tuning both decoder models and encoder models.

**Reinforcement learning (RL)** trains the model on feedback about its outputs rather than on the outputs themselves. RL is a preference-based method aimed at shaping model behavior through reward signals instead of providing the model with the right answer during training, as in SFT. The earliest form of this, **reinforcement learning from human feedback (RLHF)**, trains a separate reward model on human preference comparisons and then optimizes against it, though the complexity and instability of that pipeline have made simpler alternatives more common. [**Direct preference optimization (DPO)**](https://arxiv.org/abs/2305.18290) is now the usual starting point, since it learns directly from pairs of preferred and rejected responses without a separate reward model, while [**group relative policy optimization (GRPO)**](https://arxiv.org/abs/2402.03300) has become the standard for reasoning tasks by scoring a group of sampled responses against one another, particularly where the reward can be verified automatically.

### Distillation vs. fine-tuning

Distillation is similar to fine-tuning in that it trains a model on input-output examples to shape its behavior, and in practice the student is often trained using supervised fine-tuning on the teacher's generated data. But it is ultimately distinct from fine-tuning because the training signal comes from another model rather than from human-written labels or ground-truth data, which makes distillation a way of sourcing the training data rather than a training method in its own right. In other words, the goal is transferring an existing model's capabilities into a smaller one, whereas fine-tuning more broadly is about adapting a model to a task regardless of where the target outputs come from.

## Evaluating a fine-tuned model

As LLMs become increasingly capable of more complex tasks, including advanced reasoning and agentic behavior, evaluating them becomes more challenging. The core goal of evals is to determine whether your fine-tuned model actually does what you need it to do in the real world and whether it does that task better than its base model. Determining this can be challenging.

Convenient measures like public benchmarks or off-the-shelf metrics are tempting to turn to because they're easy to run, but they capture broad or abstract qualities rather than performance on your specific task, which is the whole point of fine-tuning.

Following these principles can help make your evals more effective:

- **Start with error analysis.** Read a sample of model output, note where the system fails, and group those failures into categories. This is what tells you which evals are worth building in the first place, so it should come before any metric or tooling.
- **Write task-specific checks, not generic ones.** Derive your evals from the failures you actually observe rather than relying on abstract off-the-shelf metrics.
- **Prefer binary pass/fail over graded scores.** Simple yes/no judgments force clearer and more consistent decisions than 1-5 scales.
- **Start cheap, escalate only when needed.** Use code-based assertions or regex where a rule can catch the problem, and reserve heavier methods like an LLM-as-judge for the subjective failures simple rules can't capture.
- **Pair offline evals with production monitoring.** Offline evals tell you whether to ship, but they can't fully predict real-world behavior, so watch live traffic once the model is deployed.

## Summary

Fine-tuning open weights models gives you a smaller, cheaper, faster model that can match or beat a larger general-purpose one on your specific task, while keeping full control over your data and ownership of the resulting weights. And with new SOTA open weights model releases occurring on a near-weekly basis, users now have more high-quality base model options to choose from than ever before.

But fine-tuning an LLM to outperform large, generalist models isn't a simple task. It demands careful thought at every stage: base model selection, data curation, choosing the right fine-tuning strategy, and evaluation. If you’d like to manually fine-tune your own model, see the links below; otherwise, reach out to the Fastino Labs team for early access to our autonomous fine-tuning agent.

## Resources

- [NVIDIA Nemotron models](https://developer.nvidia.com/topics/ai/nemotron)
- [Google DeepMind Gemma models](https://deepmind.google/models/gemma/)
- [GLiNER2 model collection](https://huggingface.co/collections/fastino/gliner2-family)
- [LoRA paper](https://arxiv.org/abs/2106.09685)
- [QLoRA paper](https://arxiv.org/abs/2305.14314)
- [Fine-tune LLMs with Unsloth](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide)

![](https://framerusercontent.com/images/TavCQPrM1cT1tcw6B1k1hkekMyw.svg?width=1130&height=62)

Fastino Inc. (“Fastino”) develops specialized AI models and provides APIs designed to support structured data extraction, classification, reasoning, and production AI workflows. Fastino is a technology company and does not provide legal, financial, compliance, or advisory services.

Any outputs, predictions, classifications, or decisions generated through Fastino models are based on the configuration, data, and implementation provided by the customer. Fastino does not control, verify, or guarantee the accuracy, completeness, or suitability of model outputs for any specific purpose. By using this website or Fastino’s models and services, you acknowledge that all content and outputs are provided for informational and operational purposes only and agree to our Terms of Use and Privacy Policy.

---
- **Source:** Unknown
