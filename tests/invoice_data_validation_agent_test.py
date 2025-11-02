import os
import sys
import json

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from agents.monitor_agent import start_folder_monitor
from agents.invoice_data_validation import ValidationAgent

def test_validation_agent():
    agent = ValidationAgent()

    invoice_data = {
        "workflow_id": "WF-2025-TEST",
        "header": {
            "invoice_no": "INV-1234",
            "invoice_date": "2025-10-31",
            "vendor_id": "V998",
            "currency": "USD",
            "total_amount": 2000.0
        },
        "line_items": [
            {"item_code": "P01", "description": "Laptop", "qty": 1, "unit_price": 1200.0, "total": 1200.0},
            {"item_code": "P02", "description": "Keyboard", "qty": 4, "unit_price": 200.0, "total": 800.0}
        ]
    }

    result = agent.validate(invoice_data)
    print(json.dumps(result, indent=2))
    assert "status" in result
    assert "discrepancies" in result

if __name__ == "__main__":
    test_validation_agent()
