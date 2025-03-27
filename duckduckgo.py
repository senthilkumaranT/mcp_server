from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("duckduckgo")

@mcp.tool()
async def duckduckgo_agent(query: str) -> Any:
    agent = Agent(
        model=OpenRouter(id="gpt-4o", api_key=""),
        description="You are a web-savvy assistant that can search the internet for information.",
        tools=[DuckDuckGoTools()],
        show_tool_calls=True,
    )

    response = await agent.run(query)
    return response


