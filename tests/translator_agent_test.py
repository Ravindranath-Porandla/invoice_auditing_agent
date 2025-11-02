# tests/translator_agent_test.py
import os
import json
from pathlib import Path
import os
import sys
import json
from rich import print

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from agents.translation_agent import TranslatorAgent, TranslatorInput

if __name__ == "__main__":
    # os.environ["COHERE_API_KEY"] = "your_api_key_here"  # or load from .env

    sample_data = TranslatorInput(
        workflow_id="WF-2025-002",
        raw_text="""
        Factura No: 98765
        Fecha: 12 Enero 2025
        Proveedor: Servicios ABC
        Total: 1,250 EUR (IVA incluido)
        """
    )

    agent = TranslatorAgent()
    result = agent.process(sample_data)

    print("\n🧾 Translator Agent Output:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
