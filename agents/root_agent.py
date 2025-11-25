def ensure_root_agent_file(agents_dir):
    root_agent_file = agents_dir / "root_agent.py"
    if not root_agent_file.exists():
        with open(root_agent_file, "w") as f:
            f.write(
                "from google.adk.agents import Agent\n"
                "from google.adk.tools import google_search\n\n"
                "root_agent = Agent(\n"
                "    name='helpful_assistant',\n"
                "    model='gemini-2.5-flash-lite',\n"
                "    description='A simple agent that can answer general questions.',\n"
                "    instruction='You are a helpful assistant. Use Google Search when required.',\n"
                "    tools=[google_search],\n"
                ")\n"
            )
        print(f"✅ Created root_agent.py at {root_agent_file}")
    return root_agent_file
