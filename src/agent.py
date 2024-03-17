import os

import yaml
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

from src.message import Message

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


class Agent(BaseModel):
    """
    An AI agent that can play twenty questions against another agent.
    The configuration for the asker and guesser agents is loaded from YAML files in the data directory.
    """

    name: str
    system_prompt: str

    def respond(self, messages: list[Message]) -> str:
        prompt = {
            "model": "gpt-4",
            "messages": self.subjective_conversation_history(messages),
        }
        response = client.chat.completions.create(**prompt)
        return response.choices[0].message.content

    def subjective_conversation_history(self, messages: list[Message]) -> list[dict]:
        """
        Creates a conversation history from the agent's perspective.
        The agent's own past messages are marked as "assistant" and the other player's messages are marked as "user".
        The message history starts with the system prompt of the current agent only.
        In this way the other agent doesn't know the correct answer.
        """

        conversation_history = [{"role": "system", "content": self.system_prompt}]
        for message in messages:
            role = "assistant" if message.agent is self else "user"
            conversation_history.append({"role": role, "content": message.content})
        return conversation_history

    def set_correct_answer(self, answer: str) -> None:
        self.system_prompt = (
            f"{self.system_prompt}\n\nThe object you are thinking of is {answer}"
        )

    @staticmethod
    def load_from_yaml(filename: str) -> "Agent":
        with open(f"./data/agents/{filename}", "r") as file:
            data = yaml.safe_load(file)
        return Agent.parse_obj(data)
