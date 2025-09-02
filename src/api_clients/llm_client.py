from google import genai
from src.utils.logger import logger
import os
import datetime
from src.utils.util import parse_time_from_message
from src.exception.exception_handler import catch_exceptions, catch_async_exceptions, run_safe


class GeminiClient:
    def __init__(self, api_key=None):
        logger.debug("Initializing GeminiClient")
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)

    @catch_exceptions
    def ask(self, prompt: str) -> str:
        """
        Simple conversational mode — just chat.
        """
        logger.debug(f"Asking Gemini (conversational): {prompt}")
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text

    def _clean(self, s: str) -> str:
        return (s or "").strip().strip("<>").strip()

    @catch_exceptions
    def run_agent(self, query: str, tools: dict) -> str:
        """
        Agentic mode — Gemini decides whether to use tools or just reply.
        Pass chat_id via tools["_chat_id"].
        tools must include callables for any tool names the model may emit.
        """
        logger.debug(f"Running Gemini Agent on: {query}")

        system_prompt = (
            "You are a helpful assistant. "
            "If the user asks about health symptoms, respond exactly with: TOOL:symptom_check|<symptoms>. "
            "If they mention reminders, respond exactly with: TOOL:add_reminder|<message with timing>. "
            "If they send an image, respond exactly with: TOOL:food_scan|<image_path>. "
            "Otherwise, reply naturally.\n\n"
        )

        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=system_prompt + f"User: {query}"
        )

        text = (response.text or "").strip()
        logger.debug(f"Gemini raw response: {text}")

        # Tool invocation path
        if text.startswith("TOOL:"):
            tool_call = text.split("TOOL:", 1)[1].strip()
            tool_name, tool_input = tool_call.split("|", 1)
            tool_name = self._clean(tool_name)
            tool_input = self._clean(tool_input)

            if tool_name not in tools:
                return f"(Unknown tool: {tool_name})"

            # Special handling for reminders
            if tool_name == "add_reminder":
                chat_id = tools.get("_chat_id")
                if chat_id is None:
                    return "(Agent error: chat_id missing for reminders)"

                remind_at = parse_time_from_message(tool_input)  # UTC aware
                if remind_at.tzinfo is None:
                    remind_at = remind_at.replace(tzinfo=datetime.timezone.utc)

                logger.info(
                    f"Agent calling tool: {tool_name} with message '{tool_input}' at {remind_at.isoformat()}"
                )
                return tools[tool_name](chat_id, tool_input, remind_at)

            logger.info(f"Agent calling tool: {tool_name} with input {tool_input}")
            return tools[tool_name](tool_input)

        return text
