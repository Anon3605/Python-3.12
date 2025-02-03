import sys
import ctypes
print('Please install sys and ctypes using \'pip install package_name\' first')

variable_01 = 10
variable_02 = variable_01
variable_03 =  variable_02

listA=[1,2,3]
listB=listA
listC=listB
print(ctypes.c_long.from_address(id(listC)).value)
print("Reference count is the number that represent how many variables are pointing on that Memory-Location")
print("Note: You must see the source code from the Editor for better understanding")
print("=====================================================")
print("Typically the reference is 1 when you create a variable and store a value in it")
print("""The Python Memory Manager is a great term that actually do the bigger work.
This Big brother helps you to code without hesitation cause you need to understand,
utilizing the memory is really hard if we program or code, This big bro help us to 
manage memory locations, pointers and destroy accessing variable storages""")

print(f"The reference count for variable_01 is {sys.getrefcount(variable_01)}")
print(f"The reference count for variable_02 is {sys.getrefcount(variable_02)}")
print(f"The reference count for variable_03 is {sys.getrefcount(variable_03)}")
print(f"The reference count for list A is {sys.getrefcount(listA)}")
print(f"The reference count for list B is {sys.getrefcount(listB)}")
print(f"The reference count for list C is {sys.getrefcount(listC)}")

print(f"The reference count using \'ctypes.c_long.from_address().value\' is {ctypes.c_long.from_address(id(listC)).value}")
print(f"The reference count using \'ctypes.c_long.from_address().value\' is {ctypes.c_long.from_address(id(variable_01)).value}")
