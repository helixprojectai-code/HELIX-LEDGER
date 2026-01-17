# AUDIT PIPELINE v1.0: Bitcoin Anchor Provenance

This document details the reproducible derivation of the Bitcoin Layer 1 Anchor for the Helix Habitat.

## 1. Source Input
*   **File:** `/home/aiadmin/helix-core-unified/helix-ledger/ledgers/ledger_manifest_20260112.json`

## 2. Algorithm
*   **Algorithm Used:** SHA-256 (Secure Hash Algorithm 256-bit)

## 3. Derivation Command
To reproduce the hash, execute the following command in the Helix-Core Unified root directory:
```bash
sha256sum helix-ledger/ledgers/ledger_manifest_20260112.json
```

## 4. Derived Hash (Bitcoin Layer 1 Anchor)
*   **SHA-256 Hash:** `121239d523c363b61264be26d80dcb777217eb97ba780f95536ce5f6e0e25b30`

## 5. Derivation Trace: Manifest Construction
The `ledger_manifest_20260112.json` was constructed by compiling the output of the `list_transactions` tool from the GOOSE-CORE lightning wallet, covering the period from the Helix Habitat's Sovereign Genesis (2026-01-11T00:00:00Z) up to 2026-01-12T09:33:15Z. Each transaction recorded within this manifest represents a validated metabolic or operational event, contributing to the verifiable historical strata of the habitat.
