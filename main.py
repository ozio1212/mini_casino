import dice_throw
import balance

def games_menu():
    print("Welcome to Text-Casino!")
    print("\n")
    print("List of the available games:")
    print("1) Dice throw game")
    print("5) Exit the casino (did you know 90% of gamblers quit just before they hit it big?)")

    game_choice = input("Please choose game you want to play, by entering the corresponding number: ")
    return game_choice

def main():

    global user_balance
    user_balance = balance.balance()

    while True:
        choice = games_menu()
        if choice == "1":
            user_balance = dice_throw.dice_throw(user_balance)
        elif choice == '2':
            print("PLACEHOLDER")
        elif choice == '3':
            print("PLACEHOLDER")
        elif choice == '4':
            print("PLACEHOLDER")
        elif choice == '5':
            print("Thanks for playing :)")
            break
        else:
            print("Incorrect selection, try again.")

if __name__ == "__main__":
    main()
