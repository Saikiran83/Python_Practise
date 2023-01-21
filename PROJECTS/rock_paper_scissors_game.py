import random
import time 

rock = 1
paper = 2
scissors = 3

names = {rock : "Rock", paper : "Paper", scissors : "Scissors"}
rules = {rock : scissors, paper : rock, scissors : paper}

players_score = 0
computer_score = 0

def start():
    print("let's start playing rock, paper and scissors game")
    while game():
        pass
    scores()
def game():
    player = move()
    computer = random.randint(1,3)
    result(player,computer)
    return play_again()
def move():
    while True:
        print
        player = input("Rock=1\nPaper=2\nScissors=3\nMake a move :")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("OOPS i didn't understand that, please enter 1,2 or 3")

def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print(f"computer threw {names[computer]}")
    global players_score, computer_score
    if player == computer:
        print("tie game")
    else:
        if rules[player] == computer:
            print("your victory has been assured")
            players_score += 1
        else:
            print("the computer laughs as you have been defeated")
            computer_score += 1
        
def play_again():
    answer = input("would you like to play again? y/n \n")
    if answer in ("y", "Y", "yes", "Yes", "Ofcourse!"):
        return answer
    else:
        print("thank you very much playing the game, see you again")

def scores():
    global players_score, computer_score
    print("HIGH scores")
    print("player: ", players_score)
    print("computer:", computer_score)

if __name__ == "__main__":
    start()
