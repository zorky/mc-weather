from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict

# from agent.agent import agent
from weather_tools import get_weather

app = FastAPI()

@app.get("/mcp/tools")
async def list_tools():
    # MCP veut un tableau de descriptions JSON
    import json
    with open("tools.json") as f:
        return JSONResponse(content=json.load(f))

class ToolCallRequest(BaseModel):
    name: str
    parameters: Dict

# async def call_tool(request: Request):

@app.post("/mcp/tool_call")
async def call_tool(request: ToolCallRequest):
    # payload = await request.json()
    # tool_name = payload.get("name")
    # params = payload.get("parameters", {})
    tool_name = request.name
    params = request.parameters
    if tool_name == "get_weather":
        # result = await get_weather(params.get("city", ""))
        result = get_weather(params.get("city", ""))
        return {"result": result}
    elif tool_name == "get_coordinates":
        from geo_tools import get_coordinates
        result = get_coordinates(params.get("city", ""))
        return {"result": result}
    else:
        return JSONResponse(status_code=400, content={"error": "Tool not found"})


# @app.get("/ask")
# async def ask_agent(question: str):
#     return {"response": agent.run(question)}