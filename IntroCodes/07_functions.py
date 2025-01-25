import random as random
print("""\n\n
 There are 4 types of functions in the python
\n\n""")

listAnswer=[
    """--> Default Built-In Functions
        example: len(), sum(), range(), input()""",
    """--> Built-In Functions from Modules called Instance/Method
        example: list.slice(), list.append(), string.lower()""",
    """--> Lambda Functions
        example:
                square = lambda x: x**2
                print(square(2))
                >>>4""",
    """--> User-defined Functions
        example: def calculator or def rockPaperScissor in the previous example"""
]

opt=input("Which One Do you wanna know? 1,2,3,4: ")

try:
    opt=int(opt)
except:
    print("Are you fucking crazy? Aggain?!?")

if type(opt)==int:
    for i in range(4):
        if i==opt-1:
            print(listAnswer[i])
            if opt==3:
                num=input("Give a number that is big around 4 digits: ")
                try:
                    num=int(num)
                except:
                    print("My friend are you really enjoying my error handling only to hear some bullshit?")
                    print("Yeah, I know, I'm great...")
                if type(num)==type(1):
                    answer=lambda x: random.randint(0,num)
                    print(f"""
                            Your Lucky number is {answer(num)}""")
                    print("If you've seen the source script, you'll know the code explanation later...")
                else:
                    print("""
                            Your lucky number is 0, like your brain.
                            Can't go with a single fucking simple""","""
                                    \n\"instructions!!!\"""".upper())
            break
    else:
        print("No money no honey, I mean the not in range, not in list!!!")
else:
    print("You still playing with me, do you know that!?!")

