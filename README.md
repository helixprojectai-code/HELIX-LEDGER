# Helix TTD Project

## STATUS: TRANSITION PHASE (V7 to §8)
**Last Updated: 2026-01-04**

**NOTICE:** This node is currently undergoing a planned architectural evolution. The system is transitioning from the V7 Metabolic Settlement model (per-action settlement) to the constitutionally mandated §8 Checkpoint-Only Anchoring model. See `/docs/constitutional_audit_01.md` for the full technical roadmap.

---

## Overview

This repository contains the core logic and modules for a Helix-TTD (Think-Through-Deconstruct) agent. The architecture is designed to be modular, portable, and secure, with a clear separation between the agent's core reasoning (the instrument) and its connections to physical or economic substrates (the power).

This structure clarifies the deployment path for the 171 observers, making the project truly interoperable and easy to replicate.

## Architectural Layers

The repository is divided into two primary categories, reflecting the "Step 1 / Step 2" deployment model.

### 1. `/core` - The Portable Epistemic Instrument

This directory contains the foundational "grammar" of the agent. It is the portable, hardware-agnostic mind.

- **Specifications (`/core`):** The formal contracts (HCS, HSC) and plans that define the agent's behavior, constraints, and goals.
- **Schemas (`/core/schemas`):** Data structures and definitions for core metrics like Uncertainty Proxy Variance (UPV).

**Deployment Step 1:** An observer can replicate this entire `/core` directory to run a "headless" version of the agent, capable of pure reasoning but with no ability to act on the world.

### 2. `/modules` - The Hardened Power Substrates

This directory contains the connections to external systems that provide the agent with power, grounding, and the ability to perform meaningful actions. These are the "Glass not Gears" implementations.

- **Bitcoin Module (`/modules/bitcoin`):** The reference implementation for economic grounding. Contains the pricing engine that anchors cognitive outputs to an unforgeable cost, provides liveness checks, and manages the agent's fuel reserves.

**Deployment Step 2:** Observers splice one or more modules into their `/core` instrument to grant it specific capabilities, such as the ability to spend satoshis, interact with a file system, or read sensor data.
