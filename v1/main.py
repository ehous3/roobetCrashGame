import random
import math

f_read = open('highscore.txt', 'r')
highscore = int(f_read.read().strip())
f_read.close()

print(f"Welcome to ehouse's crash, you will start will $100 and will lose or gain money based on how you do. Try to beat the highscore of ${highscore}")
usrMny = 100
print("Current balance: $", usrMny)

def playGame(bet, usrMny): 
    crashNum = round(random.uniform(1, 10), 2)
    i = 1
    p = None
    while round_decimals_down(i,1) <= round_decimals_down(crashNum, 1) or p.lower() == "p":
        print(round(i,1), "x")
        p = input("Enter P to pull your bet: ")
        print(crashNum)
        if p.lower() == "p":
            usrMny = usrMny + (bet * i) 
            break    
        if round_decimals_down(i,1) == round_decimals_down(crashNum, 1):
            print(f"CRASHED at {round(i,1)}X you lose")
            break
        i+=.1
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
        bet = int(input("Amount to bet: $"))
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
    print("Sorry, but you ran out of money. There are a couple ways to gain more though.")
    print("A) Rob someone")
    print("B) Phone a friend")
    print("C) Deposit money")
    print("D) Quit")
    choice = input("Type A, B, C, or D: ")
    if choice.lower() == "a": 
        rob = random.randint(1, 10)
        if rob > 3:
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
        hasDeposited = False
        if hasDeposited == False:
            print("You had $25 left in your account. Here you go")
            usrMny = 25
            print("Current balance: $", usrMny)
            intro(usrMny)
            hasDeposited = True
    else: 
        print("Thank you for playing")

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
