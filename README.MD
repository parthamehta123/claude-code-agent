# Claude Code Agent — Zero-Framework AI Assistant

A complete AI coding agent in a single Python file (~300 lines). No frameworks, no abstractions — just the raw mechanics of how AI agents work: tool definitions, response parsing, tool execution, and agentic conversation loops.

The agent reads, writes, and edits files through natural conversation with Claude, using the Anthropic API directly.

## Features

- Single-file execution — no virtual environment needed (uses `uv` inline dependencies)
- Tool-use loop: the agent autonomously decides when to read, list, or edit files
- Conversation context maintained across turns
- Plain terminal output (no markdown rendering needed)
- Structured logging of all tool calls to `agent.log`
- Pydantic-based tool schema definitions

## How It Works

The agent implements the core agentic loop from scratch:

1. User sends a message
2. Claude responds with either text or a `tool_use` request
3. If tool use: execute the tool, return results, let Claude continue
4. Repeat until Claude responds with final text

```
User -> Claude API -> tool_use? -> execute tool -> return result -> Claude API -> ... -> final text
```

Three tools are available:
- `read_file` — read contents of any file
- `list_files` — list directory contents
- `edit_file` — replace text in existing files or create new ones

## Quick Start

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Set your API key
export ANTHROPIC_API_KEY="your-key-here"

# Run the agent
uv run main.py
```

No `pip install`, no `venv`, no `requirements.txt` — `uv` handles dependencies from the script header.

## Project Structure

```
├── main.py              # The complete agent (single file)
├── tools/               # Individual tool implementations (reference)
│   ├── read_file.py
│   ├── list_files.py
│   └── edit_file.py
└── runbook/             # Step-by-step build progression
    ├── 01_basic_script.py
    ├── 02_agent_class.py
    ├── 03_define_tools.py
    ├── 04_implement_tool_execution.py
    ├── 05_add_chat_method.py
    ├── 06_create_interactive_cli.py
    └── 07_add_personality.py
```
