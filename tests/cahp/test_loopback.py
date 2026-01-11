#!/usr/bin/env python3
import json
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../modules/cahp')))
from cahp_engine_v1 import CAHPEngine

def network_sim(message: dict) -> dict:
    return json.loads(json.dumps(message))

def test_loopback():
    print("Testing CAHP v1.0.0 Network Loopback...")
    a = CAHPEngine("metabolic")
    b = CAHPEngine("open_weight")
    
    m1 = a.discovery()
    m1_net = network_sim(m1)
    v1 = b._verify(m1_net)
    
    m2 = b.proof_and_challenge(v1)
    m2_net = network_sim(m2)
    v2 = a._verify(m2_net)
    
    m3 = a.response_and_final(v2)
    m3_net = network_sim(m3)
    v3 = b._verify(m3_net)
    
    ticket = b.ticket(v3)
    assert ticket is not None
    print("✓ Loopback test passed")

if __name__ == "__main__":
    test_loopback()
