---
title: 'There is no single "best" OCR approach. Every document extraction architecture is just a compromise between layout awareness, latency, and compute cost. Over the past year, I built an OCR… | Markus Kuehnle'
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# There is no single "best" OCR approach. 

Every document extraction architecture is just a compromise between layout awareness, latency, and compute cost.

Over the past year, I built an OCR… | Markus Kuehnle

There is no single "best" OCR approach. Every document extraction architecture is just a compromise between layout awareness, latency, and compute cost. Over the past year, I built an OCR application to reliably extract structured knowledge from medical documents, focusing on explainable, self-validating, and self-healing pipelines. Here is a breakdown of the 𝗰𝗼𝗿𝗲 𝗱𝗼𝗰𝘂𝗺𝗲𝗻𝘁 𝗲𝘅𝘁𝗿𝗮𝗰𝘁𝗶𝗼𝗻 𝘁𝗲𝗰𝗵𝗻𝗶𝗾𝘂𝗲𝘀 and where each fits in production: 𝟭. 𝗦𝘁𝗮𝘁𝗶𝗰 𝗕𝗼𝘂𝗻𝗱𝗶𝗻𝗴-𝗕𝗼𝘅 𝗖𝗿𝗼𝗽𝗽𝗶𝗻𝗴 Hardcodes pixel coordinates on standardized forms. • Tool: AWS Textract (Queries API) • Best for: Fixed government & tax forms (sub-millisecond speed, low cost). • Trade-off: Breaks under visual drift, scaling, or rotation. 𝟮. 𝗚𝗲𝗼𝗺𝗲𝘁𝗿𝗶𝗰 𝗔𝗻𝗰𝗵𝗼𝗿 𝗔𝗹𝗶𝗴𝗻𝗺𝗲𝗻𝘁 Uses keypoint detection (SIFT/ORB) to warp/rectify skewed scans onto a canonical grid before cropping. • Tool: OpenCV • Best for: Mobile photo scans with physical distortion. • Trade-off: Fails when layouts vary dynamically across vendors. 𝟯. 𝗧𝘄𝗼-𝗦𝘁𝗮𝗴𝗲 𝗗𝗲𝘁𝗲𝗰𝘁𝗶𝗼𝗻 + 𝗥𝗲𝗰𝗼𝗴𝗻𝗶𝘁𝗶𝗼𝗻 Runs object detection (bounding boxes) and text recognition in series. • Tool: PaddleOCR • Best for: Fast GPU parsing of flat documents, receipts, and signs. • Trade-off: Ignores global layout, flattening multi-column reading orders. 𝟰. 𝗠𝘂𝗹𝘁𝗶-𝗦𝘁𝗮𝗴𝗲 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁 𝗢𝗿𝗰𝗵𝗲𝘀𝘁𝗿𝗮𝘁𝗶𝗼𝗻 Combines layout detectors, table parsers, and OCR engines to extract spatial hierarchies into Markdown/JSON. • Tool: Docling • Best for: RAG pipelines converting complex PDFs and research papers. • Trade-off: Higher latency and heavier system dependencies. 𝟱. 𝗦𝗽𝗲𝗰𝗶𝗮𝗹𝗶𝘇𝗲𝗱 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁 𝗧𝗿𝗮𝗻𝘀𝗳𝗼𝗿𝗺𝗲𝗿𝘀 (𝗦𝗽𝗮𝘁𝗶𝗮𝗹 & 𝗩𝗶𝘀𝘂𝗮𝗹 𝗗𝗲𝗰𝗼𝗱𝗲𝗿𝘀) Uses layout-aware token classifiers or OCR-free vision decoders to parse complex document spaces. • Tools: LayoutLMv3 / Donut • Best for: Key-value extraction across variable invoices, math, or handwritten notes. • Trade-off: High GPU memory usage, annotation overhead, and hallucination risks. 𝟲. 𝗭𝗲𝗿𝗼-𝗦𝗵𝗼𝘁 𝗠𝘂𝗹𝘁𝗶𝗺𝗼𝗱𝗮𝗹 𝗩𝗟𝗠𝘀 Frontier vision-language models that parse and extract schemas directly via prompts. • Tool: Qwen2.5-VL • Best for: Unstructured, highly variable documents with zero prior training data. • Trade-off: High API costs, higher latency, and risk of numerical hallucinations. 𝟳. 𝗗𝘆𝗻𝗮𝗺𝗶𝗰 𝗠𝘂𝗹𝘁𝗶-𝗘𝗻𝗴𝗶𝗻𝗲 𝗥𝗼𝘂𝘁𝗶𝗻𝗴 Inspects page complexity to route simple text to fast CPU parsers and complex tables/handwriting to Vision-LLMs. • Tool: LlamaIndex Document Agents • Best for: Enterprise pipelines processing millions of mixed pages at scale. • Trade-off: High architectural complexity and schema normalization overhead. 💬 Which approach is are you mainly using in your extraction pipeline? ♻️ Repost to help someone in your network

---
- **Source:** Unknown
