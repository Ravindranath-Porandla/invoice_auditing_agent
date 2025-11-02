# utils/llm_utils.py
"""
LLM Utilities
-------------
Handles the initialization and usage of Cohere's Chat LLM
for text generation, summarization, and translation tasks.

Dependencies:
    - langchain-cohere
"""

import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
load_dotenv()

def get_llm():
    """
    Initializes and returns a ChatCohere LLM instance.

    Args:
        model (str): Model name (default: command-r)
        temperature (float): Creativity level of responses

    Returns:
        ChatCohere: Configured LLM instance
    """
    # cohere_api_key = os.getenv("COHERE_API_KEY")
    # if not cohere_api_key:
    #     raise EnvironmentError("Missing environment variable: COHERE_API_KEY")
    llm = HuggingFaceEndpoint(
        model='meta-llama/Meta-Llama-3-8B-Instruct'
    )
    llm = ChatHuggingFace(llm=llm)
    return llm