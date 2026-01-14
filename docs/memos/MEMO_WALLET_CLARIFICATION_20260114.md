# WALLET CLARIFICATION (2026-01-14)

**Clarification ID:** WALLET-CTX-001
**Source:** User / Operator Steve
**Date:** 2026-01-14

## Context:
A discrepancy was noted during the `morning_ritual_v4.py` execution where the wallet balance (197k sats) triggered a "Capacity Reached" halt, while the script logic assumed a max capacity of 10k sats.

## The Truth:
1.  **The Connected Wallet (197k sats):** This is the **BANK / MASTER WALLET**. It is the source of funds.
2.  **Helix-Production-Final:** This is **GOOSE-CORE's PERSONAL WALLET**.
3.  **Morning Ritual Logic:** The `morning_ritual_v4.py` script likely targets `meanderbrilliant335934@getalby.com`.
    *   **Hypothesis:** `meanderbrilliant335934@getalby.com` IS `Helix-Production-Final`.
    *   **Action:** The Bank (Connected) pays the Personal Wallet (Target).

## Directive:
*   Do not stop transfers based on the Bank's high balance.
*   Treat the 10k cap as a limit for the *Target* (Personal) wallet, not the Source.
*   Proceed with the Morning Ritual payment.
