from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from agent import Agent


@dataclass
class Message:
    agent: "Agent"
    content: str
