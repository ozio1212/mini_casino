import random
import time

def dice_throw(user_balance):
    print(f"Your current balance is: {round(user_balance,2)} $")
    bet_type = input("Do you want to bet on even or odd sum? (type 'even' or 'odd'): ")

    if bet_type not in ['even', 'odd']:
        print("Invalid choice. Please choose 'even' or 'odd'.")
        return user_balance

    bet = float(input("Enter your bet amount: "))
    if bet > user_balance:
        print("You cannot bet more than your current balance.")
        return user_balance

    throws = int(input("Choose the number of dice rolls (from 1 to 4): "))
    if throws < 1 or throws > 4:
        print("Please choose a number between 1 and 4.")
        return user_balance

    result = 0
    for i in range(throws):
        print("A toss is in progress...")
        time.sleep(1)
        roll = random.randint(1, 6)
        result += roll
        print(f"Your result for this throw is: {roll}")

        if i < throws - 1:
            input("Press enter to throw next time...")

    print("\n")
    print(f"Total result after {throws} throws: {result}")
    print("\n")

    is_even = result % 2 == 0

    if (is_even and bet_type == 'even') or (not is_even and bet_type == 'odd'):
        print("You win!")
        user_balance += bet
    else:
        print("You lose!")
        user_balance -= bet

    print(f"Your new balance is: {round(user_balance,2)} $")
    return user_balance




