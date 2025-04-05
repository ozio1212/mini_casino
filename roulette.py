import random
import time

def play_roulette(user_balance):

    # Checking if everything is okay about bet and bet_type:
    print(f"Your current balance is: {round(user_balance, 2)} $")
    bet = float(input("Enter your bet amount: "))
    if bet > user_balance:
        print("You cannot bet more than your current balance.")
        return user_balance

    bet_type = input("Choose your bet : \n1) Color\n2) Number\n")
    if bet_type not in ['1', '2', '3', '4']:
        print("Invalid choice.")
        return user_balance

    # Game

    red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    green = [0]

    result = random.randint(0, 36)


    # COLOR BET:
    if bet_type == "1":
        color_type = input("Pick color, red/black/green: ")

        if color_type == "red":
            if result in red:
                print("The ball is rolling...")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(2)
                print(f"Result is {result} !")
                print("You win!")
                user_balance += bet
            else:
                print("The ball is rolling...")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(2)
                print(f"Result is {result} !")
                print("You lose!")
                user_balance -= bet

        elif color_type == "black":
            if result in black:
                print("The ball is rolling...")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(2)
                print(f"Result is {result} !")
                print("You win!")
                user_balance += bet
            else:
                print("The ball is rolling...")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(2)
                print(f"Result is {result} !")
                print("You lose!")
                user_balance -= bet

        elif color_type == "green":
            if result in green:
                print("The ball is rolling...")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(2)
                print(f"Result is {result} !")
                print("You win!")
                user_balance += 13*bet
            else:
                print("The ball is rolling...")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(2)
                print(f"Result is {result} !")
                print("You lose!")
                user_balance -= bet

        else:
            print("The ball is rolling...")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(2)
            print(f"Result is {result} !")
            print("You choose wrong color!")
            return user_balance

    # NUMBER BET:
    if bet_type == "2":
        number_result = int(input("Pick ur number (0-36): "))

        if number_result == result:
            print("The ball is rolling...")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(2)
            print(f"Result is {result} !")
            print("You win!")
            user_balance += 3*bet
        else:
            print("The ball is rolling...")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(2)
            print(f"Result is {result} !")
            print("You lose!")
            user_balance -= bet

    print(f"Your new balance is: {round(user_balance,2)} $")
    return user_balance
