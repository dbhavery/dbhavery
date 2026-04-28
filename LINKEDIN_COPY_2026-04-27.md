# LinkedIn Copy Package — Don Havery

**Date:** 2026-04-27
**Source data:** Live April 2026 web research on AI hiring market (Anthropic + Cursor + fal.ai + Fireworks live careers pages, plus LinkedIn headline analysis on recently-hired AI engineers, plus Boris Cherny Anthropic hiring statement Jan 2026).

**Positioning thesis (revised after live research):**
- The unified "AI Engineer" title does not exist at frontier labs. Anthropic, Cursor, fal.ai, Fireworks all use **Forward Deployed Engineer** + **Applied AI Engineer** + **Software Engineer, [domain]** + **Member of Technical Staff**. Pivot to JD-vocabulary.
- **Forward Deployed Engineer** is the single hottest title in the market right now. Anthropic alone has 7+ open. Operator-empathy / non-traditional background is a *feature* for FDE, not a liability.
- **MCP is now table-stakes**, not differentiator. RAG is the #1 JD keyword. Agentic is #2. Evals is #3.
- Boris Cherny (Anthropic, Jan 2026): hiring is shifting toward *"generalists with judgment over specialists with credentials"* — exactly Don's narrative.

---

## 1. Headline (220 char cap, paste-ready)

**Current:** `AI Engineer | System Prompt Design, Behavioral Tuning, Multi-Agent Orchestration`

**Don's pick — Option A** (algorithm-optimal, no career-stage signal):

### Option A — declarative + concrete artifact (use this)
```
Forward-Deployed AI Engineer · Shipped a 7-sub-agent voice harness at 449ms latency · Top 0.1% Claude Code · MCP, Agentic Systems, Evals
```

### Option C — safest declarative (acceptable backup)
```
Forward-Deployed Engineer · Applied AI · Building agentic systems with Claude Code and MCP · Top 0.1% Claude Code (Anthropic-certified)
```

(A prior Option B floated an "unusual-arc / ex-line-haul" opener. Don rejected that direction — career-stage and prior-industry signals suppressed across all surfaces.)

**Recruiter-search keywords required (must appear exactly once across headline + about + skills):** Forward Deployed, Applied AI, Agentic, MCP, RAG, Evals, Claude Code.

---

## 2. About section (paste into LinkedIn About, 2,600 char cap)

```
I design and ship production agentic systems end-to-end — harness, tools, evals, observability, fine-tuning. I am a Forward-Deployed-shaped engineer: I build with the customer's actual workflow in mind, then go fix the thing that breaks at 2 AM.

What I've shipped (all real, all in production):

— Aether: voice-agent harness with 7 coordinated sub-agents, 5-model routing across Claude / Gemini / Qwen / local Ollama, 449 ms end-to-end voice latency, cross-provider behavioral parity verified. 492 commits, 787 tests. Desktop (PySide6 + Rust/Tauri) + Android + Telegram + WebSocket clients.

— Vault: RAG over 152K personal files. Hybrid retrieval (BM25 + dense), ChromaDB, bge-m3 embeddings. The production-scale data infra version of the same RAG patterns Aether uses.

— Herald: autonomous research-to-publication pipeline. Pulls from 19 sources, drafts, fact-checks, generates a hero image, posts to LinkedIn, scrapes engagement back, feeds the writer prompt. Runs daily, in production for months.

— A self-improvement loop with calibrated evals + 6 mutation strategies + a Grader sub-agent that audits whether the eval assertions themselves discriminate. Catches tests passing for the wrong reasons. Flagged Sonnet 4 refusal-boundary and tool-use shifts within hours of release; retuned affected behavioral specs same day.

42 repos. 1,200+ commits. 1,700+ automated tests. All authored through Claude Code as a daily pair-programmer.

Credentials: Top 0.1% Claude Code user (Anthropic-certified). All 16 Anthropic Academy courses complete. DeepLearning.AI Generative AI with LLMs. B.S. CS in progress at Capella (AI Engineering & Machine Learning concentration).

Operator background in safety-critical, regulated environments — including a certified-trainer role responsible for signing off new operators to work independently. The reliability mindset transfers directly to production AI: prompts, evals, and harnesses are version-controlled product, not throwaway artifacts. When you're wrong, someone gets hurt.

Open to: Forward Deployed Engineer / Applied AI Engineer / Software Engineer (Agent Harness, Evals, Voice) / Member of Technical Staff.

Vancouver, WA — open to Seattle / SF / NYC, remote-first, 25% travel.
```

---

## 3. Top 3 Skills (LinkedIn Skills section, pinned)

LinkedIn weights the top 3 most heavily for recruiter search. Set these in this order:

1. **Multi-Agent Systems** (or "Agentic Systems" if available — this is the #2 JD keyword, your strongest evidence)
2. **Retrieval-Augmented Generation (RAG)** (#1 JD keyword in 2026)
3. **Model Context Protocol (MCP)** (now table-stakes; signals Anthropic-ecosystem fluency)

---

## 4. Full Skills section (in priority order, ~25-30 entries — LinkedIn caps practical use at ~30)

Add these in this order. Pinned 3 above; the rest fall into "other."

```
Multi-Agent Systems
Retrieval-Augmented Generation (RAG)
Model Context Protocol (MCP)
LLM Evals
Tool Use / Function Calling
Claude Code
Agent Orchestration
Prompt Engineering
Forward Deployed Engineering
Applied AI
LangGraph
Python
TypeScript
Next.js
Rust
Tauri
FastAPI
React
PostgreSQL
ChromaDB
Vector Databases
WebSocket
Playwright
LoRA Fine-Tuning
Hugging Face
PyTorch
Voice AI
Real-Time Systems
Observability
Production Reliability
```

**Skills to remove from your current LinkedIn (if present):**
- "Machine Learning" (raises a credential question your evidence can't answer; replace with specific RAG / LoRA / Eval items)
- "MLOps" (renamed to "AI Infra" in 2026 JDs)
- Generic "Artificial Intelligence" (signals 2023-era profile)
- Anything saying "Beginner" or "Intermediate" — only keep what you can defend

---

## 5. Featured section (the 3 pinned items at the top of the profile)

Replace whatever's currently pinned with these three:

1. **Top 0.1% Claude Code Power User certificate** — your highest-leverage credibility hook.
2. **dbhavery.dev portfolio link** — concrete artifacts, your strongest non-resume signal.
3. **Aether GitHub repo** (github.com/dbhavery/aether) — the single most evidentiary project.

---

## 6. Open-to-work tags

LinkedIn lets you select target titles for the "Open to Work" frame. Set these (replace any current selections):

```
Forward Deployed Engineer
Applied AI Engineer
Software Engineer
Member of Technical Staff
Solutions Architect
AI Engineer
Developer Advocate
```

Geography: Seattle, Bellevue, San Francisco, New York, Remote.

---

## 7. Open Anthropic applications — triage based on live data

The live careers scrape confirms these specific roles are real and open as of 2026-04-27:

**KEEP IN PIPELINE — your evidence supports them:**
- **Prompt Engineer, Claude Code** — the JD literally exists at Anthropic; pure-prompt roles persist *inside* frontier labs as specialist roles. Your top-0.1% signal is the bullseye.
- **Applied AI Engineer (Digital Natives Business)** — Applied AI is Anthropic's largest single team build-out (15+ open).
- **Forward Deployed Engineer (any of 7+ variants)** — if any are in your batch, these are your strongest fit. If not, add them post-cooldown.
- **PM, Claude Code** — your 509 skills authored is unusually strong PM signal for that team.
- **SE, Voice Platform** — Aether voice harness is direct evidence; this is one of only 1-2 voice openings at Anthropic.
- **SE, Developer Productivity** — you build dev productivity tools daily; clean fit.
- **Developer Advocate / Education** — your portfolio + Herald daily content is exactly the signal this team weights.

**LET THESE DIE QUIETLY — your evidence doesn't support them:**
- All Research Engineer roles (Pretraining, RL, Reward Models Platform, Cowork/Virtual Collaborator, Universes, Environment Scaling, Production Model Post-Training)
- Senior Research Scientist (Reward Models)
- Anthropic Fellows (ML Systems & Performance, RL, AI Safety, AI Security, Base)
- Cloud Inference Safeguards (infra-heavy, no large-scale production evidence)

The research roles raise a "where's the paper?" question you cannot currently answer. Recruiter rejection there is correct triage, not a slight.

**Post-cooldown next move (post-Oct 2026):** warm intro through a Claude Code or Applied AI / FDE / Developer Advocate team member, not another cold application. Volume already triggered the rate-limit; the next shot must be referred.

---

## 8. Source URLs (live as of 2026-04-27)

- https://job-boards.greenhouse.io/anthropic
- https://www.anthropic.com/jobs
- https://job-boards.greenhouse.io/anthropic/jobs/4985877008 (Forward Deployed Engineer, Applied AI)
- https://cursor.com/careers
- https://fal.ai/careers
- https://fireworks.ai/careers
- https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/
- https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/
