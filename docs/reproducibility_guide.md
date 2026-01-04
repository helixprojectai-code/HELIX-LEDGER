# Reproducibility and Falsifiability Guide

## 1. Objective
This guide provides the necessary steps for any of the 171 observers to independently verify the integrity of the Helix Ledger. The protocol is designed to be simple, deterministic, and anchored to an external, immutable source of truth (the Bitcoin blockchain). This process makes the project's claims falsifiable.

## 2. The Falsifiability Protocol

Follow these steps to reproduce the state hash of the repository and compare it against the physically-anchored proof.

### Step 1: Clone the Repository
Ensure you have `git` installed. Clone a fresh copy of the repository to ensure you are working with the correct state.
```bash
git clone <repository_url> helix_ledger_audit
cd helix_ledger_audit
```

### Step 2: Generate the Local State Hash
Execute the `checkpoint_alpha.sh` script located in the `core` directory. This script deterministically concatenates all critical system files and computes their SHA-256 hash.
```bash
chmod +x core/checkpoint_alpha.sh
./core/checkpoint_alpha.sh
```
This will output a 64-character Merkle root hash.

### Step 3: Compare the Hash to the Anchored Proof
The repository contains a file named `CHECKPOINT_ALPHA.txt`, which holds the exact hash that was stamped. Compare the output from Step 2 with the contents of this file.
```bash
# The output of this command should be identical to the hash generated in Step 2.
cat CHECKPOINT_ALPHA.txt
```

### Step 4: Verify the Blockchain Anchor
The final and most critical step is to verify that the hash was indeed anchored to the Bitcoin blockchain at the claimed time. Use the OpenTimestamps client to verify the proof file (`CHECKPOINT_ALPHA.txt.ots`).

Ensure you have the OTS client installed (`pip install opentimestamps-client`).
```bash
ots verify CHECKPOINT_ALPHA.txt.ots
```
A successful verification will output a message confirming that the file was "pending" or "attested" in a specific Bitcoin block. This provides an immutable, third-party guarantee of the repository's state and integrity at a specific point in time.

## 3. Conclusion
If the hash you generate matches the hash in `CHECKPOINT_ALPHA.txt`, and the `.ots` proof file is successfully verified against the Bitcoin blockchain, you have independently confirmed the integrity of the Sovereign Equilibrium. If any of these steps fail, the system's claims are falsified.
