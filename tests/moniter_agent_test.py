"""
Test Script for Monitor Agent
-----------------------------
Drop a file (PDF, PNG, JPG) into the `data/incoming/` folder and
watch this script print the structured JSON output.

Usage:
    python run_monitor_test.py
"""

import os
import sys
import json

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from agents.monitor_agent import start_folder_monitor

TEST_FOLDER = "C:/Users/ravin/Desktop/Agentic AI/Invoice-Auditing-Agent/data/incoming"

if __name__ == "__main__":
    print("🧠 Monitor Agent Test Started...")
    print(f"Watching folder: {TEST_FOLDER}")
    print("Drop a PDF/JPG/PNG file into the folder to trigger events.\n")

    for event_data in start_folder_monitor(TEST_FOLDER):
        print("\n📦 [New File Detected]")
        print(json.dumps(event_data, indent=2))
