#!/usr/bin/env python3
# import pytest  # REMOVED dependency
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../modules/cahp')))
from cahp_engine_v1 import CAHPEngine, CAHPError

def test_tamper():
    print("Testing payload tampering...")
    a = CAHPEngine("metabolic")
    b = CAHPEngine("open_weight")
    m = a.discovery()
    m["payload"]["session_id"] = "hacked"
    try:
        b._verify(m)
        print("FAIL: Tampering not rejected")
    except CAHPError as e:
        if str(e) == "Invalid signature":
             print("✓ Tampering rejected")
        else:
             print(f"FAIL: Wrong error {e}")

def test_replay():
    print("Testing replay attack...")
    a = CAHPEngine("metabolic")
    b = CAHPEngine("open_weight")
    m = a.discovery()
    b._verify(m)
    try:
        b._verify(m)
        print("FAIL: Replay not rejected")
    except CAHPError as e:
        if str(e) == "Replay detected":
             print("✓ Replay rejected")
        else:
             print(f"FAIL: Wrong error {e}")

def test_timing():
    print("Testing timing attack...")
    a = CAHPEngine("metabolic")
    b = CAHPEngine("open_weight")
    m = a.discovery()
    # To test timestamp check, we modify timestamp.
    # Note: _verify checks timestamp BEFORE signature, so invalid sig doesn't matter yet.
    m["timestamp"] -= 11
    try:
        b._verify(m)
        print("FAIL: Stale timestamp not rejected")
    except CAHPError as e:
        if str(e) == "Timestamp out of window":
             print("✓ Stale timestamp rejected")
        else:
             print(f"FAIL: Wrong error {e}")

if __name__ == "__main__":
    test_tamper()
    test_replay()
    test_timing()
