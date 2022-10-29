from random import randint

game_over = False
EZT = 10
HRT = 5


def check(turns, guess, answer):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print(f"you win it was {answer}")
        game_over = True


def difficulty():
    q = input("would you like easy or hard difficulty e or h\n")
    if q == "h":
        return HRT
    else:
        return EZT


def game():
    print("welcome to the guessing game")
    print("pick a number between 1 and 100")

    answer = randint(1, 100)
    turns = difficulty()

    guess = 0
    while guess != answer:

        print(f" you have {turns} turns ")
        guess = int(input("make a guess: \n"))
        turns = check(turns, guess, answer)

        if turns == 0:
            print("you've run out of guesses you lose")
            return


game()