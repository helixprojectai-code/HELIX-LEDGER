#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../modules/cahp')))
from cahp_engine_v1 import CAHPEngine

def test_full_mutual():
    print("Testing CAHP v1.0.0 Full Mutual Handshake...")
    a = CAHPEngine("metabolic")
    b = CAHPEngine("open_weight")
    
    m1 = a.discovery()
    v1 = b._verify(m1)
    
    m2 = b.proof_and_challenge(v1)
    v2 = a._verify(m2)
    
    m3 = a.response_and_final(v2)
    v3 = b._verify(m3)
    
    ticket = b.ticket(v3)
    
    assert ticket is not None, "Mutual handshake failed: Ticket is None"
    print("✓ Full mutual handshake passed")
    
if __name__ == "__main__":
    test_full_mutual()
