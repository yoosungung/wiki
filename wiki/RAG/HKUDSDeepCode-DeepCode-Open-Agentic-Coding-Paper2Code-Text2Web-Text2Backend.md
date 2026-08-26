---
title: 'HKUDSDeepCode "DeepCode Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)"'
related_raw: ['[[raw/HKUDSDeepCode "DeepCode Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)".md]]']
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# HKUDSDeepCode "DeepCode Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)"

```
██████╗ ███████╗███████╗██████╗  ██████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║  ██║█████╗  █████╗  ██████╔╝██║     ██║   ██║██║  ██║█████╗
██║  ██║██╔══╝  ██╔══╝  ██╔═══╝ ██║     ██║   ██║██║  ██║██╔══╝
██████╔╝███████╗███████╗██║     ╚██████╗╚██████╔╝██████╔╝███████╗
╚═════╝ ╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
```

[![HKUDS%2FDeepCode | Trendshift](https://camo.githubusercontent.com/05ab13ac44ac770b1b3ab525469fe37d12f2cbad08a8305ba06966cd623eea92/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3134363635)](https://trendshift.io/repositories/14665?utm_source=repository-badge&utm_medium=badge&utm_campaign=badge-repository-14665)## DeepCode: Open Agentic Coding

### Advancing Code Generation with Multi-Agent Systems

[![](https://camo.githubusercontent.com/a9c39fb9099ef6e3819d3397f6967809a9019d620921e5e0104dbd2c1f5c1b40/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f484b5544532f44656570436f64653f636f6c6f723d303064396666267374796c653d666f722d7468652d6261646765266c6f676f3d73746172266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://github.com/HKUDS/DeepCode/stargazers) [![](https://camo.githubusercontent.com/cdf5bd9aca7daa1af839230129b7e31e1a73fa357d37b15795d414148e21f331/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617065722d61725869762d6f72616e67653f7374796c653d666f722d7468652d6261646765266c6f676f3d6172786976266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://arxiv.org/abs/2512.07921) [![](https://camo.githubusercontent.com/e11d4a76523eca84a3cd40f1cbad2cc2c71e753df08c6464d0bfc162ca2398ba/68747470733a2f2f696d672e736869656c64732e696f2f62616467652ff09f908d507974686f6e2d332e31322532422d3465636463343f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://camo.githubusercontent.com/e11d4a76523eca84a3cd40f1cbad2cc2c71e753df08c6464d0bfc162ca2398ba/68747470733a2f2f696d672e736869656c64732e696f2f62616467652ff09f908d507974686f6e2d332e31322532422d3465636463343f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)

[![Feishu](https://camo.githubusercontent.com/bd35c9ed9293c731eb7291729ccf72034a9f1fe9f840d4d8668e84cd4333010e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4665697368752d47726f75702d4539444246433f7374796c653d666c6174266c6f676f3d666569736875266c6f676f436f6c6f723d7768697465)](https://github.com/HKUDS/.github/blob/main/profile/README.md) [![WeChat](https://camo.githubusercontent.com/08ab611a06d7426a0b4d1c949dfe5acc00edc85da0e5ecb242c7ce2a9652d1a8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5765436861742d47726f75702d4335454142343f7374796c653d666c6174266c6f676f3d776563686174266c6f676f436f6c6f723d7768697465)](https://github.com/HKUDS/.github/blob/main/profile/README.md)

[![](https://camo.githubusercontent.com/5dc13c91fe6858f8373b0aa709fc6505f1716ffc1c7e35050fcdccd6971376f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f517569636b25323053746172742d476574253230537461727465642532304e6f772d3030643966663f7374796c653d666f722d7468652d6261646765266c6f676f3d726f636b6574266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](#quick-start)

 [![English](https://camo.githubusercontent.com/1112ae8c0d90e7dd57a65eb7fe7c95d04494d08db022976e1d362818df30cb5d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f456e676c6973682d3030643466663f7374796c653d666f722d7468652d6261646765266c6f676f3d726561646d65266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://github.com/HKUDS/DeepCode/blob/main/README.md)[![中文](https://camo.githubusercontent.com/deb181a4692339e3ae9dd6ba1822cef4c33e056f0e0a0c27c350fa45b0739257/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe4b8ade696872d3030643466663f7374796c653d666f722d7468652d6261646765266c6f676f3d726561646d65266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d316131613265)](https://github.com/HKUDS/DeepCode/blob/main/README_ZH.md)

### 🖥️ Interface Showcase

#### 🖥️ DeepCode Desktop

[![DeepCode Desktop coding agent demo](https://github.com/Zongwei9888/Experiment_Images/raw/e389750e733ec2c1b94986cb990036899dcaec52/DeepCode_images/Area.gif)](https://github.com/Zongwei9888/Experiment_Images/raw/e389750e733ec2c1b94986cb990036899dcaec52/DeepCode_images/Area.gif)

*Work with DeepCode in a visual workspace for Sessions, goals, tool activity, code changes, and verification.*

DeepCode has one Agent runtime and two interfaces: an interactive CLI for terminal workflows and a Tauri Desktop workbench for visual Sessions, review, and settings. Both open the same local Projects, Session history, models, Skills, permissions, Goals, and Automations. See the [`Desktop source guide`](https://github.com/HKUDS/DeepCode/blob/main/desktop/README.md) to run the application locally.

---

### 🎬 Introduction Video

[![DeepCode Introduction Video](https://camo.githubusercontent.com/5457b62f9acc76200ee09452c81dd2211bfbda322648c94388a506116221a124/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f5052676d5038704f4930382f6d617872657364656661756c742e6a7067)](https://youtu.be/PRgmP8pOI08)

*🎯 **Watch our complete introduction** - See how DeepCode transforms research papers and natural language into production-ready code*

[![Watch Video](https://camo.githubusercontent.com/e979c84415566f535a9222d3bde5d5103b7857a58a2d7b646d27903469dc3696/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe296b6efb88f5f57617463685f566964656f2d4646303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d796f7574756265266c6f676f436f6c6f723d7768697465)](https://youtu.be/PRgmP8pOI08)

---

> *"Where AI Agents Transform Ideas into Production-Ready Code"*

---

## 📑 Table of Contents

[![A verified task completed with DeepCode](https://github.com/HKUDS/DeepCode/raw/main/assets/readme/deepcode-overview.png)](https://github.com/HKUDS/DeepCode/blob/main/assets/readme/deepcode-overview.png)

## News

**2026-08-09 · Skills now have a real runtime contract**

- **Load guidance through one provider boundary.** Skill discovery, content reads, and package search now stay with the provider that owns the Skill, while the catalog remains metadata-only. Local Skills keep their existing precedence and identity, and future providers no longer need filesystem shortcuts to fit the runtime.
- **Compose Skills without hiding missing capabilities.** Skills can declare tool and Skill dependencies; DeepCode expands them in order, detects cycles, and fails before the first model request when a requirement is unavailable.
- **Reveal only what the task needs.** The Agent can search and read bounded package resources progressively, with revision, traversal, symlink, and size checks applied at the shared provider contract.
- **Keep execution constrained and auditable.** A Skill can narrow the tools already allowed by the Session but cannot grant new permissions. CLI, TUI, and Desktop share the same immutable Turn snapshot and persist only Skill identity, invocation kind, and revision—not the instruction body.

**2026-08-07 · Thinking controls, more providers, and a Desktop you can tune**

- **Reasoning controls work again across the board.** Thinking levels are now resolved from the model catalog, so Claude, GPT-5, Kimi, Qwen and Grok all offer their real effort levels, and DeepSeek, GLM and MiniMax get a working thinking toggle. A newly released model inherits its family's controls instead of silently losing them.
- **Three more providers.** Requesty and Forge join as gateways, and MiniMax arrives with its own catalog entry — including the 1M-context M3 tier.
- **Make the Desktop yours.** Settings → Appearance adds conversation width, a light/dark override that no longer follows the OS blindly, font size, and font selection filtered to what is actually installed on your machine.
- **Safer command execution on Windows.** A Job Object backend gives the sandbox real process-tree isolation where previously there was none.

**2026-08-04 · Skills that work wherever you do**

- **Keep reusable expertise close to your work.** DeepCode discovers Skills from the current project as well as your personal collection, while keeping existing DeepCode and Claude-compatible Skill locations working.
- **Use the same Skill from CLI or Desktop.** Select it for a task and DeepCode carries its identity and version with the Turn, so the Session shows which guidance shaped the result.
- **Create Skills without leaving DeepCode.** The built-in Skill Creator helps you scaffold and validate focused, reusable workflows from either interface.
- **Stay focused as your library grows.** Context-aware discovery keeps the Agent prompt concise while the complete Skill catalog remains available to browse and manage.

**2026-08-03 · 🎉 DeepCode v2.0 is here**

DeepCode v2.0 introduces a new general-purpose Coding Agent framework for building, fixing, understanding, and improving real software projects.

- **Take on real repository work.** DeepCode can explore a codebase, edit files, run commands and tests, review changes, and carry a task through to a working result.
- **Keep complex goals moving with Loop Engineering.** Give DeepCode a goal and it can continue through understanding, implementation, verification, and repair instead of stopping after one plausible answer.
- **Stay in control while the Agent works.** Add requirements, correct its direction, switch models, stop, resume, or revise the goal without throwing away the work already completed.
- **See what you are getting.** Plans, tool activity, code changes, test results, and verification evidence stay visible so the result is easier to review and trust.
- **Build Automations around the way you work.** Turn any natural-language instruction into a project-specific task: run it on demand or on a recurring interval, then edit, pause, resume, and review every result. Use it for the work you want DeepCode to keep taking care of, from regression checks and test repair to documentation upkeep and repository maintenance.
- **Work your way.** Use Desktop or CLI, bring your own models and Skills, and delegate focused work without changing the underlying Agent workflow.

DeepCode v2.0 is built to help you spend less time supervising every step and more time shipping software you are proud of. We cannot wait to see what you build! 🚀

**Earlier 2026 milestones**
- **2026-07-31 · One execution model across CLI and Desktop.** Interactive, headless, Goal, Automation, and Desktop work share the same durable Project, Session, Thread, and Turn lifecycle. Workspace trust stays independent from the Session access preset, and reasoning controls remain model-aware.
- **2026-07-21 · Durable Goals and safe Session lifecycle.** Long-running Goals are resumable across CLI and Desktop, while guarded archival and deletion preserve repository files and recover safely after interruption.
- **2026-07-20 · Session-level model control and shared Skills.** Named LLM connections and future-Turn model switches preserve conversation history; project and user Skills are shared across entry points.
- **2026-07-17 · Durable Session navigation and replay.** Projects organize collapsible Session history, long conversations replay incrementally, and approvals, reviews, tests, and Artifacts remain attached to their task.
- **2026-07-10 · Loop Engineering and parallel agents.** Mutable Goals can inspect, implement, verify, and repair across steerable Turns, while focused work can be delegated in isolated worktrees with explicit conflict handling.
- **2026-07-08 · Durable Sessions and memory.** Session history survives restarts, project instructions can live in `AGENTS.md` or `DEEPCODE.md`, and persistent notes remain with the workspace.
- **2026-07-08 · General coding agent.** The free-form TUI, native file and shell tools, headless execution, context compaction, and cross-directory resume established the current product foundation.
- **2026-07-04 · Agent Harness foundation.** A shared execution contract, three-valued permissions, sensitive-path protection, platform sandboxing, and normalized events made supervised local execution possible.
- The complete pre-restructure history is preserved in the [legacy README](https://github.com/HKUDS/DeepCode/blob/main/docs/archive/README_LEGACY_2026-07-20.md).

## What Deep means in DeepCode

Most Coding Agents can generate code. The hard part is understanding a real project, making changes within the right boundaries, continuously correcting course from runtime results, and making it clear why the outcome can be trusted.

DeepCode is an open-source Coding Agent for real software engineering. Give it a simple change or a goal that takes dozens of steps. It can understand the project, work on the code, run tools, verify results, and continue after an interruption, restart, or model switch.

“Deep” represents four kinds of depth that remain with the task from start to finish:

| Depth | What it means for you |
| --- | --- |
| **Deep Context** | Understand the task through project structure, engineering rules, Skills, Session history, and long-term memory. |
| **Deep Execution** | Search, edit, run commands, and execute tests instead of stopping at suggestions—and show the work as it happens. |
| **Deep Verification** | Check results with tests, builds, diagnostics, Diffs, and task Artifacts rather than treating a plausible answer as done. |
| **Deep Continuity** | Preserve conversations, decisions, tool records, and evidence across time, directories, clients, and model changes. |

DeepCode stands out in three ways:

- **Turn complex knowledge into a working system.** DeepCode is not limited to Issues and code snippets. Paper2Code can start from papers, documents, reference repositories, and experiment goals, then carry the work through understanding, implementation, and verification.
- **Keep long tasks moving while staying in control.** A Goal is not a one-shot prompt. Add requirements, revise the Goal, pause, stop, or continue while the task is running without losing completed work.
- **Take code changes through verification and review.** DeepCode goes beyond generating a patch. It runs the commands and tests the task requires, inspects build results and file changes, and links the Goal outcome to relevant execution records for review.

DeepCode is not designed to make an Agent look busier. It is designed to help you finish real software engineering work more reliably.

## Core capabilities

DeepCode provides a complete local Coding Agent workflow. CLI and Desktop are two ways to use the same Agent, Sessions, models, Skills, permissions, and task state.

[![DeepCode Agent Harness and verification loop](https://github.com/HKUDS/DeepCode/raw/main/assets/readme/verification-loop.png)](https://github.com/HKUDS/DeepCode/blob/main/assets/readme/verification-loop.png)

### Work directly in your repository

DeepCode can read and search code, edit files, apply patches, run commands and tests, and continue working from the results. Tool calls, execution progress, and file changes stay visible, so you can see what the Agent did and what changed in the project.

Use it to explain code, fix bugs, and add tests—or for cross-file refactors, feature development, and longer repository-level tasks.

When you provide a public HTTP or HTTPS URL, the shared `web_fetch` tool can read the page without a search provider or an additional API key.

### Goal-driven Loop Engineering

For work that cannot be completed in one response, give DeepCode a natural- language Goal. The Agent keeps analyzing, implementing, verifying, and fixing around that Goal without requiring you to push every step manually.

While it runs, you can still:

- add information to the current task;
- revise the Goal or its acceptance criteria;
- queue the next instruction;
- pause, stop, or continue the task;
- resume the same Goal after leaving the application.

Automatic execution does not take away your control. You can always change what should happen next.

### Evidence-driven completion

DeepCode does not use one hard-coded rule to judge every Coding task. It selects evidence that fits the task, such as test results, build output, static checks, diagnostics, file changes, Diffs, or generated Artifacts.

A failed verification is not presented as success. It becomes input to the next repair. When a task is complete—or genuinely blocked—the result, reason, and related evidence remain in the Session for review and reproduction.

### Durable Sessions and project context

Every Session is stored locally and linked to its original project. Start DeepCode from any directory, find earlier projects and Sessions, and continue the same work in CLI or Desktop.

A Session stores more than chat text: it keeps tool calls, permission decisions, Goals, model configuration, and verification records. Project rules, persistent memory, Skills, and long-conversation compaction help the Agent keep context throughout complex work.

### Your models, your reasoning settings

DeepCode is not tied to one model provider. Connect OpenRouter, OpenAI, Anthropic, DeepSeek, Gemini, an OpenAI-compatible gateway, Ollama, vLLM, or another compatible endpoint with your own API Key.

Before use, a connection can check credentials, the model catalog, and a real inference request. Each Session can choose a model and Thinking Level. Changing models mid-Session affects future Turns only; it does not delete history or confuse where earlier work came from. When supported, DeepCode can also show a reasoning summary returned by the Provider.

### Reusable Skills

Skills turn team conventions, domain knowledge, review methods, and repeated workflows into reusable Agent capabilities. Keep project Skills in `.agents/skills`, keep personal Skills in `~/.agents/skills`, or use the bundled Skill Creator to build one conversationally.

DeepCode also reads existing `.deepcode/skills` and Claude-style directories without migrating them. A Skill can guide how the Agent works, but it cannot bypass project trust, tool permissions, or safety boundaries.

### Permissions you can understand

Every project must be explicitly trusted before execution. Each Session can use one of three modes:

- **Ask**: confirm sensitive operations before they run;
- **Read only**: allow analysis and reading only;
- **Full access**: allow complete work in a trusted project.

Individual tools also support `allow`, `ask`, and `deny`. CLI and Desktop share the same permission state, and DeepCode does not silently replay operations with side effects after a task is stopped or interrupted.

### Parallel agents without file collisions

Complex work can be split across focused Agents—for example, separate Agents for code investigation, test analysis, and implementation review.

Parallel changes can run in isolated Git worktrees so Agents do not edit the same working directory at once. Results return to the main task for review and integration. Conflicts are shown explicitly instead of being silently overwritten, and the main Agent remains responsible for the final Goal.

### Automate repeatable engineering work

Once a workflow is stable, save it as an Automation and run it manually or on a schedule. For example:

- check tests and builds regularly;
- scan for regressions;
- organize pending work;
- run repository maintenance or periodic reviews.

Automation does not launch a separate, reduced Agent. It uses the same Sessions, models, Skills, permissions, approvals, and recovery behavior, and keeps the history of every run.

### Paper2Code

Paper2Code was DeepCode's original research direction and remains its dedicated workflow for research reproduction.

It can start from a paper, technical document, URL, or reference repository; understand the research goal; find related implementations; organize a development plan; generate code; and verify the result through experiments and Artifacts. It reflects DeepCode's core idea: the goal is not to generate code that merely looks correct, but to turn complex knowledge into a system that can run, be inspected, and keep improving.

## Quick start

DeepCode has two interfaces with separate installation paths. Choose one to get started; both use the same Agent runtime and canonical Session history.

> `uv tool install --python 3.12 deepcode-hku` installs the CLI and shared Python runtime. It does **not** install the Tauri Desktop application.

### Option A — Install the CLI

Install `uv` first if it is not already available. On Windows PowerShell:

```
winget install --id astral-sh.uv --exact
```

Open a new terminal after the first `uv` installation, then run:

```
uv tool install --python 3.12 deepcode-hku
deepcode init
```

The explicit Python selection is intentional: DeepCode requires Python 3.12+ and must not fall back to an unsupported legacy package on an older interpreter. If an existing uv tool environment still contains DeepCode 1.x, migrate it with `uv tool upgrade --python 3.12 deepcode-hku`.

Create a model connection once. `--api-key` opens a non-echoing prompt:

```
deepcode provider set personal-openrouter --template openrouter --label "OpenRouter · Personal" --api-key
deepcode provider models personal-openrouter --refresh
deepcode provider test personal-openrouter --model <model-id>
```

Enter the repository you want DeepCode to work in and start the interactive Agent:

```
cd <your-project>
deepcode
```

`deepcode init` creates minimal user configuration under `~/.deepcode/`. Credentials are stored separately in user-private storage and are never written to Session history. `pipx install deepcode-hku` and `pip install deepcode-hku` are also supported in an appropriate Python 3.12+ environment.

### Option B — Install Desktop

Desktop release bundles are distributed separately from the Python package. Check [GitHub Releases](https://github.com/HKUDS/DeepCode/releases) for a signed installer for your platform. If no installer is attached, use the source setup below.

#### macOS and Linux from source

Install the platform dependencies from the [Tauri 2 prerequisite guide](https://v2.tauri.app/start/prerequisites/), plus Git, Python 3.12+, `uv`, Node.js 22+, and stable Rust. Then run:

```
git clone https://github.com/HKUDS/DeepCode.git
cd DeepCode
uv venv --python 3.12
uv pip install --python .venv/bin/python -e .
.venv/bin/deepcode init
cd desktop
npm ci
npm run setup:sidecar
npm run build:sidecar
cd ..
mkdir -p ~/.local/bin
ln -sf "$(pwd)/scripts/deepcode-desktop" ~/.local/bin/deepcode-desktop
export PATH="$HOME/.local/bin:$PATH"
deepcode-desktop
```

The final link is a one-time source launcher installation. Afterwards, `deepcode-desktop` starts this checkout from any directory, provided `~/.local/bin` is on `PATH`. Add the export to your shell profile if it is not already configured. The command launches Desktop; add or select the repository you want to work on from the Project sidebar.

#### Windows from source

Windows requires Microsoft Edge WebView2 and the Visual Studio 2022 Build Tools workload **Desktop development with C++**. Accept the UAC prompt raised by Build Tools:

```
winget install --id Git.Git --exact
winget install --id astral-sh.uv --exact
winget install --id OpenJS.NodeJS.LTS --exact
winget install --id Rustlang.Rustup --exact
winget install --id Microsoft.VisualStudio.2022.BuildTools --exact \`
  --override "--wait --passive --norestart --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
```

Close PowerShell, open a new window, and verify the toolchains:

```
git --version
uv --version
node --version
rustup default stable-msvc
rustc --version
cargo --version
```

Clone, prepare, and start Desktop:

```
git clone https://github.com/HKUDS/DeepCode.git
Set-Location DeepCode
uv venv --python 3.12
uv pip install --python .venv\Scripts\python.exe -e .
.venv\Scripts\deepcode.exe init
Set-Location desktop
npm ci
$env:DEEPCODE_PYTHON = (Resolve-Path ..\.venv\Scripts\python.exe)
npm run setup:sidecar
npm run build:sidecar
npm run tauri -- dev
```

Keep that PowerShell window open while Desktop is running. See the [Desktop source guide](https://github.com/HKUDS/DeepCode/blob/main/desktop/README.md#windows-powershell) for subsequent launches and troubleshooting.

#### Configure the Desktop model

Open **Settings → AI providers** after Desktop starts.

[![Configure an AI provider and model in DeepCode Desktop](https://github.com/HKUDS/DeepCode/raw/main/assets/setting_model.png)](https://github.com/HKUDS/DeepCode/blob/main/assets/setting_model.png)

<sub>Provider credentials, model discovery, and inference verification stay in one Desktop workflow.</sub>

1. Select **Add provider**, choose the service, and enter an API key or its environment-variable name.
2. Select **Save and check** to verify the credential and load the provider's model catalog without sending repository content.
3. Under **Agent model**, choose an exact model ID and select **Save and verify model**. This final check sends only a minimal inference request.
4. Add or open a Project, create a Session, choose the model, Thinking effort, and access level, then describe the task in natural language.

> The interface changes how the work is presented, not the Agent, policy, configuration, or Session history behind it.

## Using DeepCode

### Sessions

Every task lives in a durable Session attached to its original Project. Open a Project in Desktop or start `deepcode` from its directory, then create a new Session or resume an existing one. The same history can move between Desktop and CLI without export or conversion.

| What you want to do | Desktop | Interactive CLI |
| --- | --- | --- |
| Start a Session | **New thread** | `/new [title]` |
| Resume local history | Select it under the Project | `/resume` |
| Find history from every Project | Browse the project list | `/resume all` |
| Attach a file | Use the composer attachment | `@path/to/file` |
| Change the next Turn's model | Composer model picker | `/model` |
| Adjust Thinking effort | Composer effort picker | `/effort` |
| Choose tool access | Composer access picker | `/permissions` |
| Load Skills for the next Turn | Composer Skills control | `/skill <name>` |
| Create a reusable Skill | **Skills → Create Skill** | `$skill-creator` |
| Set or revise a durable Goal | Goal panel | `/goal` |
| Stop the active Turn | Use the stop control | `/stop` |

Session history, tool activity, approvals, Goal state, and verification evidence remain together. Archiving hides a Session without deleting its history; permanent deletion removes the Session records but never repository files.

### Connections and models

Desktop provides connection setup and verification under **Settings → AI providers**. In the CLI, `/model` changes the connection and model for future Turns, while `/effort` selects a Thinking level supported by that model.

Model changes never rewrite earlier history or alter an active Turn. Thinking effort controls the request sent to the provider; transcript detail controls only presentation. DeepCode shows provider-designated reasoning summaries when available and never merges raw chain-of-thought into the assistant answer.

Provider administration, environment-variable credentials, custom gateways, model discovery, and machine-readable checks are documented in the [Headless and Automation guide](https://github.com/HKUDS/DeepCode/blob/main/docs/HEADLESS_AND_AUTOMATION.md#connection-and-model-management).

### Skills

Skills turn reusable engineering knowledge into instructions the Agent can load for a task. Desktop provides a Skills workspace; the interactive CLI uses `/skills` to discover them and `/skill <name>` to select one for the next Turn. Choose **Skills → Create Skill** in Desktop or invoke `$skill-creator` in CLI to create and validate one through a normal Agent Turn.

Project Skills in `.agents/skills` travel with a repository; user Skills in `~/.agents/skills` remain available across Projects. Existing DeepCode and Claude-compatible directories remain readable. A Skill can guide the Agent, but it cannot grant permissions or bypass Project trust, approvals, or tool policy. Import, enable, disable, and catalog commands live in the [advanced guide](https://github.com/HKUDS/DeepCode/blob/main/docs/HEADLESS_AND_AUTOMATION.md#skill-management).

### Safety and execution

DeepCode treats execution as a product boundary rather than a client-side confirmation:

- Projects require explicit trust before Agent execution on every interface.
- Permission decisions are `allow`, `ask`, or `deny`.
- An approval resumes the exact suspended tool call.
- **Ask** keeps the workspace command sandbox and protected-path checks; **Read only** denies mutating tools; **Full access** is an explicit, confirmed Session grant that removes approval and filesystem sandbox boundaries. Explicit deny rules still win.
- CLI and Desktop edit the same Session override. Each admitted Turn freezes the complete resolved security profile: changes apply to new submissions, while active and already queued Turns keep their recorded access after resume or worker handoff.
- Shell and code processes are terminated as owned process trees on timeout, interruption, or shutdown.
- Crash recovery settles incomplete Turns without automatically replaying side effects.

### Long-running work

Ordinary prompts can run a full multi-tool coding Turn. When work must continue across several Turns or process restarts, attach a durable Goal to the Session. Use the Goal panel in Desktop or `/goal <objective>` in the CLI.

While DeepCode works, new input can steer the active Turn. You can edit the Goal, stop the current Turn, queue a follow-up, pause the Goal, or resume it later. These actions preserve the same Session, history, permissions, Skills, and evidence instead of starting an isolated execution.

The working Agent requests `complete` or `blocked` from its full context. DeepCode enforces ownership, lifecycle, permission, and budget boundaries, but does not pretend a generic host-side rule can validate every coding task. A normal semantic result is labelled **Completed**; tests, builds, diagnostics, diffs, or independent review remain visible evidence. No provider, model, task type, or test command is fixed by the Goal engine.

### Automations and headless workflows

The Desktop Automation workspace turns a trusted Project instruction into a manual or interval run while keeping the normal Agent, Session, Goal, permissions, recovery, and Run history. Use it for repeatable work such as repository health checks, regression review, or scheduled maintenance.

Shell scripts and CI systems can use the same runtime without opening an interface. The separate [Headless and Automation guide](https://github.com/HKUDS/DeepCode/blob/main/docs/HEADLESS_AND_AUTOMATION.md) contains the `exec`, `loop`, Automation, Provider, Skill, and Session administration commands. They are advanced integration surfaces—not a second way ordinary Desktop or CLI users must learn to talk to DeepCode.

## Paper2Code

Paper2Code is the research origin of DeepCode and remains its specialized workflow for scientific code reproduction. The general coding Agent extends the product; it does not replace or flatten the original Paper2Code design.

Its central idea is unchanged: reproducing a paper is not a one-shot generation task. A central orchestrator coordinates distinct responsibilities for understanding the source, planning the reproduction, finding and indexing useful references, implementing the system, and verifying the result.

### The original architecture

[![Paper2Code framework from source documents through code generation, verification, and refinement](https://github.com/HKUDS/DeepCode/raw/main/assets/readme/framework2.png)](https://github.com/HKUDS/DeepCode/blob/main/assets/readme/framework2.png)

The specialist roles preserve the separation of concerns that made the original system effective:

| Role | Responsibility |
| --- | --- |
| **Central Orchestrating Agent** | Interprets progress, selects the next phase, coordinates specialists, and adapts the plan when evidence changes. |
| **Intent Understanding Agent** | Turns the user's objective into explicit functional requirements, technical constraints, and an actionable task decomposition. |
| **Document Parsing Agent** | Processes papers and technical documents, extracting algorithms, equations, methods, assumptions, and implementation requirements. |
| **Code Planning Agent** | Converts the understood method into an implementation roadmap, module boundaries, dependencies, interfaces, and verification goals. |
| **Code Reference Mining Agent** | Discovers relevant repositories, libraries, and implementation patterns, then evaluates their relevance and integration potential. |
| **Code Indexing Agent** | Builds a searchable semantic index and knowledge graph so useful components and relationships can be recovered during generation. |
| **Code Generation Agent** | Synthesizes the plan and evidence into executable code, tests, documentation, and the interfaces needed for a reproducible result. |

Four ideas connect those roles into one system:

- **Intelligent orchestration.** The central Agent chooses and revisits phases according to task state instead of treating reproduction as a fixed prompt chain.
- **Document and intent grounding.** Papers, specifications, URLs, and attached files are converted into explicit implementation requirements before code is written.
- **Memory and CodeRAG.** Large documents and reference repositories are segmented, indexed, and retrieved as bounded context rather than repeatedly placed into the model window.
- **Iterative verification.** Execution, tests, and observed failures feed back into planning and implementation until the deliverable has supporting evidence.

The supporting tool layer follows the same division:

| Layer | Purpose |
| --- | --- |
| Document ingestion | Fetch and normalize papers, URLs, PDFs, DOCX, presentations, text, and HTML. |
| Document segmentation | Divide long technical material into coherent, recoverable sections for analysis. |
| Reference discovery | Find candidate repositories and supporting implementations. |
| Code reference indexing | Build searchable context over external and local code, including cross-file relationships. |
| Implementation execution | Read and write files, run shell or Python commands, inspect the project structure, and keep logs. |
| Verification and delivery | Run tests, record results, and deliver the codebase together with documentation and Artifacts. |

The modern product adds durable plans, explicit plan review, checkpoints, bounded retries, and interactive inspection around this workflow. Those additions make recovery and supervision stronger while preserving the Paper2Code architecture and its order of reasoning.

### Research results

The original DeepCode study evaluates scientific code reproduction on [PaperBench](https://openai.com/index/paperbench/), which asks agents to reproduce 20 ICML 2024 papers across 8,316 gradable components.

| **75.9%**   <sub>Human expert subset<br>+3.5 points</sub> | **84.8%**   <sub>Commercial-agent subset<br>+26.1 points</sub> | **73.5%**   <sub>Scientific coding<br>+22.4 points</sub> | **73.5%**   <sub>LLM-agent baseline<br>+30.2 points</sub> |
| --- | --- | --- | --- |

[![DeepCode PaperBench results](https://github.com/HKUDS/DeepCode/raw/main/assets/result_main02.jpg)](https://github.com/HKUDS/DeepCode/blob/main/assets/result_main02.jpg)

| Evaluation subset | DeepCode | Reported comparison | Difference |
| --- | --- | --- | --- |
| Human expert subset | 75.9% | Best reported human baseline: 72.4% | +3.5 points |
| Commercial-agent subset | 84.8% | Best reported commercial agent: 58.7% | +26.1 points |
| Scientific coding | 73.5% | PaperCoder: 51.1% | +22.4 points |
| LLM-agent baseline | 73.5% | Best reported LLM agent: 43.3% | +30.2 points |

These are PaperBench-specific results reported by the original study. They are not a general-purpose coding benchmark or a comparison against continuously updated products.

Read the [paper](https://arxiv.org/abs/2512.07921) for methodology, evaluation scope, models, and baseline details.

## 🎬 Live Demonstrations

These recordings show projects produced by earlier DeepCode workflows. They are output demonstrations rather than screenshots of the current Desktop UI.

| #### 📄 Paper2Code  **Research to implementation**  [![Paper2Code demonstration](https://camo.githubusercontent.com/85910fb811045219ad1395bbfe5a6c4f2693a31c1c262163590d0713e7d66c0f/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f4d515a59704c6b7a7362772f6d617872657364656661756c742e6a7067)](https://www.youtube.com/watch?v=MQZYpLkzsbw)  **[▶ Watch demonstration](https://www.youtube.com/watch?v=MQZYpLkzsbw)**  <sub>Reproduce a research paper as an executable project.</sub> | #### 🖼️ Generated vision project  **Image workflow example**  [![Generated image-processing project](https://camo.githubusercontent.com/66dfdd7450b34e5e0aaaed1e815e8be6fed9387b5c93d8834ad9e649e3d6ab38/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f6e4674356d4c614d4561632f6d617872657364656661756c742e6a7067)](https://www.youtube.com/watch?v=nFt5mLaMEac)  **[▶ Watch demonstration](https://www.youtube.com/watch?v=nFt5mLaMEac)**  <sub>See an earlier generated image-processing workflow in use.</sub> | #### 🌐 Generated web project  **Frontend implementation example**  [![Generated frontend project](https://camo.githubusercontent.com/3ee2783e935ac6d506f6c4f3833f5ed1ba66e296922ff2408c6f573fe622daf3/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f3738777833646b546141552f6d617872657364656661756c742e6a7067)](https://www.youtube.com/watch?v=78wx3dkTaAU)  **[▶ Watch demonstration](https://www.youtube.com/watch?v=78wx3dkTaAU)**  <sub>Follow a complete frontend implementation from idea to result.</sub> |
| --- | --- | --- |

The [project introduction](https://youtu.be/PRgmP8pOI08) remains available for a broader walkthrough.

## Development

### Source installation

```
git clone https://github.com/HKUDS/DeepCode.git
cd DeepCode

curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python=3.13
source .venv/bin/activate
uv pip install -e .
```

On Windows PowerShell, activate with `.\.venv\Scripts\Activate.ps1`.

### Verification

```
uvx pre-commit run --all-files
python -m compileall -q app_server cli core tools workflows
deepcode --version
deepcode-app-server --verify-runtime

cd desktop
npm run lint
npm test -- --run
npm run build
```

Desktop packaging, Rust checks, signing, and release procedures are documented in [`desktop/README.md`](https://github.com/HKUDS/DeepCode/blob/main/desktop/README.md) and the [Desktop release runbook](https://github.com/HKUDS/DeepCode/blob/main/docs/DESKTOP_RELEASE_RUNBOOK.md).

**Contributor architecture notes**

| Topic | Document |
| --- | --- |
| Agent execution and approvals | [P2 Agent execution](https://github.com/HKUDS/DeepCode/blob/main/docs/P2_AGENT_EXECUTION_ARCHITECTURE.md) |
| Desktop sidecar and lifecycle | [P3 Desktop runtime](https://github.com/HKUDS/DeepCode/blob/main/docs/P3_DESKTOP_RUNTIME_ARCHITECTURE.md) |
| Git review, files, terminal, and tests | [P4 Code workbench](https://github.com/HKUDS/DeepCode/blob/main/docs/P4_CODE_WORKBENCH_ARCHITECTURE.md) |
| Durable Paper2Code workflow | [P5 Paper2Code](https://github.com/HKUDS/DeepCode/blob/main/docs/P5_PAPER2CODE_ARCHITECTURE.md) |
| Canonical Sessions and cross-directory resume | [P6 Session alignment](https://github.com/HKUDS/DeepCode/blob/main/docs/P6_SESSION_ALIGNMENT_REVIEW.md) |
| Skills identity, security, and persistence | [Skills architecture](https://github.com/HKUDS/DeepCode/blob/main/docs/SKILLS_PRODUCT_ARCHITECTURE.md) |
| Automation scheduling and execution | [Automation architecture](https://github.com/HKUDS/DeepCode/blob/main/docs/AUTOMATION_ARCHITECTURE.md) |
| Desktop product and interaction model | [Desktop UI specification](https://github.com/HKUDS/DeepCode/blob/main/docs/DESKTOP_PRODUCT_UI_SPEC.md) |
| Privacy and diagnostics | [Privacy contract](https://github.com/HKUDS/DeepCode/blob/main/docs/PRIVACY_AND_DIAGNOSTICS.md) |

The pre-restructure README is preserved in [`docs/archive/README_LEGACY_2026-07-20.md`](https://github.com/HKUDS/DeepCode/blob/main/docs/archive/README_LEGACY_2026-07-20.md). The empty product-image slots have a shared [capture brief](https://github.com/HKUDS/DeepCode/blob/main/assets/readme/README.md).

---

## ⭐ Star History

*Community growth trajectory*

[

![DeepCode Star History chart](https://camo.githubusercontent.com/9ee3fb6e30ba4923c9af0b730937e96b323430eb8c998dd6fc0e582a2233a9ac/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d484b5544532f44656570436f646526747970653d44617465)

](https://star-history.com/#HKUDS/DeepCode&Date)

---

### 🚀 Ready to build with DeepCode?

[![Get started](https://camo.githubusercontent.com/79f97c82e90fe69edf64798fe91c182e2c636188b4ca244735d7f925847b6b71/68747470733a2f2f696d672e736869656c64732e696f2f62616467652ff09f9a805f4765745f537461727465642d3030643466663f7374796c653d666f722d7468652d6261646765266c6f676f3d726f636b6574266c6f676f436f6c6f723d7768697465)](#quick-start) [![View DeepCode on GitHub](https://camo.githubusercontent.com/f981f4457f1976d226695d4ae3b4000bfd08191fffbe3ec4af89f0117e45a284/68747470733a2f2f696d672e736869656c64732e696f2f62616467652ff09f8f9befb88f5f566965775f6f6e5f4769744875622d3030643466663f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://github.com/HKUDS/DeepCode) [![Star DeepCode](https://camo.githubusercontent.com/3e94132a0f1875dc360ed98f2518f18cb47bc5abaf271b13f654e2cbca892f41/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe2ad905f537461725f50726f6a6563742d3030643466663f7374796c653d666f722d7468652d6261646765266c6f676f3d73746172266c6f676f436f6c6f723d7768697465)](https://github.com/HKUDS/DeepCode/stargazers)

---

## 🙏 Appreciation

Thanks to everyone in the open-source community — your stars, issues, pull requests and discussions shape where DeepCode goes next.

[![DeepCode contributors](https://camo.githubusercontent.com/aa3160c3d9c86afa87b0bd570a2ab446df03153cb830c5096c1546da04828b15/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d484b5544532f44656570436f6465266d61783d393939)](https://github.com/HKUDS/DeepCode/graphs/contributors)

Everyone who has opened a pull request is listed in [CONTRIBUTORS.md](https://github.com/HKUDS/DeepCode/blob/main/CONTRIBUTORS.md), including contributions that predate the v2.0 rebuild and so are not reflected in the graph above.

---

## 📖 Citation

If DeepCode contributes to your research, cite:

```
@misc{li2025deepcodeopenagenticcoding,
  title         = {DeepCode: Open Agentic Coding},
          = {Zongwei Li and Zhonghang Li and Zirui Guo and Xubin Ren and Chao Huang},
  year          = {2025},
  eprint        = {2512.07921},
  archivePrefix = {arXiv},
  primaryClass  = {cs.SE},
  url           = {https://arxiv.org/abs/2512.07921}
}
```

---
- **Source:** Unknown
