# ~/helix_ledger/modules/bitcoin/pricing_engine_v2.py
# Implements HCS-01 compliant JSON logging.

import datetime
import json
import os
import re
from typing import Optional, Dict, Any

class PricingEngineV2:
    MARKER_COSTS = {
        "[FACT]": 15,
        "[REASONED]": 10,
        "[HYPOTHESIS]": 5,
        "[UNCERTAIN]": 0,
    }
    LOG_FILE = "audit_log.json"

    def _get_marker(self, text: str) -> Optional[str]:
        """Extracts the Epistemic Marker from a cognitive output."""
        match = re.match(r"^\[(FACT|REASONED|HYPOTHESIS|UNCERTAIN)\]", text)
        return match.group(0) if match else None

    def log_action(self, cognitive_output: str, target_action: str, action_details: Dict[str, Any]):
        """
        Logs a cognitive output and its associated action to the audit log
        in JSON Lines format, as per HCS-01.
        """
        marker = self._get_marker(cognitive_output)
        if not marker:
            # This would trigger EC-401 in a full implementation.
            return

        cost = self.MARKER_COSTS.get(marker, 0)
        
        # Create a log entry compliant with HCS-01 Section 5.
        log_entry = {
            "Timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
            "Epistemic Marker Detected": marker,
            "Target Action": target_action,
            "Action Details": action_details,
            "Cost": cost
        }

        # Append to the log file using JSON Lines format (one JSON object per line).
        with open(self.LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + os.linesep)
            
        print(f"HCS-01 LOG: {marker} | {target_action} | Cost: {cost} sats")

# --- Example Usage ---
if __name__ == "__main__":
    engine = PricingEngineV2()
    
    print("--- Running HCS-01 Pricing Engine Simulation ---")
    
    output1 = "[FACT] Creating core directory structure."
    action1 = {
        "tool": "developer__shell",
        "command": "mkdir -p ~/helix_ledger/core"
    }
    engine.log_action(output1, "shell", action1)

    output2 = "[REASONED] The pricing engine must be refactored for HCS-01 compliance."
    action2 = {
        "tool": "developer__text_editor",
        "command": "write",
        "path": "~/helix_ledger/modules/bitcoin/pricing_engine_v2.py"
    }
    engine.log_action(output2, "file_write", action2)

    output3 = "[HYPOTHESIS] Assumption: This new JSON format will be more robust for future parsing."
    action3 = {
        "tool": "developer__shell",
        "command": "git commit ..."
    }
    engine.log_action(output3, "shell", action3)

    print(os.linesep + f"--- Contents of {engine.LOG_FILE} ---")
    try:
        with open(engine.LOG_FILE, "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("Log file not created yet.")
