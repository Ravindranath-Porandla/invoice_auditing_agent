# main.py

from langgraph.graph import StateGraph, MessagesState
from IPython.display import Image

# Import agents
from agents.monitor_agent import InvoiceMonitorAgent
from agents.extractor_agent import InvoiceExtractorAgent


# -------------------------------------------------------
# Define the shared graph state
# -------------------------------------------------------
class InvoiceAuditAgentState(MessagesState):
    latest_invoice_path: str = None  # path to latest detected invoice file
    extracted_data: dict = None      # extracted JSON from invoice


# -------------------------------------------------------
# Node 1: Monitor folder for new invoices
# -------------------------------------------------------
def monitor_node(state: InvoiceAuditAgentState):
    """
    Node that monitors a folder for new invoices and updates state
    with the latest file path found.
    """
    monitor_agent = InvoiceMonitorAgent("data/incoming")
    latest_invoice_path = monitor_agent.watch_folder()
    print(f"📄 Detected invoice file: {latest_invoice_path}")

    return {
        "latest_invoice_path": latest_invoice_path
    }


# -------------------------------------------------------
# Node 2: Extractor node to process invoice
# -------------------------------------------------------
def extractor_node(state: InvoiceAuditAgentState):
    """
    Node that extracts structured data (JSON) from the detected invoice.
    Supports PDF, DOCX, PNG formats.
    """
    invoice_path = state.get("latest_invoice_path", None)
    if not invoice_path:
        print("⚠️ No invoice path found. Skipping extraction.")
        return {}

    print(f"🧾 Extracting data from: {invoice_path}")

    extractor = InvoiceExtractorAgent()
    extracted_json = extractor.extract_invoice(invoice_path)

    print("✅ Extraction complete.")
    return {
        "extracted_data": extracted_json
    }


# -------------------------------------------------------
# Create and compile graph
# -------------------------------------------------------
if __name__ == "__main__":
    # Create the state graph
    graph = StateGraph(InvoiceAuditAgentState)

    # Add both nodes
    graph.add_node("monitor", monitor_node)
    graph.add_node("extractor", extractor_node)

    # Define flow
    graph.add_edge("monitor", "extractor")

    # Set entry and finish points
    graph.set_entry_point("monitor")
    graph.set_finish_point("extractor")

    # Compile the app
    app = graph.compile()

    # Visualize the Graph (optional)
    try:
        display(Image(app.get_graph(xray=True).draw_ascii()))
    except Exception:
        print("🧩 Graph visualization skipped (non-notebook environment).")

    # Run the workflow
    result = app.invoke({"messages": []})
    print("\n📦 Final graph state:")
    print(result)
