import asyncio
from agent import root_agent

async def main():
    while True:
        user_input = input("You: ")
        response = await root_agent.run(user_input)
        print("AI:", response)

asyncio.run(main())