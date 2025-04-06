import random
import time

def coin_toss(user_balance):

    # Checking if everything is okay about bet and bet_type:
    print(f"Your current balance is: {round(user_balance,2)} $")
    print("Are you betting on heads or tails?\n1) Heads\n2) Tails")
    bet_type = int(input("\nPick a number: "))

    if bet_type not in [1, 2]:
        print("Invalid choice. Please choose '1' or '2'.")
        return user_balance

    bet = float(input("Enter your bet amount: "))
    if bet > user_balance:
        print("You cannot bet more than your current balance.")
        return user_balance

    # Game:
    print("Coin is in the air...")
    time.sleep(1)
    print("It's falling!")
    time.sleep(1)
    result = random.randint(1,2)

    if bet_type == 1:
        if result == 1:
            print("The result is Heads!")
            print("You won!")
            user_balance += bet
        else:
            print("The result is Tails!")
            print("You lost!")
            user_balance -= bet

    if bet_type == 2:
        if result == 2:
            print("The result is Tails!")
            print("You won!")
            user_balance += bet
        else:
            print("The result is Heads!")
            print("You lost!")
            user_balance -= bet

    print(f"Your new balance is: {round(user_balance, 2)} $")
    return user_balance