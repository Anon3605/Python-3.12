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
print("Output for the varibles we get:") 

print(f"Decimal value is {id(variable01)} and hex is {hex(id(variable01))}")
print(f"Decimal value is {id(variable02)} and hex is {hex(id(variable02))}")
print(f"Decimal value is {id(variable03)} and hex is {hex(id(variable03))}")