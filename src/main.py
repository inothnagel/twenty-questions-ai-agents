from itertools import cycle

from src.agent import Agent
from src.message import Message


def main() -> None:
    knower = Agent.load_from_yaml("knower.yml")
    guesser = Agent.load_from_yaml("guesser.yml")
    agents = [knower, guesser]

    knower.set_correct_answer(
        input("What thing would you like the Asker to be thinking of?")
    )

    messages = []
    for i, agent in enumerate(cycle(agents)):
        if i >= 40:
            break
        response = agent.respond(messages)
        messages.append(Message(agent, response))
        print(f"{agent.name}: {response}")


if __name__ == "__main__":
    main()
