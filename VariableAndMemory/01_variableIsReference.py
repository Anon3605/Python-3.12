variable01=10
variable02="Anon3605"
variable03=25.5

print("As we know variables are used to store something in a program")
print("But here is the main catch\n")
print("01. The variable name you give is an alice name for a reference.")
print("02. Value is stored in a memory location")
print("03.The memory location is called reference point\n")

print("variable_name--> Refers to a memory location --> Memory stores the value in it\n")

print("""variable01=10
variable02="Anon3605"
variable03=25.5
      
For this code we can use id(variable_name) to find out the memory location which
will be in a decimal number, to convert in to hwx we can use built in hexadecimal
convertor called hex()
Example: id(variable_name) or for hexadecimal, hex(id(variable_name))""")
print("Output for the variables we get:") 

print(f"For Variable01 decimal value is {id(variable01)} and hex is {hex(id(variable01))}")
print(f"For Variable02 decimal value is {id(variable02)} and hex is {hex(id(variable02))}")
print(f"For Variable03 decimal value is {id(variable03)} and hex is {hex(id(variable03))}\n")

print("Note: Variables are memory references\n")
print("The whole process is here:")
print("01. Everything in python are called object")
print("02. object01, object02, object03 ... object0n are stored in various memory locations")
print("    The whole memory location section where the objects are stored, called heap")
print("03. Retrieving objects from the heap is taken care by the Python Memory Manager")