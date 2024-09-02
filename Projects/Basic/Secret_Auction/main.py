from Logo import logo_art
import os


def clear_screen():
   
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')

print(logo_art)


print("****WELCOME TO THE SECRET AUCTION PROGRAM******")

bids = {}

game = True

while game:
    name = input("What is your Name ? : ")
    price = int(input("What is your Bid : $"))

    bids[name] = price
    fs = True
    while fs:
        situation = input("Are there are any other bidders ? Type 'Yes' or 'No'  :").lower()
        if situation == "yes":
            game = True
            fs = False
            clear_screen()
        elif situation =="no":
            game = False
            fs = False
        else:
            print("You entered the wrong input we think")
            fs = True

maxi = 0
final = ""
for i in bids:
    if bids[i] > maxi:
        maxi = bids[i]
        final = i

print(f"****THE WINNER OF BID IS {final} *********")

