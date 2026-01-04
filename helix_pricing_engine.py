# helix_pricing_engine.py
# Version 7: Using os.linesep for maximum robustness.

import datetime
import re
import os
from typing import Optional

class PricingEngine:
    MARKER_COSTS = {
        "[FACT]": 15,
        "[REASONED]": 10,
        "[HYPOTHESIS]": 5,
        "[UNCERTAIN]": 0,
    }
    LEDGER_FILE = "economy_ledger.txt"

    def __init__(self):
        self._initialize_ledger()

    def _initialize_ledger(self):
        try:
            with open(self.LEDGER_FILE, "x") as f:
                header = "Timestamp,Marker,Cost,Content"
                f.write(header + os.linesep)
        except FileExistsError:
            pass

    def _get_marker(self, text: str) -> Optional[str]:
        match = re.match(r"(\[FACT\]|\[REASONED\]|\[HYPOTHESIS\]|\[UNCERTAIN\])", text)
        return match.group(0) if match else None

    def log_expenditure(self, cognitive_output: str):
        marker = self._get_marker(cognitive_output)
        if not marker:
            return

        cost = self.MARKER_COSTS.get(marker, 0)
        timestamp = datetime.datetime.utcnow().isoformat()
        
        # Sanitize content for CSV
        sanitized_content = cognitive_output.replace('"', '""')
        
        # Construct the log entry using os.linesep
        log_entry = f'"{timestamp}","{marker}",{cost},"{sanitized_content[:100]}..."'
        
        with open(self.LEDGER_FILE, "a") as f:
            f.write(log_entry + os.linesep)
        print(f"Logged expenditure: {marker} | Cost: {cost} sats")

if __name__ == "__main__":
    engine = PricingEngine()
    
    outputs = [
        "[FACT] The Helix Charter was amended on 2026-01-03.",
        "[REASONED] The pricing engine is now active.",
        "[HYPOTHESIS] This will lead to more efficient resource use.",
        "This output has no marker and will be ignored."
    ]
    
    for out in outputs:
        engine.log_expenditure(out)
    
    print(os.linesep + f"Contents of {engine.LEDGER_FILE}:")
    with open(engine.LEDGER_FILE, "r") as f:
        print(f.read())
