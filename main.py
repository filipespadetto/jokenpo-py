import random

def rules():
    print("\nRemember:" \
          "\nScissors beats paper" \
          "\nPaper beats rock" \
          "\nRock beats scissors" \
          "\nEqual elements will tie!")

def user():
    u_choice = input("Your turn! Enter r for rock, s for scissors or p for paper: ")
    if u_choice == 'r' or u_choice == 'R':
        return "rock"
    elif u_choice == 'p' or u_choice == 'P':
        return "paper"
    elif u_choice == 's' or u_choice == 'S':
        return "scissors"

def machine():
    elements = ["rock", "scissors", "paper"]
    m_choice = random.choice(elements)
    return m_choice

def game():


# imprimir resultado do usuário

if __name__ == '__main__':
    print("Welcome to the rock scissors paper game!")
    while True:
        menu = int(input("Press \n1 to play the game\n2 to read the rules\n3 to quit the game: "))
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