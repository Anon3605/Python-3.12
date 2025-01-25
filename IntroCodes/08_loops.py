def for_loop():
    a="Hello"
    b="Bye"
    for i in a:
        if i=="o":
            print(i)
            break
        print(f"{i}--> ",end=("")) 
    print("And Now")
    for i in b:
        if i=="e":
            print("e")
            break
        print(f"{i}--> ",end=("")) 
    print("END")

def while_loop():
    i=1
    while i<11:
        if i==6:
            print(f"99 X {i} = {i*99}")
        print(f"99 X {i} = {i*99}",end=("--> "))
        i+=1
    print("END")

def check(param):
    try:
        return int(param)
    except:
        print("Please, I'm done with making juicy replies for your errors...")
        print("Do as it says")
        return False

data={
        "for Loop: It's bound to a range or a limit where the loop will always stop":
        ["""syntax:
    for variable in iterable:
        statements
This loop will break if there is no iterable left.
Every time each iterable will be stored in the variable""",
        """Example:
    a="Hello"
    b="Bye"
    for i in a:
        if i=="o":
            print(i)
            break
        print(f"{i}--> ",end=("")) 
    print("And Now")
    for i in b:
        if i=="e":
            print("e")
            break
        print(f"{i}--> ",end=("")) 
    print("END")"""],
        "while Loop: It's not bound to a range, it will run until the condition is met":
        ["""syntax:
    while condition:
        statement
        increment/decrement/anything that will responsible to break the condition
Or else the loop will be infinite and the Ram of the machine will crash!!!""",
        """Example:
    i=1
    while i>11:
        if i==5:
            print(f"99 X {i} = {i*99}")
        print(f"99 X {i} = {i*99}",end=("-->"))
        i+=1
    print("END")"""],
        "do while loop is a loop that is fundamental in C or C++ or java or any compiler based language":
        ["""syntax:
    statement
    while statement_not_met_condition:
        statement""",
        """Example: If you saw the source code, you'll find:
    opt=check(input("Which One do you wanna Know?: "))
    while opt==None:
        print("====================================")
        opt=check(input("Which One do you wanna Know?: "))
This is where your input is checked first, if not, then we're running it in a loop until you gave an integer value
        """]
    }

print("""There are 3 types of loops in programming language
    -->for Loop
    -->while Loop
    -->do while Loop""")

opt=check(input("Which One do you wanna Know?: "))
while opt==None:
    print("====================================")
    opt=check(input("Which One do you wanna Know?: "))
for i in range(3):
    if i==opt-1:
        j=1
        for k in data:
            if j==opt:
                print(k)
                opt2=check(input("Do you wanna know more? (0/1): "))
                print(data[k][0]) if opt2==1 else print("Go have a sleep, you need that")
                opt2=check(input("Do you wanna know more? (0/1): "))
                print(data[k][1]) if opt2==1 else print("Go have a sleep, you need that")
                if opt==1 or opt==2:
                    opt2=check(input("Do you wanna see the output? (0/1): "))
                    if opt==1 and opt2==1:
                        for_loop()
                    elif opt==2 and opt2==1:
                        while_loop()
                    else:
                        print("You really need a mental health doctor. Did I code for nothing?!")
            j+=1
        break
else:
    print("GoodYear Tyres ltd.")