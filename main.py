from os import system
import game_data
import art
from random import randint

def clear ():
    system('cls')

def correctAns ():
    print (f"You're right! Current score: {score}\n")

random1 = randint(0, 49)
random2 = randint(0, 49)

score = 0
wrong = False

while (wrong == False):
    while (random1 == random2):
        random2 = randint (0,49)

    if (game_data.data[random1]['follower_count'] > game_data.data[random2]['follower_count']):
        higherIndex = random1
    else:
        higherIndex = random2

    clear ()
    print (art.gamelogo)
    if (score > 0):
        correctAns ()

    print (f"Compare A: {game_data.data[random1]['name']}, a {game_data.data[random1]['description']}, from {game_data.data[random1]['country']}.")
    print (art.vslogo)
    print (f"Against B: {game_data.data[random2]['name']}, a {game_data.data[random2]['description']}, from {game_data.data[random2]['country']}.")

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    if (user_choice == 'A' or user_choice == 'a'):
        if (higherIndex == random1):
            score += 1
        else:
            wrong = True
            print (f"Wrong answer. Your score: {score}")
            break
        
    elif (user_choice == 'B' or user_choice == 'b'):
        if (higherIndex == random2):
            score += 1
        else:
            wrong = True
            print (f"Wrong answer. Your score: {score}")
            break

    else:
        print ("Wrong input.")
    
    random1 = higherIndex
    random2 = randint (0, 49)