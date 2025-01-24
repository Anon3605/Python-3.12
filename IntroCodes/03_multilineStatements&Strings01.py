import time

print("This is the pre-requisite of Multiline statement and Multiline string")
print("Implicit or explicit expressions are work for physical newline\n")
def takeOptions():
    try:
        check=int(input("Which one do you want to know?:"))
        if check not in [1,2]:
            check=0
        return check-1
    except ValueError:
        raise ValueError("OOPSy!!! You gave a wrong input!")

listA=["Implicit", "Explicit"]
listB=["Note: Comments can be a part of it and the newline occurs after the comma\n",
    """Note: Comments cannot be a part of it and new line needs to be specified by 
backslash characters like \\n, \\r, \\t etc\n"""]
listC=["""An explicit newline is a newline that is directly written or specified in the code
Implicitly: 
Expressions can be use in:
    01. List
    02. Tuple
    03. Dictionary
    04. Sets
    05. Functions arguments/parameters""",
  """An implicit newline occurs automatically as part of an operation, usually without the \n
programmer needing to specify it.
Expressions can be use in:
    01. Conditions
    02. Strings"""]
print("There are two way to use multiline statements:")
print("".join(str(i+1)+". "+listA[i]+"\n" for i in range(2)))

choice=takeOptions()
if choice==-1:
    raise ValueError("OOPss!!! Wrong Input!!!")
print(choice)
time.sleep(1)
print(f"What is {listA[choice]} newline character?")
time.sleep(1)
print(f"{listC[choice]}")
time.sleep(1)
print(f"{listB[choice]}")