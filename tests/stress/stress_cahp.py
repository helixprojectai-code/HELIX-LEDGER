"""
Stress Test for CAHP v1.0.0
MNAP-002 High Frequency Validation
"""

import sys
import os
import time
import threading
import statistics
from queue import Queue

# Add root to path
sys.path.append(os.path.expanduser("~/helix-core-unified/helix-ledger/modules/cahp"))
from cahp_engine_v1 import CAHPEngine

RESULTS = Queue()

def worker(worker_id):
    try:
        engine = CAHPEngine(f"worker_{worker_id}")
        start_time = time.perf_counter()
        
        # 1. Reverse Handshake
        origin = engine.verify_synthetic_origin()
        
        # 2. Discovery (Simulate full handshake init)
        msg1 = engine.discovery()
        
        duration = (time.perf_counter() - start_time) * 1000 # ms
        
        success = (origin["status"] == "VALID_SYNTHETIC")
        RESULTS.put({"id": worker_id, "success": success, "duration": duration})
        
    except Exception as e:
        RESULTS.put({"id": worker_id, "success": False, "error": str(e)})

def run_stress_test(concurrency=50):
    print(f"--- Starting Stress Test (Concurrency: {concurrency}) ---")
    threads = []
    
    start_global = time.perf_counter()
    
    for i in range(concurrency):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    end_global = time.perf_counter()
    total_time = end_global - start_global
    
    results_list = []
    while not RESULTS.empty():
        results_list.append(RESULTS.get())
        
    successes = [r for r in results_list if r.get("success")]
    failures = [r for r in results_list if not r.get("success")]
    
    durations = [r["duration"] for r in successes]
    
    print(f"Total Time: {total_time:.4f}s")
    print(f"Throughput: {concurrency/total_time:.2f} handshakes/sec")
    print(f"Success Rate: {len(successes)}/{concurrency} ({len(successes)/concurrency*100:.1f}%)")
    
    if durations:
        print(f"Latency (Avg): {statistics.mean(durations):.2f}ms")
        print(f"Latency (Max): {max(durations):.2f}ms")
        print(f"Latency (Min): {min(durations):.2f}ms")
        
    if failures:
        print("Failures detected:")
        for f in failures[:5]:
            print(f"  Worker {f['id']}: {f.get('error', 'Unknown')}")

if __name__ == "__main__":
    run_stress_test(50)
