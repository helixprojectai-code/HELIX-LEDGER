# ~/helix_ledger/modules/bitcoin/pricing_engine_v3.py
# Implements HCS-01 compliance and Dynamic Fee-Band Protection.

import datetime
import json
import os
import re
from typing import Optional, Dict, Any

# NOTE: This module requires the 'requests' library.
# pip install requests
import requests

class PricingEngineV3:
    MARKER_COSTS = {
        "[FACT]": 15,
        "[REASONED]": 10,
        "[HYPOTHESIS]": 5,
        "[UNCERTAIN]": 0,
    }
    LOG_FILE = "audit_log.json"
    FEE_THRESHOLD_SAT_V_B = 50  # Corresponds to a high-fee environment
    FEE_API_URL = "https://mempool.space/api/v1/fees/recommended"

    def _get_marker(self, text: str) -> Optional[str]:
        """Extracts the Epistemic Marker from a cognitive output."""
        match = re.match(r"^\[(FACT|REASONED|HYPOTHESIS|UNCERTAIN)\]", text)
        return match.group(0) if match else None

    def is_network_congested(self) -> bool:
        """
        Checks if the current Bitcoin network fee exceeds the defined threshold.
        Returns True if congested, False otherwise.
        In case of an API error, it fails closed (returns True).
        """
        try:
            response = requests.get(self.FEE_API_URL, timeout=5)
            response.raise_for_status()  # Raises an exception for 4xx or 5xx status codes
            fees = response.json()
            # We check the 'halfHourFee' as a balanced measure of current network demand.
            current_fee = fees.get("halfHourFee", float('inf')) 
            print(f"DEBUG: Current network fee is {current_fee} sat/vB. Threshold is {self.FEE_THRESHOLD_SAT_V_B} sat/vB.")
            return current_fee > self.FEE_THRESHOLD_SAT_V_B
        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"ERROR: Could not retrieve network fees. Failing closed. Reason: {e}")
            return True # Fail-closed

    def process_action(self, cognitive_output: str, target_action: str, action_details: Dict[str, Any]):
        """
        Processes a cognitive output, checks network fees, and logs the action
        if the network is not congested.
        """
        # [HYPOTHESIS] Assumption: Checking for congestion before processing is a valid safety measure.
        if self.is_network_congested():
            print("[UNCERTAIN]: Network fee exceeds threshold or API is unreachable. Pausing non-critical transactions.")
            # In a real implementation, this would halt further action.
            return

        marker = self._get_marker(cognitive_output)
        if not marker:
            return

        cost = self.MARKER_COSTS.get(marker, 0)
        
        log_entry = {
            "Timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
            "Epistemic Marker Detected": marker,
            "Target Action": target_action,
            "Action Details": action_details,
            "Cost": cost
        }

        with open(self.LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + os.linesep)
            
        print(f"HCS-01 LOG: {marker} | {target_action} | Cost: {cost} sats")

# --- Example Usage ---
if __name__ == "__main__":
    engine = PricingEngineV3()
    print("--- Running HCS-01 Pricing Engine V3 Simulation ---")
    
    # --- SCENARIO 1: Normal Operation (Low Fees) ---
    print("
--- SCENARIO 1: Fees are low, action is processed. ---")
    output1 = "[FACT] Committing new safety module to the repository."
    action1 = {"tool": "developer__shell", "command": "git commit..."}
    engine.process_action(output1, "shell", action1)

    # --- SCENARIO 2: High Fee Simulation ---
    print("
--- SCENARIO 2: Simulating high fees, action is blocked. ---")
    engine.FEE_THRESHOLD_SAT_V_B = 0 # Force the threshold to be lower than the fee
    output2 = "[REASONED] This transaction is not critical and should be paused."
    action2 = {"tool": "mcp_zgnz7abg__pay_invoice", "invoice": "..."}
    engine.process_action(output2, "payment", action2)
