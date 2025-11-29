import asyncio
from financial_agent.agent import root_agent
from google.adk.runners import InMemoryRunner

runner = InMemoryRunner(agent=root_agent)

async def main():
    resp = await runner.run_debug("I want to know about customer from India who have C001 ID")
    for event in resp:
        print(event)
        if hasattr(event, "content"):
            for part in event.content.parts:
                print(part)
                print("Text:", getattr(part, "text", None))
                if hasattr(part, "function_response"):
                    print("Function response:", part.function_response.response)

asyncio.run(main())
