import random
def main():
    numbers = [0,1,2,3,4,5,6,7,8,9,10,11]

    input("Press enter to play: ")

    player1 = random.randint(0,11)
    player2 = random.randint(0,11)

    print(f"player one's number is {numbers[player1]}\n player two's number is {numbers[player2]}")

    if player1 > player2 :
        print("player 1 wins !")
    elif player2 > player1:
        print ("player 2 wins!")
    else:
        print("it's a tie.. nobody wins.")