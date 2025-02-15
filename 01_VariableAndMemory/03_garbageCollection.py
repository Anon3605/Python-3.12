import ctypes
import gc

print("""Memory Leak: If a program fails to release unwanted memory after finishing a particular task,
can cause low performance or failure to the system, that's called Memory Leak""")
print("""Python Memory Manager: If the memory reference for a variable is 0 then this good guy removes 
the variable memory address and the value or frees up the space""")
print("""But for circular references we use garbage collector from python cause circular references 
creates memory leaks as they cab't be removed by the Python Memory Manager""")

print("Disabling the garbage collector aka gc")
gc.disable()

def referenceCount(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object Exists"
    return "404"

class First:
    def __init__(self):
        self.a = Second(self)
        print(f"A: self.{hex(id(self))} and b: {hex(id(self.a))}")
    

class Second:
    def __init__(self, a):
        self.b = a
        print(f"B: self.{hex(id(self))} and b: {hex(id(self.b))}")


my_var=First()
MEM_LOCA=id(my_var.a) #Storing for not to lose uk
MEM_LOCB=id(my_var.a.b) #Storing for not to lose uk
print(f"Memory reference count of my_var.a before removing the initial variable name {referenceCount(MEM_LOCA)}")
print(f"Memory reference count of my_var.b before removing the initial variable name {referenceCount(MEM_LOCB)}")

my_var=None
print("my_var is allocated to None")
print(f"Memory reference count of my_var.a after removing the initial variable name {referenceCount(MEM_LOCA)}")
print(f"Memory reference count of my_var.b after removing the initial variable name {referenceCount(MEM_LOCB)}")

print("This is Circular Referencing where --> a pointing to --> b and vice versa")

print("     a --> b     ")
print("     ↑     ↓     ")
print("     b <-- a     ")

print(f"See if the object Still exists in the memory: {object_by_id(MEM_LOCA)}")
print(f"See if the object Still exists in the memory: {object_by_id(MEM_LOCB)}")

gc.enable()
gc.collect()

print("After turning on the Garbage Collector or gc.enable() and collecting the circular references")
print(f"See if the object Still exists in the memory: {object_by_id(MEM_LOCA)}")
print(f"See if the object Still exists in the memory: {object_by_id(MEM_LOCB)}")
print("404 means not found")
print("The garbage collector has deleted all the circular references and cleaned it up")