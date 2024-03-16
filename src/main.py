from src.agent import Agent
from src.message import Message


def main() -> None:
    asker = Agent.load_from_yaml("asker.yml")
    guesser = Agent.load_from_yaml("guesser.yml")
    agents = [guesser, asker]

    asker.set_correct_answer(
        input("What thing would you like the Asker to be thinking of?")
    )

    messages = []
    for i in range(1, 40):
        agent = agents[i % 2]
        response = agent.respond(messages)
        messages.append(Message(agent, response))
        print(f"{agent.name}: {response}")


if __name__ == "__main__":
    main()
