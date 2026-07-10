import os
import re

# Mapping of filename to new path (relative to wiki/Agents/)
mapping = {
    # Memory-and-Cognition
    "Claude-Mem 지속적인 메모리 압축 시스템.md": "Memory-and-Cognition/Claude-Mem 지속적인 메모리 압축 시스템.md",
    "Cognee - AI Memory System.md": "Memory-and-Cognition/Cognee - AI Memory System.md",
    "Cognee 빠른 시작.md": "Memory-and-Cognition/Cognee 빠른 시작.md",
    "Cognee 설치.md": "Memory-and-Cognition/Cognee 설치.md",
    "Cognee 핵심 개념.md": "Memory-and-Cognition/Cognee 핵심 개념.md",
    "Cognee.md": "Memory-and-Cognition/Cognee.md",
    "Hierarchical-Memory-for-LLMs-계층적-메모리-구조.md": "Memory-and-Cognition/Hierarchical-Memory-for-LLMs-계층적-메모리-구조.md",
    "LangMem.md": "Memory-and-Cognition/LangMem.md",
    "Mem-Palace-Cognee-Update-2026-04-09.md": "Memory-and-Cognition/Mem-Palace-Cognee-Update-2026-04-09.md",
    "Mem0-vs-Cognee-Comparison-2026.md": "Memory-and-Cognition/Mem0-vs-Cognee-Comparison-2026.md",
    "Mem0-vs-Cognee-vs-QMD-Comparison.md": "Memory-and-Cognition/Mem0-vs-Cognee-vs-QMD-Comparison.md",
    "Mem0.md": "Memory-and-Cognition/Mem0.md",
    "Memory.md": "Memory-and-Cognition/Memory.md",
    "OpenMemory.md": "Memory-and-Cognition/OpenMemory.md",

    # Text-to-SQL
    "000_T2SQL-MOC.md": "Text-to-SQL/000_T2SQL-MOC.md",
    "2026-04-09-sLM-T2SQL-Trends.md": "Text-to-SQL/2026-04-09-sLM-T2SQL-Trends.md",
    "2026-04-09-ThoughtSpot-Spotter.md": "Text-to-SQL/2026-04-09-ThoughtSpot-Spotter.md",
    "Agentic-Semantic-Layer-ThoughtSpot-Spotter-Semantics-비즈니스-컨텍스트-레이어.md": "Text-to-SQL/Agentic-Semantic-Layer-ThoughtSpot-Spotter-Semantics-비즈니스-컨텍스트-레이어.md",
    "Arctic-Text2SQL-R1-Reinforcement-Learning.md": "Text-to-SQL/Arctic-Text2SQL-R1-Reinforcement-Learning.md",
    "AV-SQL-Agentic-Views-Spider-2-0.md": "Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md",
    "BIRD-Critic-SQLite-Talon-Models.md": "Text-to-SQL/BIRD-Critic-SQLite-Talon-Models.md",
    "BIRD-Interact-ICLR-2026.md": "Text-to-SQL/BIRD-Interact-ICLR-2026.md",
    "DBHub_MCP_Server.md": "Text-to-SQL/DBHub_MCP_Server.md",
    "PremSQL-Update-2026-04-09.md": "Text-to-SQL/PremSQL-Update-2026-04-09.md",
    "Qwen2.5-Coder-T2SQL-Benchmark-Performance-오픈소스-SQL-모델-성능-분석.md": "Text-to-SQL/Qwen2.5-Coder-T2SQL-Benchmark-Performance-오픈소스-SQL-모델-성능-분석.md",
    "ReViSQL-BIRD-Human-Parity-2026.md": "Text-to-SQL/ReViSQL-BIRD-Human-Parity-2026.md",
    "SLM-SQL-IJCNLP-2026.md": "Text-to-SQL/SLM-SQL-IJCNLP-2026.md",
    "sLM-Text-to-SQL-MATS-Schema-Linking-2026.md": "Text-to-SQL/sLM-Text-to-SQL-MATS-Schema-Linking-2026.md",
    "Snowflake-Arctic-Text2SQL-R1.md": "Text-to-SQL/Snowflake-Arctic-Text2SQL-R1.md",
    "Spider-2.0-Benchmark-엔터프라이즈-SQL-워크플로우-평가.md": "Text-to-SQL/Spider-2.0-Benchmark-엔터프라이즈-SQL-워크플로우-평가.md",
    "Text-to-SQL-Reasoning-2026.md": "Text-to-SQL/Text-to-SQL-Reasoning-2026.md",
    "ThoughtSpot_Spotter_Semantics.md": "Text-to-SQL/ThoughtSpot_Spotter_Semantics.md",
    "ThoughtSpot-Spotter-Semantics-Agentic-Layer-Release.md": "Text-to-SQL/ThoughtSpot-Spotter-Semantics-Agentic-Layer-Release.md",
    "ThoughtSpot-Spotter-Semantics-Agentic-Layer.md": "Text-to-SQL/ThoughtSpot-Spotter-Semantics-Agentic-Layer.md",
    "ThoughtSpot-Spotter-Semantics-Instance-Upgrade-2026.md": "Text-to-SQL/ThoughtSpot-Spotter-Semantics-Instance-Upgrade-2026.md",
    "ThoughtSpot-Spotter-Semantics-Update-2026-04-09.md": "Text-to-SQL/ThoughtSpot-Spotter-Semantics-Update-2026-04-09.md",
    "ThoughtSpot-Spotter-Semantics-에이전틱-시맨틱-레이어.md": "Text-to-SQL/ThoughtSpot-Spotter-Semantics-에이전틱-시맨틱-레이어.md",
    "ThoughtSpot-Spotter-Semantics.md": "Text-to-SQL/ThoughtSpot-Spotter-Semantics.md",
    "ThoughtSpot-Spotter-Spider-2.0.md": "Text-to-SQL/ThoughtSpot-Spotter-Spider-2.0.md",

    # Robotics-and-VLA
    "2026-04-09-VLA-Robotics.md": "Robotics-and-VLA/2026-04-09-VLA-Robotics.md",
    "E-VLA-Efficient-Vision-Language-Action.md": "Robotics-and-VLA/E-VLA-Efficient-Vision-Language-Action.md",
    "Figure-03-Helix-VLA-Stack.md": "Robotics-and-VLA/Figure-03-Helix-VLA-Stack.md",
    "Figure-PI-VLA-Update-2026-04-09.md": "Robotics-and-VLA/Figure-PI-VLA-Update-2026-04-09.md",
    "Gemma4-Edge-Robotics-Nvidia-Cosmos-3-GR00T.md": "Robotics-and-VLA/Gemma4-Edge-Robotics-Nvidia-Cosmos-3-GR00T.md",
    "Google-RT-3-Open-Source-Robotics.md": "Robotics-and-VLA/Google-RT-3-Open-Source-Robotics.md",
    "NVIDIA_Physical_AI.md": "Robotics-and-VLA/NVIDIA_Physical_AI.md",
    "Nvidia-Cosmos-VLA-2026.md": "Robotics-and-VLA/Nvidia-Cosmos-VLA-2026.md",
    "NVIDIA-GTC-2026-Physical-AI.md": "Robotics-and-VLA/NVIDIA-GTC-2026-Physical-AI.md",
    "NVIDIA-Physical-AI-GR00T-Cosmos-물리적-AI-혁신.md": "Robotics-and-VLA/NVIDIA-Physical-AI-GR00T-Cosmos-물리적-AI-혁신.md",
    "Physical-Intelligence-pi0-Foundation-Model.md": "Robotics-and-VLA/Physical-Intelligence-pi0-Foundation-Model.md",
    "RoboMonkey.md": "Robotics-and-VLA/RoboMonkey.md",
    "Robotics-NVIDIA-Physical-AI-Google-SIMA2.md": "Robotics-and-VLA/Robotics-NVIDIA-Physical-AI-Google-SIMA2.md",
    "ROS2.md": "Robotics-and-VLA/ROS2.md",
    "VLA-Adapter - Effective Paradigm for Tiny-Scale VLA Models.md": "Robotics-and-VLA/VLA-Adapter - Effective Paradigm for Tiny-Scale VLA Models.md",
    "VLAb-VLA-pretraining.md": "Robotics-and-VLA/VLAb-VLA-pretraining.md",
    "VTLA-CraftNet-Tactile-Robotics.md": "Robotics-and-VLA/VTLA-CraftNet-Tactile-Robotics.md",
    "Why VLAs are becoming the real link between AI reasoning and physical robotics.md": "Robotics-and-VLA/Why VLAs are becoming the real link between AI reasoning and physical robotics.md",
    "X-Square-Robot-WALL-A-VLA-Model.md": "Robotics-and-VLA/X-Square-Robot-WALL-A-VLA-Model.md",

    # Coding-and-Engineering
    "Anthropic의 코딩 AI 에이전트, 치명적인 사이버 공격에 직면.md": "Coding-and-Engineering/Anthropic의 코딩 AI 에이전트, 치명적인 사이버 공격에 직면.md",
    "Claude Code의 Task 변화와 AI-native 엔지니어의 조건.md": "Coding-and-Engineering/Claude Code의 Task 변화와 AI-native 엔지니어의 조건.md",
    "Claude_Code_on_the_web.md": "Coding-and-Engineering/Claude_Code_on_the_web.md",
    "Claude-Code-Agentic-CLI-Update.md": "Coding-and-Engineering/Claude-Code-Agentic-CLI-Update.md",
    "Confucius Code Agent - 모델 스케일링의 종말과 에이전트 설계의 중요성.md": "Coding-and-Engineering/Confucius Code Agent - 모델 스케일링의 종말과 에이전트 설계의 중요성.md",
    "fastcampus-ai-agent-vibecoding.md": "Coding-and-Engineering/fastcampus-ai-agent-vibecoding.md",
    "langchain-code.md": "Coding-and-Engineering/langchain-code.md",

    # Multi-Agent-and-Orchestration
    "Compound-AI-Systems-Architecture.md": "Multi-Agent-and-Orchestration/Compound-AI-Systems-Architecture.md",
    "LangAlpha 다중 에이전트 AI 주식 분석 도구.md": "Multi-Agent-and-Orchestration/LangAlpha 다중 에이전트 AI 주식 분석 도구.md",
    "Langchain_다중_에이전트_아키텍처_선택.md": "Multi-Agent-and-Orchestration/Langchain_다중_에이전트_아키텍처_선택.md",
    "LangGraph-Deep-Agents-Update-2026-04-09.md": "Multi-Agent-and-Orchestration/LangGraph-Deep-Agents-Update-2026-04-09.md",
    "LatentMAS.md": "Multi-Agent-and-Orchestration/LatentMAS.md",
    "Multi-Agent Consensus Alignment.md": "Multi-Agent-and-Orchestration/Multi-Agent Consensus Alignment.md",
    "Multi-Agent Systems - Collaboration, Complexity, and Innovation.md": "Multi-Agent-and-Orchestration/Multi-Agent Systems - Collaboration, Complexity, and Innovation.md",
    "Multi-Agent-Orchestration-Patterns-2026.md": "Multi-Agent-and-Orchestration/Multi-Agent-Orchestration-Patterns-2026.md",
    "NVIDIA-ToolOrchestra.md": "Multi-Agent-and-Orchestration/NVIDIA-ToolOrchestra.md",
    "멀티-에이전트-패턴.md": "Multi-Agent-and-Orchestration/멀티-에이전트-패턴.md",
    "하이브-마인드와-강화학습.md": "Multi-Agent-and-Orchestration/하이브-마인드와-강화학습.md",

    # Implementation
    "Agent-Lightning.md": "Implementation/Agent-Lightning.md",
    "Agent0.md": "Implementation/Agent0.md",
    "Agentor.md": "Implementation/Agentor.md",
    "Airweave.md": "Implementation/Airweave.md",
    "building-agentic-payments-with-langchain-and-privy.md": "Implementation/building-agentic-payments-with-langchain-and-privy.md",
    "Deep-Agents-Runtime-LangChain-에이전트-실행-환경.md": "Implementation/Deep-Agents-Runtime-LangChain-에이전트-실행-환경.md",
    "DeepAgents를 위한 샌드박스.md": "Implementation/DeepAgents를 위한 샌드박스.md",
    "DeepAgent를 위한 샌드박스 사용.md": "Implementation/DeepAgent를 위한 샌드박스 사용.md",
    "DS-STAR) A State-of-the-Art Versatile Data Science Agent.md": "Implementation/DS-STAR) A State-of-the-Art Versatile Data Science Agent.md",
    "Enterprise-Voice-AI-System.md": "Implementation/Enterprise-Voice-AI-System.md",
    "IBM_CUGA.md": "Implementation/IBM_CUGA.md",
    "LangSmith-No-Code-Agent-Builder.md": "Implementation/LangSmith-No-Code-Agent-Builder.md",
    "LiteLLM Gateway - Vertex AI Agent Engine 지원.md": "Implementation/LiteLLM Gateway - Vertex AI Agent Engine 지원.md",
    "Manus_1.5_release.md": "Implementation/Manus_1.5_release.md",
    "MaxKB.md": "Implementation/MaxKB.md",
    "Microsoft Agent-Lightning.md": "Implementation/Microsoft Agent-Lightning.md",
    "my-adk-python-samples.md": "Implementation/my-adk-python-samples.md",
    "Open Notebook.md": "Implementation/Open Notebook.md",
    "open-agent-builder.md": "Implementation/open-agent-builder.md",
    "Programmatic-Tool-Calling-Agent.md": "Implementation/Programmatic-Tool-Calling-Agent.md",
    "RunAgent.md": "Implementation/RunAgent.md",
    "Skyvern.md": "Implementation/Skyvern.md",
    "Strands Agents와 Amazon S3 Vectors를 사용한 RAG 시스템 구축 가이드.md": "Implementation/Strands Agents와 Amazon S3 Vectors를 사용한 RAG 시스템 구축 가이드.md",
    "TrendRadar.md": "Implementation/TrendRadar.md",

    # Self-Evolving
    "AlphaEvolve on Google Cloud.md": "Self-Evolving/AlphaEvolve on Google Cloud.md",
    "Hyperagents-Self-Evolving-AI.md": "Self-Evolving/Hyperagents-Self-Evolving-AI.md",
    "Misevolution-Risk-and-Self-Evolving-Agents.md": "Self-Evolving/Misevolution-Risk-and-Self-Evolving-Agents.md",
    "OpenSpace-Self-Evolving-Agents.md": "Self-Evolving/OpenSpace-Self-Evolving-Agents.md",
    "Self-Evolving-Agents-Autonomous-Tools-2026.md": "Self-Evolving/Self-Evolving-Agents-Autonomous-Tools-2026.md",
    "Self-evolving-Agents-DGM-O-mega-자가-진화형-에이전트-모델.md": "Self-Evolving/Self-evolving-Agents-DGM-O-mega-자가-진화형-에이전트-모델.md",
    "Self-Evolving-Agents-NVIDIA.md": "Self-Evolving/Self-Evolving-Agents-NVIDIA.md",
}

# Add entries for without .md extension as well (Obsidian often links without .md)
mapping_no_ext = {}
for k, v in mapping.items():
    if k.endswith(".md"):
        mapping_no_ext[k[:-3]] = v[:-3]

all_mapping = {**mapping, **mapping_no_ext}

wiki_root = "wiki"

def update_links(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    # Update [[wiki/Agents/Filename]] or [[Agents/Filename]]
    for old_name, new_rel_path in all_mapping.items():
        # Handle [[wiki/Agents/Name]]
        pattern1 = r"\[\[wiki/Agents/" + re.escape(old_name) + r"(\|.*?)?\]\]"
        replacement1 = r"[[wiki/Agents/" + new_rel_path + r"\1]]"
        new_content = re.sub(pattern1, replacement1, content)
        if new_content != content:
            content = new_content
            changed = True
            
        # Handle [[Agents/Name]]
        pattern2 = r"\[\[Agents/" + re.escape(old_name) + r"(\|.*?)?\]\]"
        replacement2 = r"[[Agents/" + new_rel_path + r"\1]]"
        new_content = re.sub(pattern2, replacement2, content)
        if new_content != content:
            content = new_content
            changed = True

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

count = 0
for root, dirs, files in os.walk(wiki_root):
    for file in files:
        if file.endswith(".md"):
            if update_links(os.path.join(root, file)):
                count += 1

print(f"Updated links in {count} files.")
