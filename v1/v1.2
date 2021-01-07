import random
import math
import hashlib
import hmac
import sys

f_read = open('highscore.txt', 'r')
highscore = int(f_read.read().strip())
f_read.close()

print(f"Welcome to ehouse's crash, you will start will $100 and will lose or gain money based on how you do. Try to beat the highscore of ${highscore}")
usrMny = 100.00
print("Current balance: $", usrMny)

hasDeposited = False

def playGame(bet, usrMny): 
    e = 2**52
    salt = random.randint(0, sys.maxsize)
    game_hash = random.randint(0, sys.maxsize)
    hm = hmac.new(str.encode(str(game_hash)), b'', hashlib.sha256)
    hm.update(str(salt).encode("utf-8"))
    h = hm.hexdigest()
    if (int(h, 16) % 33 == 0):
        crashNum = 1
    h = int(h[:13], 16)
    e = 2**52
    crashNum = (((100 * e - h) / (e-h)) // 1) / 100.0
    i = 1
    p = None
    #print(crashNum)  #optional for testing, ruins fun
    while round_decimals_down(i,2) <= round_decimals_down(crashNum, 2) or p.lower() == "p":
        print(round(i,2), "x")
        p = input("Enter P to pull your bet: ")
        if p.lower() == "p":
            usrMny = usrMny + (bet * i) 
            break    
        if round_decimals_down(i,2) == round_decimals_down(crashNum, 2):
            print(f"CRASHED at {round(i,2)}x you lose")
            break
        i+=.01
    print("Current balance: $", round(usrMny, 1))
    if usrMny > highscore:
        newHs = int(float(usrMny))
        f_write = open('highscore.txt', 'w')
        f_write.write(str(newHs))
        f_write.close()
        print(f"Congrats you beat the highscore and set a new record with a score of ${newHs}")
    if usrMny > 1.0:
        intro(usrMny)
    else:
        outOfMoney()

def intro(usrMny): 
    try:
        bet = float(input("Amount to bet: $"))
        if bet > usrMny:
            print("You do not have enough money for that bet. Try again.")
            print("Current balance: $", usrMny)
            intro(usrMny)
        else:
            print("Launching rocket...")
            usrMny = usrMny - bet
            playGame(bet, usrMny)
    except ValueError:
        print("Please enter a valid bet")
        intro(usrMny)

def outOfMoney():
    global hasDeposited
    print("Sorry, but you ran out of money. There are a couple ways to gain more though.")
    print('A) Rob someone\nB) Phone a friend\nC) Deposit money\nD) Quit')
    choice = input("Type A, B, C, or D: ")
    if choice.lower() == "a": 
        rob = random.randint(1, 10)
        if rob < 3:
            print("Robbing was successful, here is another $100")
            usrMny = 100
            print("Current balance: $", usrMny)
            intro(usrMny)
        else:
            print("Rob unsuccessful, and you are going to jail. Game Over")
    elif choice.lower() == "b":
        phoneFriend = random.randint(1, 10)
        if phoneFriend > 6:
            print("Your friend is very nice and gives you another $40")
            usrMny = 40
            print("Current balance: $", usrMny)
            intro(usrMny)
        else:
            print("Your friend didn't pick up. Game Over")
    elif choice.lower() == "c":
        if hasDeposited == False:
            print("You had $25 left in your account. Here you go")
            usrMny = 25
            print("Current balance: $", usrMny)
            hasDeposited = True
            intro(usrMny)
        else:
            print("Your account is empty. Game over.")
    elif choice.lower() == "d":
        print("Thank you for playing")
    else: 
        print("Please enter a valid letter")
        outOfMoney()

def round_decimals_down(number:float, decimals:int=2):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor

intro(usrMny)
