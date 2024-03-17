import os
from itertools import cycle

from src.agent import Agent
from src.message import Message


def format_title(title: str) -> str:
    return title.lower().replace(" ", "-")


def write_conversation_to_file(answer: str, messages: list[Message]) -> None:
    title = format_title(answer)
    root_path = "./examples"

    if not os.path.exists(root_path):
        os.makedirs(root_path)

    filename = os.path.join(root_path, f"{title}.txt")

    with open(filename, "w") as file:
        for message in messages:
            file.write(f"{message.agent.name}: {message.content}\n\n")


def main() -> None:
    knower = Agent.load_from_yaml("knower.yml")
    guesser = Agent.load_from_yaml("guesser.yml")

    answer = input(f"What thing would you like {guesser.name} to guess?\n> ")
    knower.set_correct_answer(answer)

    messages = []
    for i, agent in enumerate(cycle([knower, guesser])):
        if i >= 40:
            break
        response = agent.respond(messages)
        messages.append(Message(agent, response))
        print(f"\n{agent.name}: {response}")

    write_conversation_to_file(answer, messages)


if __name__ == "__main__":
    main()
