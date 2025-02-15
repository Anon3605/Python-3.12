import ctypes
import gc

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

gc.disable()
my_var=First()