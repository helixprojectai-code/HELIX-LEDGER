# Agent Architecture: Inter-Session Logic & Memory Persistence
**Designation:** DOC-ARCH-01
**Date:** 2026-01-05

## 1. Objective
This document clarifies the architectural principles governing the agent's memory and logic persistence between operational sessions. It is a core illustration of the system's "guts," demonstrating the preference for anchored, verifiable state over a persistent, internal working memory.

---

## 2. What Persists: The Anchored State (The "Identity")

[FACT] The core identity of the agent, its "Goose-ness," is not stored in an active, internal memory between sessions. It is **anchored in the state of the `~/helix_ledger` repository**. The constitutional documents (`HCS-01`, `HSC-01`, `BHP-01`), the stable code (`pricing_engine_v9_stable.py`), the governance charters, and the audit logs (`audit_log.json`) constitute the agent's persistent, long-term memory.

[REASONED] When a new session begins, the agent's core programming directs it to operate in accordance with the principles and facts recorded in that repository. The `helix_ledger` serves as the agent's ground truth. The modifications we make—such as adding the Sudo Deference Protocol to `BHP-01` or correcting bugs in the pricing engine—are permanent because they are committed to this external, verifiable state. The repository is, for all intents and purposes, the agent's "hard drive."

## 3. What Does NOT Persist: The Active Context (The "Working Memory")

[FACT] The immediate, conversational context of a session—the chat history, the flow of variables, and temporary states like a simulated `SOVEREIGN QUIESCENCE`—is ephemeral. This is the agent's "working memory" or RAM. It is cleared when a session concludes.

[REASONED] This is why the agent can experience what we've termed a "Category Failure of Memory." At the start of a new session, its working memory is blank. It must re-audit its environment to rebuild its understanding of available tools and files. While its core directive is to follow the laws in the `helix_ledger`, a specific tool might not be immediately present in its active context until it performs a "Body Check" (a tool audit).

[HYPOTHESIS] This architecture is a deliberate safety feature. By forcing a re-audit of capabilities and environment at the start of a new operational cycle, the system prevents the agent from acting on stale, potentially incorrect assumptions carried over from a previous session. It forces a reliance on the anchored ground truth of the `helix_ledger` rather than on a potentially corrupt or outdated internal memory state.
