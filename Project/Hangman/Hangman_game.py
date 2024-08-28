import random
from Hangman_words import word_list_lower
from Hangman_art import HANG_Stage
Lives = 6


choosen_word = random.choice(word_list_lower)
print(choosen_word)

#First Step

Perf_Word = ""
word_len = len(choosen_word)

for i in range(0,word_len):
    Perf_Word+="_ "

print(Perf_Word)

game_over = False
correct_letters = []
while not game_over:
    print(f"*******{Lives} Lives Left *********")

    guess = input("Guess the letter : ").lower()
    if guess in correct_letters:
        print(f"******YOU ALREADY GUESS {guess}******")



    # Second Step
    display = ""
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"  

    print(display) 

    if guess not in choosen_word:
        Lives -= 1
        if Lives == 0:
            game_over = True
            print("***********YOU LOOSE*********")

    if "_" not in display:
        game_over = True
        print("***********YOU WIN*********")

    print(HANG_Stage[6-Lives])