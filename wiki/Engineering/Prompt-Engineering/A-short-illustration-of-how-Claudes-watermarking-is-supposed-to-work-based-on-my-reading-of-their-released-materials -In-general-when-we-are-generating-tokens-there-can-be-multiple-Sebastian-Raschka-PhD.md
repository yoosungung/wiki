---
title: "A short illustration of how Claude's watermarking is supposed to work (based on my reading of their released materials). 

In general, when we are generating tokens, there can be multiple… | Sebastian Raschka, PhD"
related_raw: ["[[raw/A short illustration of how Claude's watermarking is supposed to work (based on my reading of their released materials). 

In general, when we are generating tokens, there can be multiple… | Sebastian Raschka, PhD.md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# A short illustration of how Claude's watermarking is supposed to work (based on my reading of their released materials). 

In general, when we are generating tokens, there can be multiple… | Sebastian Raschka, PhD

A short illustration of how Claude's watermarking is supposed to work (based on my reading of their released materials). In general, when we are generating tokens, there can be multiple high-scoring tokens at certain next-word positions. Usually, we sample with top-k or top-p sampling so the highest-scoring token is most often selected (if we repeat the sampling many times), but other tokens may be selected as well. With watermarking, there is a key that says which of the (ideally equally) highest-scoring tokens to select. Or, more concretely, the secret key and previous token influence the randomness here. Now, if we repeat this at many token positions, this creates the watermark, as it will be a pattern that is statistically unlikely to get otherwise (due to combinatorics). One thing I am confused about: They basically say that they HAVE to do this for everyone due to EU regulation. Why? Sure, but this is an inference-time technique that doesn't require retraining or training a separate model, so if they wanted, they could only do that for EU users? 🤔

I'm still not sure how this works. First, even if this works - given a text - you will need the prompt that generated it to be able to tell if this was watermarked or not. The distributions depend on the prompt, which you don't have when trying to investigate a piece of text. Second, this does not seem deterministic. Especially for shorter texts, the statistical significance of this test will always be questionable. For longer texts, sure, they will have higher and higher confidence. But it will always remain a non-deterministic way to test.

The make-or-break detail with these schemes is that watermarking needs entropy to hide in. High-temperature prose gives you sampling freedom to bias toward the green-list tokens, but low-entropy outputs — code, math, short factual answers — leave little room to nudge tokens without hurting correctness, so the signal weakens exactly where provenance matters most. Do you know if Claude's approach degrades gracefully there, or just drops detectability? Paraphrasing robustness feels like the other open question.

---
- **Source:** Unknown
