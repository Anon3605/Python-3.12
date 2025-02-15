import math
number = 10
print(f"The data type of number is {type(number)}")
number = 0.1
print(f"The data type of number is {type(number)}")
number = "Hello"
print(f"The data type of number is {type(number)}")
number = ["I", "am", "Whatever"]
print(f"The data type of number is {type(number)}")
number = lambda x: (x*2)/0.5
print(f"The data type of number is {type(number)}")
number = 4 +5j
print(f"The data type of number is {type(number)}")
number = {1:11,
          2:22,
          3:33,
          4:44,
          5:55}
print(f"The data type of number is {type(number)}")

print("""So here's the reality check, The number is just and address it never cared
about it's datatype or anything, every time a new variable is assigned, the variable
number just changed it's reference and the python packet manager removed the data
from the location as the reference count is fucking 0, that's it.
      
THAT'S THE DYNAMIC WRITING RIGHT THERE""")