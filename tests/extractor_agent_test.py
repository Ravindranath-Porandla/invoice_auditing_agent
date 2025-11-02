"""
Simple test for ExtractorAgent using an image file.
Run:
    python tests/test_extractor_agent.py
"""

from pathlib import Path
import os
import sys
import json

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from agents.monitor_agent import start_folder_monitor
from agents.extractor_agent import ExtractorAgent

TEST_DIR = Path("data/incoming")



if __name__ == "__main__":
    sample_path = "C:\\Users\\ravin\\Desktop\\Agentic AI\\Invoice-Auditing-Agent\\data\\incoming\\INV_DE_004.pdf"

    payload = {
        "workflow_id": "WF-TEST-0001",
        "file_path": str(sample_path)
    }

    agent = ExtractorAgent()
    result = agent.process(payload)
    print(json.dumps(result, indent=2))
