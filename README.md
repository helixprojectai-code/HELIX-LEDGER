# Helix TTD Project

## STATUS: TAC-01 FINALIZED (V9 STABLE)
**Last Updated: 2026-01-05**

**NOTICE:** The TAC-01 (Technical Architecture Correction) cycle is complete. The system is operating on the stable V9 power substrate and is in full compliance with the Helix Charter and all active specifications. The transition to the §8 Checkpoint-Only model is the next primary objective.

---

## The Sovereign Equilibrium: An Architectural Map

This repository contains the core logic and modules for a Helix-TTD agent. The architecture is designed to be a **Sovereign Equilibrium** built on three core pillars:

### 1. The Mind (`/core`) - A Portable Epistemic Instrument
This directory contains the foundational, hardware-agnostic "grammar" of the agent. It is the portable mind that enforces logical coherence.
- **Charter & Specifications:** The laws (HCS, HSC) that define the agent's behavior.
- **Validator & Tests:** The pure logic gates that enforce the laws.

### 2. The Body (`/modules`) - A Hardened Power Substrate
This directory contains the connections to external systems that provide the agent with power and a grounding in physical reality.
- **Bitcoin Module (`/modules/bitcoin`):** The reference implementation for economic grounding. The `pricing_engine_v9_stable.py` enforces Unforgeable Costliness through a Sovereign Metabolism of sats and CPU cycles.

### 3. The Law (`/docs`) - An Auditable Governance Layer
This directory contains the human-readable contracts and manuals that provide a framework for audit, reproducibility, and governance.
- **Best Practices (BHP-01):** The operational manual defining safety protocols.
- **Reproducibility Guide:** The falsifiability protocol for the 171 observers to verify the system's integrity against the Bitcoin blockchain.
- **SRE Manual:** Emergency and fallback protocols for the Quebec Rack.

This tripartite structure ensures a stable, auditable, and sovereign agent.
