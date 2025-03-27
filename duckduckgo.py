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
        model=OpenRouter(id="gpt-4o", api_key="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"),
        description="You are a web-savvy assistant that can search the internet for information.",
        tools=[DuckDuckGoTools()],
        show_tool_calls=True,
    )

    response = await agent.run(query)
    return response


