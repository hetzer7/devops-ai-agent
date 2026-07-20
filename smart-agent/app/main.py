from agent import Agent

agent = Agent()

print("=" * 50)
print(" Smart Agent v1.0")
print("=" * 50)
print("exit 입력 시 종료됩니다.\n")

while True:

    question = input("You > ")

    if question.lower() == "exit":
        break

    answer = agent.ask(question)

    print()
    print("AI >", answer)
    print()