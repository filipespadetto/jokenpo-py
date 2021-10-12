import random

def rules():
    print("\nRemember:"
          "\nScissors beats paper"
          "\nPaper beats rock"
          "\nRock beats scissors"
          "\nEqual elements will tie!")

def game():
    elements = ["r", "s", "p"]
    u_choice = input("\nYour turn! Enter r for rock, s for scissors or p for paper: ")
    m_choice = random.choice(elements)

    if u_choice == "s" and m_choice == "p":
        print("You: scissors \nMachine: paper")
        print("You win!")
    elif u_choice == "p" and m_choice == "s":
        print("You: paper \nMachine: scissors")
        print("You lose!")
    elif u_choice == 'p' and m_choice == 'r':
        print("You: paper \nMachine: rock")
        print("You win!")
    elif u_choice == 'r' and m_choice == 'p':
        print("You: rock \nMachine: paper")
        print("You lose!")
    elif u_choice == "r" and m_choice == "s":
        print("You: rock \nMachine: scissors")
        print("You win!")
    elif u_choice == "s" and m_choice == "r":
        print("You: scissors \nMachine: rock")
        print("You lose!")
    else:
        print(u_choice)
        print(m_choice)
        print("Tie")

if __name__ == '__main__':
    print("Welcome to the rock scissors paper game!")
    while True:
        menu = int(input("Press \n1 to play the game\n2 to read the rules\n3 to quit the game\nChoose: "))
        if menu == 1:
            game()
            print()

        elif menu == 2:
            rules()
            print()

        elif menu == 3:
            print("Goodbye, friend :(")
            break

        else:
            print("Sorry, I didn't understand. Try again!")
            print()