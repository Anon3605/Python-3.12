import time

print("Variables are nothing but Identifiers which identify something")
print("""There are some Rules that Identifiers should follow:
--> They are \"Case-Sensitive\"
--> Starts with underscore( _ ) or letter ( a-z, A-Z )
    example: var, my_var, index1, index_1, _var, __var, __init__
--> Cannot be reserved keywords of PYTHON!!!
False	await	else	import	pass
None	break	except	in	raise
True	class	finally	is	return
and	continue	for	lambda	try
as	def	from	nonlocal	while
assert	del	global	not	with
async	elif	if	or	yield
""")

print("\nConventions\n")
print("01: Single Underscore")
print("_variableName --> This is called \"Internal Use\" or \"Private variable\" ")
print("""Objects named this way will not get imported like : 
from module import *""")
print("\n02: Double Underscore")
print("""__variableName --> Used to destroy class attributes
Useful in inheritance chains""")
print("\n03: Double Double Underscore or Dunder")
print("""__variableName__ --> Used for system defined names that have a special meaning
to the interpreter
Use the only pre-defined by python, not make one
Example__lt__(), __init__()
Here __init__() means initialization and __lt__() means x<y like x.__lt__(y)""")

validVariableNames=["utilities",
                    "db_utils",
                    "BankAccount",
                    "open_account", 
                    "account_id",
                    "MIN_ARP (This one for constant)"]
ln=["st","nd","rd","th"]

for i in range(len(validVariableNames)):
    time.sleep(2) 
    j=i
    if i>3:
        j=3
    print(f"Example of {i+1}{ln[j]} variable name: {validVariableNames[i]}")

answer=input("Understood?(Yes or No?) : ")
print("GO to next") if answer.lower()=="yes" else print("Read again")