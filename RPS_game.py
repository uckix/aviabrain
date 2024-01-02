"""
Rock-Paper-Scissors Game
Author: Shahriyor
"""
import random

reqs = ["r", "p", "s"]

def computer():
    return random.choice(reqs)

def play():
    myturn = input("Choose one r/p/s: ")
    print(f"You choose {myturn}")
    compturn = computer()
    print(f"Computer chooses {compturn}")

    if myturn == compturn:
        print("It's a tie!")
        return 0
    elif (myturn == "r" and compturn == "s") or (myturn == "p" and compturn == "r") or (myturn == "s" and compturn == "p"):
        print("You win!")
        return 1
    elif (myturn == "r" and compturn == "p") or (myturn == "p" and compturn == "s") or (myturn == "s" and compturn == "r"):
        print("Computer wins!")
        return 2
    else:
        print("An invalid character was entered!", myturn, 'Choose again!')
        return play()

def main():
    computer_score = 0
    my_score = 0

    number_of_playing = input("How many times you want to play? ")

    if number_of_playing.isdigit():
        number_of_playing = int(number_of_playing)
    else:
        print("Please enter a number!")
        main()

    rounds_played = 0

    while rounds_played < number_of_playing:
        result = play()
        
        if result == 1:
            my_score += 1
        elif result == 2:
            computer_score += 1

        rounds_played += 1

    print(f"\nYour score is {my_score}")
    print(f"Computer's score is {computer_score}")

main()
