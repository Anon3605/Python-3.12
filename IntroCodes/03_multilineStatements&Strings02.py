print("This is the example of Implicit and Explicit new line example program.")

listA=[1, #comments can be included
       2, #comments can be included
       3]

def function(a, #comments can be included
             b):
    code_01=1
    code_02=2
    function(code_01,#you can make another comment
            code_02 )

if listA[0] \
    and listA[1] \
    and listA[2]:
    print("Hello World")

def summation(x=0, #default value is 0
              y=0, #default value is 0
              z=0):
    return x+y+z

def multiplication(x=0, #default value is 0
                   y=0, #default value is 0
                   z=0):
    return x*y*z

def name(str1="",
         str2="",
         str3=""):
    print(f"""Your first name is: {str1}
          Your middle name is: {str2}
          Your last name is : {str3}
          Your full name will be {str1} {str2} {str3}""")

ans=int(input("Wanna see Multiline Statements(01) or Mulline Strings(02): "))
if ans==1 \
    or \
    ans==2:
    if ans==1:
        print("Enter 3 values with spaces")
        x=[int(i) for i in input().split()]
        print(f"""Summation is: {summation(x[0],x[1],x[2])}
Multiply is: {multiplication(x[0],x[1],x[2])}""")
        print("""The whole operation went through this code which is in the source code:

listA=[1, #comments can be included
    2, #comments can be included
    3]

def function(a, #comments can be included
    b):
    code_01=1
    code_02=2
    function(code_01,#you can make another comment
            code_02 )

if listA[0] \
    and listA[1] \
    and listA[2]:
    print("Hello World")
        
def summation(x=0, #default value is 0
        y=0, #default value is 0
        z=0):
    return x+y+z

def multiplication(x=0, #default value is 0
    y=0, #default value is 0
    z=0):
    return x*y*z
        
This shows that the parameters are arranged in new-lines and have in-line comments""")
    elif ans==2:
        print("""Enter your first, middle and last name with spaces
Skip if you don't require one""")
        print("We use triple quotation for multiline string \"\"\"strings\"\"\"""")
        first_N,middle_N,last_N=input("First Name: "),input("Middle Name: "),input("Last Name: ")
        x=[first_N,
           middle_N,
           last_N]
        print(f"Input taken, {x}")
        name(x[0],x[1],x[2])
        print("""This is the code that is written for the output,
def name(str1="",
        str2="",
        str3=""):
    print(f\"\"\"Your first name is: \{str1\}
    Your middle name is: {str2}
    Your last name is : {str3}
    Your full name will be {str1} {str2} {str3}\"\"\")
Here tou can see the arguments are using implicitly and the print statement is multiline string""")
else:
    print("""Wrong Input...
Closing...
Thank You...""")