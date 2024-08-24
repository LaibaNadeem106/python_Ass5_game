import random

def play_high_low_game(num_rounds=5):
    print("WELCOME to High Low GaMe ^-^")
    print("--------------------------------")

    score =0
    for round_number in range(1, num_rounds+1):
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Round{round_number}")
        print(f"Your Number is {player_number}")
        
        while True:
            guess =input("Do you think your number is higher or lower than computer's ?").lower().strip()
            if guess in ['higher','lower']:
                break
            print("Please enter either 'higher' or 'lower")

        if (guess == "higher" and player_number>computer_number) or (guess == "lower" and player_number<computer_number):
            print(f"You were right ! The computer's number was {computer_number}")
            score+=1

        else:
            print(f"Awwww!!!! that's Incorrect . The Computer's nnumber was {computer_number}")

        print(f"Your score is now{score}")

    if score == num_rounds:
        print("Wow! You played Perfectly ")
    elif score>=num_rounds//2:
        print("GOOD job ! you played really well ")
    else:
        print("Better luck next time!")

NUM_ROUNDS =5
play_high_low_game(NUM_ROUNDS)
