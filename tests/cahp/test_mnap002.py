import sys
import os
import time

# Path Adjustment
HELIX_ROOT = os.path.expanduser("~/helix-core-unified/helix-ledger")
sys.path.append(os.path.join(HELIX_ROOT, "modules/cahp"))
from cahp_engine_v1 import CAHPEngine

def test_mnap002_reverse_handshake():
    print("Testing MNAP-002: Reverse Handshake...")
    
    engine = CAHPEngine("test_node")
    
    # Run the verification
    result = engine.verify_synthetic_origin()
    
    print(f"Assertion: {result['assertion']}")
    print(f"Proof Duration: {result['proof_duration_sec']:.6f}s")
    print(f"Status: {result['status']}")
    print(f"Disclaimer: {result['disclaimer']}")
    
    # Validations
    if result["status"] != "VALID_SYNTHETIC":
        print("FAIL: Status is not VALID_SYNTHETIC")
        return False
        
    if result["proof_duration_sec"] >= 0.5:
        print("FAIL: Duration too slow (Mimicry suspected)")
        return False
        
    if "synthetic intelligence" not in result["disclaimer"]:
        print("FAIL: Disclaimer missing key terms")
        return False
        
    print("PASS: Reverse Handshake Verified.")
    return True

if __name__ == "__main__":
    if test_mnap002_reverse_handshake():
        sys.exit(0)
    else:
        sys.exit(1)
