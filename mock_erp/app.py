from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
import json
import uvicorn
import os

app = FastAPI(
    title="Mock ERP System",
    description="Mock ERP API for AI Invoice Auditor Project",
    version="1.0.0"
)

# -------------------------------------------------------------------
# Data Loading Utilities
# -------------------------------------------------------------------
DATA_DIR = os.path.dirname(__file__)

def load_json(file_name: str) -> List[Dict[str, Any]]:
    file_path = os.path.join(DATA_DIR, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Error loading {file_name}: {e}")

# Load all datasets once at startup
po_records = load_json("data/PO Records.json")
vendors = load_json("data/vendors.json")
sku_master = load_json("data/sku_master.json")

# Create lookup maps for quick access
po_index = {po["po_number"]: po for po in po_records}
vendor_index = {v["vendor_id"]: v for v in vendors}
sku_index = {sku["item_code"]: sku for sku in sku_master}


# -------------------------------------------------------------------
# Endpoints
# -------------------------------------------------------------------

@app.get("/")
async def root():
    return {"message": "Mock ERP API is running", "endpoints": ["/po/{po_number}", "/vendor/{vendor_id}", "/sku/{item_code}"]}


@app.get("/po/{po_number}")
async def get_po(po_number: str):
    """
    Retrieve purchase order details by PO number.
    Example: /po/PO-1001
    """
    po_data = po_index.get(po_number)
    if not po_data:
        raise HTTPException(status_code=404, detail=f"PO number {po_number} not found in ERP records.")
    return {"status": "success", "data": po_data}


@app.get("/vendor/{vendor_id}")
async def get_vendor(vendor_id: str):
    """
    Retrieve vendor information by vendor ID.
    Example: /vendor/VEND-001
    """
    vendor_data = vendor_index.get(vendor_id)
    if not vendor_data:
        raise HTTPException(status_code=404, detail=f"Vendor ID {vendor_id} not found in ERP records.")
    return {"status": "success", "data": vendor_data}


@app.get("/sku/{item_code}")
async def get_sku(item_code: str):
    """
    Retrieve SKU metadata by item code.
    Example: /sku/SKU-001
    """
    sku_data = sku_index.get(item_code)
    if not sku_data:
        raise HTTPException(status_code=404, detail=f"Item code {item_code} not found in SKU master.")
    return {"status": "success", "data": sku_data}


# -------------------------------------------------------------------
# Run locally (optional)
# -------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
