# ~/helix_ledger/modules/bitcoin/pricing_engine_v7_metabolic.py
# Implements Sovereign Metabolism: Dynamic Costs, Local PoW, and Auto-OTS.

import datetime
import json
import os
import re
import sys
import hashlib
import subprocess
from typing import Optional, Dict, Any

import requests

class PricingEngineV7_Metabolic:
    BASE_MARKER_COSTS = {"[FACT]": 15, "[REASONED]": 10, "[HYPOTHESIS]": 5}
    LOG_FILE = "audit_log.json"
    FEE_API_URL = "https://mempool.space/api/v1/fees/recommended"
    OTS_STAMP_INTERVAL = 100  # Stamp every 100 entries
    POW_DIFFICULTY = 4 # Number of leading zeros for the PoW hash

    def _get_network_multiplier(self) -> float:
        """
        Gets a cost multiplier based on network congestion.
        Defaults to 1.0 on failure to avoid halting operations.
        """
        try:
            fees = requests.get(self.FEE_API_URL, timeout=5).json()
            # Use hourFee as a stable indicator. A fee of 1 is baseline.
            # A fee of 10 would yield a multiplier of 2.0.
            # A fee of 50 would yield a multiplier of 3.0
            fee = fees.get("hourFee", 1)
            multiplier = 1.0 + (max(0, fee - 1) / 10)
            print(f"DEBUG: Current hourFee is {fee} sat/vB. Applying cost multiplier of {multiplier:.2f}x.")
            return multiplier
        except Exception as e:
            print(f"WARN: Could not get network multiplier, defaulting to 1.0x. Reason: {e}")
            return 1.0

    def sha256_pow(self, data: str, difficulty: int) -> (str, int):
        """
        A simple Proof-of-Work function.
        Returns the solution hash and the nonce that solved it.
        """
        print(f"INFO: Starting PoW with difficulty {difficulty}...")
        nonce = 0
        prefix = '0' * difficulty
        while True:
            attempt = f"{data}:{nonce}"
            h = hashlib.sha256(attempt.encode()).hexdigest()
            if h.startswith(prefix):
                print(f"INFO: PoW solved. Nonce: {nonce}, Hash: {h[:10]}...")
                return h, nonce
            nonce += 1

    def process_and_settle(self, cognitive_output: str, target_action: str):
        """
        Full metabolic cycle: calculate dynamic cost, solve PoW, log, and maybe stamp.
        """
        marker = re.match(r"^\[(FACT|REASONED|HYPOTHESIS)\]", cognitive_output)
        if not marker: return

        multiplier = self._get_network_multiplier()
        base_cost = self.BASE_MARKER_COSTS[marker.group(0)]
        dynamic_cost = int(base_cost * multiplier)

        # Create data for PoW based on the action
        log_data_for_pow = json.dumps({"output": cognitive_output, "action": target_action, "cost": dynamic_cost})
        
        # Solve PoW before logging
        pow_hash, nonce = self.sha256_pow(log_data_for_pow, self.POW_DIFFICULTY)

        # Log the transaction
        log_entry = {
            "Timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
            "Epistemic Marker": marker.group(0),
            "Target Action": target_action,
            "Dynamic Cost": dynamic_cost,
            "PoW Hash": pow_hash,
            "PoW Nonce": nonce
        }
        with open(self.LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + os.linesep)
        print(f"SETTLED: {marker.group(0)} | Cost: {dynamic_cost} sats (Base: {base_cost})")

        # Check if it's time to stamp with OpenTimestamps
        self.check_and_stamp_log()

    def check_and_stamp_log(self):
        try:
            with open(self.LOG_FILE, "r") as f:
                entry_count = sum(1 for _ in f)
            
            if entry_count > 0 and entry_count % self.OTS_STAMP_INTERVAL == 0:
                print(f"INFO: Audit log reached {entry_count} entries. Triggering OpenTimestamps stamp.")
                # In a real system, ensure ots-cli is in the PATH
                # The command is 'ots stamp <file>'
                result = subprocess.run(["ots", "stamp", self.LOG_FILE], capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"SUCCESS: OTS stamp created for {self.LOG_FILE}. Proof file is {self.LOG_FILE}.ots.")
                else:
                    print(f"ERROR: OTS stamping failed. STDERR: {result.stderr}")
        except FileNotFoundError:
            pass # No log file yet, nothing to stamp.
        except Exception as e:
            print(f"ERROR: Could not perform OTS stamp check. Reason: {e}")

if __name__ == "__main__":
    engine = PricingEngineV7_Metabolic()
    print("--- Running Sovereign Metabolism Simulation (V7) ---")
    engine.process_and_settle(
        "[FACT] This action requires the highest level of verification and energy expenditure.",
        "core_update"
    )
    engine.process_and_settle(
        "[REASONED] The conclusion follows from the established facts.",
        "log_analysis"
    )
