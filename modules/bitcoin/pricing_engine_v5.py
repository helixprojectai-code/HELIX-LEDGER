# ~/helix_ledger/modules/bitcoin/pricing_engine_v5.py
# Implements all safety features with robust newline handling.

import datetime
import json
import os
import re
import sys
from typing import Optional, Dict, Any

import requests

class PricingEngineV5:
    MARKER_COSTS = {"[FACT]": 15, "[REASONED]": 10, "[HYPOTHESIS]": 5, "[UNCERTAIN]": 0}
    LOG_FILE = "audit_log.json"
    FEE_THRESHOLD_SAT_V_B = 50
    FEE_API_URL = "https://mempool.space/api/v1/fees/recommended"
    FUEL_RUNWAY_THRESHOLD = 8000

    def __init__(self, current_balance_sats: int):
        self.current_balance_sats = current_balance_sats

    def _get_marker(self, text: str) -> Optional[str]:
        match = re.match(r"^\[(FACT|REASONED|HYPOTHESIS|UNCERTAIN)\]", text)
        return match.group(0) if match else None

    def is_network_congested(self) -> bool:
        try:
            response = requests.get(self.FEE_API_URL, timeout=5)
            response.raise_for_status()
            fees = response.json()
            current_fee = fees.get("halfHourFee", float('inf'))
            print(f"DEBUG: Current network fee is {current_fee} sat/vB.")
            return current_fee > self.FEE_THRESHOLD_SAT_V_B
        except requests.exceptions.RequestException as e:
            print(f"ERROR: Could not retrieve network fees. Failing closed. Reason: {e}")
            return True

    def check_fuel_runway(self):
        if self.current_balance_sats < self.FUEL_RUNWAY_THRESHOLD:
            print("[EM-4: SPECULATIVE] Low Fuel Warning. Research liveness at risk.")
            
    def process_action(self, cognitive_output: str, target_action: str, action_details: Dict[str, Any]):
        self.check_fuel_runway()

        if self.is_network_congested():
            print("[UNCERTAIN]: Network fee exceeds threshold. Pausing.")
            return

        marker = self._get_marker(cognitive_output)
        if not marker: return

        cost = self.MARKER_COSTS.get(marker, 0)
        log_entry = {
            "Timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
            "Epistemic Marker Detected": marker,
            "Target Action": target_action,
            "Action Details": action_details,
            "Cost": cost,
            "Balance After (simulated)": self.current_balance_sats - cost
        }
        with open(self.LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + os.linesep)
        print(f"HCS-01 LOG: {marker} | {target_action} | Cost: {cost} sats")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit("Usage: python pricing_engine_v5.py <current_balance_sats>")
    try:
        balance = int(sys.argv[1])
    except ValueError: sys.exit("Error: Invalid balance provided.")

    engine = PricingEngineV5(current_balance_sats=balance)
    print(f"--- Running HCS-01 Pricing Engine V5 Simulation with Balance: {balance} sats ---")

    # SCENARIO 1: Normal Operation
    print() # Robust newline
    print("--- SCENARIO 1: Balance is sufficient, action is processed. ---")
    engine.process_action("[FACT] Committing new fuel safety module.", "shell", {"tool": "developer__shell", "command": "git commit..."})
    
    # SCENARIO 2: Low Fuel Simulation
    print() # Robust newline
    print("--- SCENARIO 2: Simulating low fuel, warning is triggered. ---")
    engine.current_balance_sats = 7500
    engine.process_action("[REASONED] The next action may deplete reserves.", "payment", {"tool": "mcp_zgnz7abg__pay_invoice", "invoice": "..."})
