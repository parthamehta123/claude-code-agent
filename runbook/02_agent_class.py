# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "anthropic", # type: ignore
#     "pydantic",
# ]
# ///

import os
import sys
from typing import List, Dict, Any
from anthropic import Anthropic
from pydantic import BaseModel


class Tool(BaseModel):
    name: str
    description: str
    input_schema: Dict[str, Any]


class AIAgent:
    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)
        self.messages: List[Dict[str, Any]] = []
        self.tools: List[Tool] = []
        print("Agent initialized")


if __name__ == "__main__":
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set")
        sys.exit(1)
    agent = AIAgent(api_key)

# ```bash
# export ANTHROPIC_API_KEY="your-api-key-here"
# uv run runbook/02_agent_class.py
# ```
# Should print: Agent initialized
