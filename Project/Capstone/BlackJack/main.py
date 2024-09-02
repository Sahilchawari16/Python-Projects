import random
from logo import logo
import os

def clear_screen():
   
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,]
    card = random.choice(cards)
    return card
def calculate_score(cardsresult):
    if sum(cardsresult)==21 and len(cardsresult)==2:
        return sum(cardsresult)
    if sum(cardsresult)>21 and 11 in cardsresult:
        cardsresult.remove(11)
        cardsresult.append(1)
        
    return sum(cardsresult)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "You Win You Have A BlackJack"
    elif c_score == 0:
        return "You Lose Opponent Has A BlackJack"
    elif u_score > 21:
        return "You Went Over , Opponent Wins"
    elif c_score > 21:
        return "Opponent Went Over , You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {user_cards}, Current score : {user_score}")
        print(f"Computer first card is : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            user_deal = input("Type 'Yes' to get another card , 'no' to pass : ").lower()
            if user_deal == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        print(f"Your final hand: {user_cards}. Your final score is {user_score}")
        print(f"The Computer's final hand : {computer_cards}. The Computers final score is {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'yes' or 'no':") == "yes":
    clear_screen()
    print(logo)
    play_game()

