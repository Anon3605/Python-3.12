import sys
import ctypes
print('Please install sys and ctypes using \'pip install package_name\' first')
print("""Here we have listA, listB, listC, listZ where
    listA=>listB
    listA=>listB=>listC
    listA=>listZ""")
listA=[1,2,3]
listB=listA
listC=listB
listZ=listA

print("Reference count is the number that represent how many variables are pointing on that Memory-Location")
print("Note: You must see the source code from the Editor for better understanding")
print("=====================================================")
print("Typically the reference is 1 when you create a variable and store a value in it")
print("""The Python Memory Manager is a great term that actually do the bigger work.
This Big brother helps you to code without hesitation cause you need to understand,
utilizing the memory is really hard if we program or code, This big bro help us to 
manage memory locations, pointers and destroy accessing variable storages\n""")
print("Using sys.getrefcount():")
print(f"The reference count for list A is {sys.getrefcount(listA)}")
print(f"The reference count for list B is {sys.getrefcount(listB)}")
print(f"The reference count for list C is {sys.getrefcount(listC)}")
print("""Note: The sys.getrefcount() gives you the main reference + 1 because the extra 1
is the sys.getrefcount() also refer itself to the location that's why 
we get extra 1 with the main reference point\n""")

print(f"The reference count using \'ctypes.c_long.from_address().value\' is {ctypes.c_long.from_address(id(listC)).value}")
print("""Note: The main ctypes.c_long.from_address(id(variable_name))) is giving us the acurate 
memorylocation to the module and module returning the actual reference counts\n""")

print("If we turn listZ into None or listZ=None, we get :")
listZ=None
print(f"The reference count for list A is {sys.getrefcount(listA)}")
print("We are storing the main memory address to a variableX")
variableX=id(listA)
print("If we turn listA into None or listA=None, we get :")
listA=None
print(f"The reference count using \'ctypes.c_long.from_address().value\' is {ctypes.c_long.from_address(variableX).value}")
print("So it doesn't mater what is the root, everyone is directly connected to the variable reference")
print("Turning all into None")
listB, listC = None, None
print(print(f"The reference count using \'ctypes.c_long.from_address().value\' on variableX is {ctypes.c_long.from_address(variableX).value}"))
print("So now you got None")
print("The MEM LOCATION : {variableX}")
print("This will be stored with the garbage values and Python Memory manger will not let you to access it later")
