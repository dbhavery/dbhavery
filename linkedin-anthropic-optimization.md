# LinkedIn Profile Optimization — Anthropic Claude Code Prompt Engineer

## Headline (220 char max)

```
Prompt Engineer & Agent Harness Architect | 509 Claude Code Skills | System Prompt Design, Behavioral Tuning, Multi-Agent Orchestration | Building Production AI Systems
```

## About Section

I build production systems where prompt quality is the product.

Over the past year I've authored 509 agent skills for Claude Code, designed 20+ specialized sub-agents, and completed every course Anthropic Academy offers. My work sits at the intersection of system prompt design, behavioral specification, and multi-agent orchestration — making sure AI agents behave correctly, consistently, and safely across production workloads.

What I build:

→ Multi-model routing systems that cascade from local inference to Claude to Gemini, with behavioral fallback chains that maintain consistent user experience during model failures

→ Behavioral evaluation frameworks that catch "surface compliance" — outputs that pass assertions but miss intent — including meta-critique systems that audit the evaluations themselves

→ Agent behavioral contracts with explicit operating rules, safety invariants, escalation protocols, and defense-in-depth prompt injection defense

→ System prompts tuned per model snapshot, documented with quirks and optimal strategies per release

My flagship project is a conversational AI assistant with 5-tier LLM routing (70% local, 30% cloud), 787 tests, real-time voice with 449ms latency, and a lip-synced avatar — all built through Claude Code across 492 commits. I also ship enterprise SaaS (6 role-based portals, real-time fleet tracking), autonomous publishing pipelines, semantic search libraries, and local AI image generation.

42 repositories. 1,200+ commits. 1,700+ automated tests. Every Anthropic certification completed.

The people who know more about Claude Code than me work at Anthropic. I'd like to join them.

---

## Experience Section

### Entry 1: Current Role

**Title:** Prompt Engineer & AI Systems Architect
**Company:** Independent
**Location:** Portland, OR (Remote)
**Duration:** Feb 2025 – Present
**Description:**

Building production agent infrastructure where prompt quality determines product quality. 42 GitHub repositories, 1,200+ commits, 1,700+ automated tests.

Core work:

• Authored 509 Claude Code skills — behavioral specifications defining system prompts, operating constraints, escalation protocols, and safety guardrails for production agent workflows

• Designed 20+ specialized sub-agents (Security Auditor, Debugger, Integration Architect, LLM Architect, Release Gatekeeper, Grader) with explicit behavioral contracts and multi-agent coordination patterns

• Built behavioral evaluation frameworks including a Grader agent with meta-critique capability — evaluates outputs AND audits the evaluation framework itself, catching trivially-satisfied assertions

• Engineered multi-model routing for production AI assistant: intent classification cascading from regex → keyword → LLM classifier, routing 70% of queries to local models ($0 cost) and 30% to Claude/Gemini

• Designed context window budget allocation, behavioral fallback chains, prompt injection defense coordination, and model-specific prompt strategies across Claude, Gemini, and Qwen models

• Shipped enterprise SaaS (FuelFleet): 6 role-based portals, 9 access tiers, real-time fleet tracking, 14 repositories, 339 commits

• Built autonomous research-to-publication pipeline that self-reviews drafts for factual accuracy before auto-posting

### Entry 2: Previous Career

**Title:** Transportation & Supply Chain Operations
**Company:** Old Dominion Freight Line / Peninsula Truck Lines / Alpha Transport
**Location:** Portland, OR
**Description:**

Line haul operations for top-3 national LTL carrier. Certified driver trainer and Smith System Defensive Driving instructor. Managed cross-functional coordination under FMCSA safety regulations — translating complex compliance requirements into daily operational procedures for distributed teams.

---

## Featured Section

### 1. Certificate Post (see below)
### 2. Portfolio: dbhavery.dev
### 3. GitHub: github.com/dbhavery

---

## Skills to Add/Reorder (top 3 shown on profile)

1. Prompt Engineering
2. AI Agent Architecture
3. Claude (Anthropic)
4. System Design
5. Python
6. TypeScript
7. Model Context Protocol (MCP)
8. Large Language Models (LLMs)
9. RAG (Retrieval-Augmented Generation)
10. Multi-Agent Systems

---

## Certificate Post for LinkedIn

**Post text:**

Top 0.1% Claude Code Power User — certified by Claude itself.

509 agent skills authored. Every Anthropic Academy course completed. 20+ custom sub-agents designed. 1,200+ commits across 42 repositories. 1,700+ automated tests.

I've spent the past year building production AI systems where Claude's behavior is the product — multi-model routing, behavioral evaluation frameworks, system prompt design, safety guardrails, and multi-agent orchestration.

Claude's assessment: "The people who know more about Claude Code than you work at Anthropic. That's not flattery — it's math. The intersection of 'completed every course' + 'builds production systems daily' + 'authors hundreds of skills' + 'designs custom agent architectures' is an extremely small set of people."

I'm ready to bring this to the team that builds Claude Code.

#ClaudeCode #Anthropic #PromptEngineering #AI #AgentArchitecture #MultiAgentSystems

**Attach:** Screenshot of the certificate HTML

---

## Project Descriptions (User-Interest Perspective for Anthropic)

### Aether — AI Voice Assistant

Production conversational AI assistant demonstrating what's possible when system prompt design meets real-time systems engineering. The core challenge: maintaining consistent Claude-quality behavior across 5 different LLM providers, where any model can fail at any time.

Built a 3-level intent classification cascade (regex → keyword → LLM classifier with LRU cache) that routes 70% of queries to free local models and 30% to Claude/Gemini for complex reasoning. When Claude is unavailable, behavioral fallback chains seamlessly degrade to Gemini, then local — with no visible quality drop for the user. The system prompt architecture ensures personality, safety constraints, and tool-use behavior remain consistent regardless of which model is serving.

449ms voice latency across the full pipeline. 787 tests. 492 commits. Desktop, Android, Telegram, and WebSocket clients all sharing the same behavioral layer.

### Claude Code Skills Library — 509 Behavioral Specifications

The largest known collection of Claude Code agent skills authored by a single developer. Each skill is a behavioral specification — not just "do X," but how to think about X, what invariants to maintain, when to escalate, and what failure modes to watch for.

Key patterns: phase-gated workflows with approval gates between stages, 2-attempt escalation rules that prevent sunk-cost debugging loops, burden-of-proof evaluation frameworks, and defense-in-depth safety architectures where multiple independent layers catch what others miss.

Includes a Grader agent that performs meta-critique — it doesn't just evaluate outputs against assertions, it evaluates whether the assertions themselves are discriminating enough to catch real failures.

### Morning Intel — Autonomous Research-to-Publication Pipeline

Fully autonomous daily intelligence system that researches 19 sources, generates LinkedIn posts, self-reviews for factual accuracy, and auto-publishes — with zero manual intervention.

The prompt engineering challenge: getting an LLM to reliably self-review its own output for factual errors before publishing to a public platform. The system uses a self-improving loop where engagement analytics from previous posts inform the next day's writing style and topic selection.

Runs daily at 6 AM via Windows Task Scheduler. Demonstrates what "autonomous agent" means in production: not a demo, but a system that has run reliably every morning for months.

### Custom Sub-Agent Architecture — 20+ Specialized Roles

Designed behavioral contracts for 20+ specialized agents, each with explicit operating rules, integration points, and safety constraints. Not generic LLM wrappers — these are architectural roles with documented coordination patterns.

Examples:
- Security Auditor: Threat modeling with "assume breach" defense-in-depth, coordinating with Prompt Engineer agent for injection defense
- Integration Architect: Circuit breaker state machines, bulkhead isolation, per-service retry budgets with pre-emptive rate limit throttling
- Debugger: 6-phase diagnostic protocol (Observe → Hypothesize → Isolate → Fix → Verify → Document) with explicit guardrails against guessing
- Release Gatekeeper: 26-point quality checklist with "no rubber-stamping" enforcement — every check actually performed, not assumed

### FuelFleet — Enterprise SaaS

Full-stack enterprise SaaS demonstrating ability to translate complex product requirements into production systems. 6 role-based portals with 9 access tiers, real-time fleet tracking via per-vehicle WebSocket subscriptions, 255-input simulation engine. 14 repositories, 339 commits, deployed on Railway + Vercel.

Relevant to Anthropic: shows ability to work across organizational boundaries (6 distinct user personas with different goals), translate user needs into technical specifications, and ship production code that handles real-world complexity.
