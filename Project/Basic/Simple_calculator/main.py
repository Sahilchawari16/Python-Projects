import Logo
import os

def clear_screen():
   
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')




def add(f_n, s_n):
    return f_n + s_n

def min(f_n, s_n):
    return f_n - s_n

def mul(f_n, s_n):
    return f_n*s_n

def div(f_n, s_n):
    return f_n/s_n


cal_dict = {'+' : add,
            '-' : min,
            '*' : mul,
            '/' : div}
def calculator():

    # print(Logo.logo_art)
    print(Logo.calculator_picture)
    want_repeat = True

    f_number = float(input("What is First Number :"))
    while want_repeat:
        for i in cal_dict:
            print(i)
        cal_symbol = input("Pick an Operation :  ")
        s_number = float(input("Write your Second Number : "))

        answer = cal_dict[cal_symbol](f_number, s_number)
        print(f"{f_number} {cal_symbol} {s_number} = {answer}")


        choice =input(f"If you want to start with the {answer} then type 'yes' , or type 'no' to start with a new calculation.").lower()
        if choice == 'yes':
            f_number = answer

        else:
            want_repeat = False
            clear_screen()
            calculator()

calculator()


