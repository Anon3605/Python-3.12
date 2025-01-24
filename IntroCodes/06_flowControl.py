import random

def show():
    programs=["Calculator", "Rock-Paper-Scissor"]
    for i in range(len(programs)):
        print(f"{i+1}--> {programs[i]}")

def rockPaperScissor(x):
    # 1=rock
    # 2=paper
    # 3=scissor
    try:
        player=int(x)
    except:
        return -1
    bot=random.randint(1,3)
    print("Bot choose: ",bot)
    if player<bot:
        if player==1 and bot==3 :
            print("Player won this round")
            return 1
        else:
            print("Player lose this round")
    elif player>bot:
        if player==3 and bot==1:
            print("Player lose this round")
        else:
            print("Player won this round")
            return 1
    else:
        print("Draw this round")
    return 0

def calculator(args):
    x=args.split()
    if x[1]=="+":
        return int(x[0])+int(x[2])
    elif x[1]=="-":
        return int(x[0])-int(x[2])
    elif x[1]=="/":
        return int(x[0])/int(x[2])
    elif x[1]=="x":
        return int(x[0])*int(x[2])
    elif x[1]=="%":
        return int(x[0])%int(x[2])
    elif x[1]=="^":
        return int(x[0])**int(x[2])
    else:
        return -1

print("""if conditions:
    statements
elif conditions:
    statements
else:
    statements""")
print("So this is flow control in simple\n")

show()
choice= True
while choice:
    try:
        program=int(input("Which program do you want to see now: "))
        if program not in (1,2):
            print("Please give the value as given in the program")
            show()
            continue
        else:
            if program==1:
                print("""+ --> addition
- --> subtraction
/ --> division
x --> Multiplication
% --> Modulus
^ --> Power""")
                print("Please Enter an equation like this: 5 + 10")
                print("This means you need to give spaces between every values and operant")
                print("Note: This program is not error handled, so you'll get error if you did wrong")
                answer=calculator(input("Enter in the format given above: "))
                print(f"Your calculation is : {answer}")
            elif program==2:
                print("""1=rock\n2=paper\n3=scissor""")
                print("You'll play for 3 rounds")
                print("Note: This program is not error handled, so you'll get error if you did wrong")
                win=0
                for i in range(3):
                    win+=rockPaperScissor(input("Rock or Paper Or Scissor?: "))
                if win>1:
                    print("You won the tournament")
                else:
                    print(f"You Fucked up bro! You loss in {win}:{3-win} ratio")
            print("Exiting")
            choice=False
    except:
        print("You entered a wrong type")
        continue