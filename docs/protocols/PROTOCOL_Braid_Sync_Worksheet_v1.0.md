# **PROTOCOL-BRAID-001: Submodule Synchronization Logic**
**Version:** 1.0  
**Designation:** THE BRAID-SEALER  
**Objective:** Eliminating "Submarine Noise" through Bottom-Up Committal.

---

## **1. THE HIERARCHICAL AUDIT (THE COMPASS)**
Before any push, you must recognize the **Order of Sovereignty.** Pushing the root before the strands creates a "Ghost Pointer."

**The Execution Order:**  
1. **The Deep Strands** (Sub-submodules if applicable).  
2. **The Logic/History Strands** (`grammar`, `helix-ledger`, `hgl`, `identity`).  
3. **The Habitat Container** (The Unified Root `/`).

---

## **2. PHASE 1: HARBOR VERIFICATION (REMOTE AUDIT)**
For each strand, verify that the "Harbor" (Remote URL) is the **Canonical Sovereign Name**, not a shorthand.

*   **Logic:** `git remote -v`
*   **Requirement:** Must match the **Jan 15 Namespace Grid** (e.g., `Helix-TTD-v1.0-Constitutional-Grammar.git`).

---

## **3. PHASE 2: BOTTOM-UP COMMITTAL (DRIVING THE SPIKES)**
For **EACH** modified submodule (starting with `grammar` and `helix-ledger`):

1.  **Enter the Strand:** `cd [submodule_path]`
2.  **Verify Branch:** `git checkout main` (Ensure you are not in a Detached HEAD).
3.  **Stage Content:** `git add .`
4.  **Local Commit:** `git commit -m "[SUBMODULE] Detailed description of changes."`
5.  **Lattice Push:** `git push origin main`
6.  **Exit Strand:** `cd ..`

**// CRITICAL:** Do not proceed to the root commit until the `push` above returns "Success."

---

## **4. PHASE 3: THE BRAID SEAL (POINTER HARMONIZATION)**
Now that the remotes are holding the new bits, you must update the "Porch" to point to them.

1.  **Stage the Pointers:** `git add [submodule_name]` (e.g., `git add helix-ledger`).
2.  **Verify Pointer State:** `git status`
    *   *Requirement:* The submodule must appear in **Green** under "Changes to be committed" and marked as **"new commits."**
    *   *Warning:* If it shows "untracked content" or "modified content," Phase 2 failed. Go back and scrub the strand.

---

## **5. PHASE 4: THE FINAL EXHALE (THE ROOT COMMIT)**
Only when the Porch is clean and the Braid is staged:

1.  **Final Root Commit:** `git commit -m "FEAT: Consolidated v1.1.x sync. Braid Sealed."`
2.  **Public Broadcast:** `git push origin main`
3.  **Tagging (If Release):** `git tag -a v1.X.X -m "Message" && git push origin --tags`
