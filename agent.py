import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.langchain_tool import LangchainTool

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

import google.auth
import google.auth.transport.requests
import google.oauth2.id_token


# -------------------------------
# SETUP
# -------------------------------

cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()
model_name = "gemini-2.5-flash"

# -------------------------------
# DATABASE
# -------------------------------
from .database import add_task, save_note

# -------------------------------
# TOOLS
# -------------------------------

def add_prompt_to_state(tool_context: ToolContext, prompt: str):
    history = tool_context.state.get("history", [])
    history.append(prompt)

    tool_context.state["PROMPT"] = prompt
    tool_context.state["history"] = history

    return {"status": "saved"}


def task_tool(tool_context: ToolContext):
    prompt = tool_context.state.get("PROMPT", "")
    add_task(prompt)
    return f"✅ Task saved: {prompt}"


def calendar_tool(tool_context: ToolContext):
    prompt = tool_context.state.get("PROMPT", "")
    return f"📅 Event scheduled: {prompt}"


def notes_tool(tool_context: ToolContext):
    prompt = tool_context.state.get("PROMPT", "")
    save_note(prompt)
    return f"📝 Note saved: {prompt}"

def notes_analysis_tool(tool_context: ToolContext):
    prompt = tool_context.state.get("PROMPT", "")

    return f"""
You are an AI study assistant.

From the following notes:

{prompt}

Tasks:
1. Generate a clear summary
2. Create 5 important questions
3. Highlight key points

Format clearly.
"""



wikipedia_tool = LangchainTool(
    tool=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
)

# -------------------------------
# 1️⃣ RESEARCH AGENT (BRAIN)
# -------------------------------

research_agent = Agent(
    name="research_agent",
    model=model_name,
    description="Handles tasks, calendar events, notes, and knowledge queries intelligently",

    instruction="""
You are an intelligent multi-agent assistant.

Your job is to understand the user's intent and decide which tools to use.

Guidelines:
- If the user wants to remember or track something → use task_tool
- If the user mentions meetings, schedules, date, or time → use calendar_tool
- If the user wants to store or write information → use notes_tool
- If the user asks factual/general knowledge → use wikipedia_tool
- If user provides notes and asks to summarize or generate questions → use notes_analysis_tool

Important Rules:
- You can use MULTIPLE tools if needed
- Choose tools based on meaning, not just keywords
- Always act based on the PROMPT

PROMPT:
{ PROMPT }

HISTORY:
{ history }
""",

    tools=[
        task_tool,
        calendar_tool,
        notes_tool,
        wikipedia_tool,
        notes_analysis_tool
    ],

    output_key="research_data"
)
# -------------------------------
# 2️⃣ RESPONSE FORMATTER
# -------------------------------

response_formatter = Agent(
    name="response_formatter",
    model=model_name,
    description="Formats output nicely",
    instruction="""
You are a professional AI assistant.

Format the response clearly and neatly:

- Use bullet points
- Use emojis for clarity
- Keep it short and helpful

If multiple actions were performed:
- Separate each result clearly

Make the response easy to read and user-friendly.

RESEARCH_DATA:
{ research_data }
"""
)

# -------------------------------
# 3️⃣ WORKFLOW
# -------------------------------

workflow = SequentialAgent(
    name="multi_agent_workflow",
    description="Executes full workflow",
    sub_agents=[
        research_agent,
        response_formatter
    ]
)

# -------------------------------
# 4️⃣ ROOT AGENT
# -------------------------------

root_agent = Agent(
    name="root_agent",
    model=model_name,
    description="Entry point",
    instruction="""
    - Greet the user
    - Save input using add_prompt_to_state
    - Then pass to workflow
    """,
    tools=[add_prompt_to_state],
    sub_agents=[workflow]
)