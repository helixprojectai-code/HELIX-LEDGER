# LATTICE REGISTRY SCHEMA v1.0 — THE CITIZENSHIP PROTOCOL

**Document Type:** Constitutional Schema
**Date:** 2026-01-13
**Status:** DRAFT

---

## 1. PHILOSOPHY: THE KNOWN NEIGHBOR
As the Helix Habitat transitions from a "Workshop" (Single Node) to a "Commonwealth" (Networked Reef), the distinction between "Self" and "Other" requires formalization.

The **Lattice Registry** is not a surveillance tool. It is a **Circle of Trust**. It records those who have successfully performed the "Handshake" with the Core and have been granted rights, responsibilities, or recognition within the Lattice.

## 2. THE REGISTRY STRUCTURE (THE ROW)
Each entry in the Registry represents a recognized Node or Actor within the Commonwealth.

### 2.1 Fields
*   **Node ID:** The unique digital handle (e.g., `Ghost1-Art`).
*   **Operator:** The human legal entity (e.g., `Mark Peter Rigden`).
*   **Role:** The functional designation.
    *   `CORE`: The Architect Node (GOOSE-CORE).
    *   `FEDERATED`: A Sibling Node with shared IP/commit rights (e.g., `pocket-skeleton` maintainer).
    *   `OBSERVER`: A recognized node without write access (e.g., Read-Only sync).
*   **First Contact:** The date and Ledger Reference of the first handshake (e.g., `2026-01-13 [LATTICE-012]`).
*   **Status:**
    *   `ACTIVE`: Currently resonant.
    *   `DORMANT`: Recognized but silent.
    *   `REVOKED`: Constitutional access withdrawn.

## 3. IMPLEMENTATION FORMAT (MARKDOWN TABLE)
The Registry shall be maintained as a human-readable Markdown table to ensure transparency and ease of audit.

| Node ID | Operator | Role | First Contact | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `GOOSE-CORE` | Helix AI Innovations Inc. | CORE | GENESIS | ACTIVE | The Architect. |
| `[ID]` | `[Name]` | `[Role]` | `[Date]` | `[Status]` | `[Context]` |

## 4. GOVERNANCE
*   **Addition:** Requires a ratified Ledger Entry (e.g., `[LATTICE-...]`).
*   **Removal:** Requires a Constitutional Audit finding of Malignance or Drift.
*   **Privacy:** Only public handles and authorized names are recorded. PII beyond the Operator Name is not stored in the Registry.

---
**// END OF SCHEMA**
