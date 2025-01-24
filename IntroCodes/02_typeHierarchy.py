import time
print("Here are 3 topics in short explained:")
time.sleep(1)
print("Numbers, Collections & Callables")
print("""Numbers are 2 types:
01.Integral
    --> Integers
    --> Boolean
02.Non-Integral
    --> Float (Double in C)
    --> Complex
    --> Decimals
    --> Fractions""")

print("""Callables are many-typed:
Callables are something which can be called in a program.
--> User-Defined Function
--> Generators
--> Classes
--> Instance Methods
--> Class Instances (--call__())
--> Built-in Functions (len(), open(), close())
--> Built-int methods (list_name.append(value))""")

print("""Singleton also known as \'Single Instance\'
Singletons ensures a class has only one instance and provides one global
point of access to that instances.
--> None
--> NotImplimented
--> Ellipsis(...)""")

print("""Collections have 3 types:
01. Sequences
    --> Mutable (Lists)
    --> Immutable (Tuples, Strings)
02. Sets
    --> Mutable (Sets)
    --> Immutable (Frozen Sets)
03. Mappings
    --> Dictionaries""")

def mutunmut(*args):
    mutable="Which can be changed after declaration with no problem or duplicates"
    immutable="Which can not be changed after declaration you need to duplicates"
    print("They are mutable and they are immutable. Do you wanna know? yes/no")
    ans=input().lower()
    print(f"{mutable} Example: '{args[0]}',\n{immutable} Examples: {str(args[1::])[1:-1]}") if ans=="yes" else print("Closing...")

def understand_collections(x=0):
    if x==1:
        print("A sequence in Python represents an arrangement of items in a specific order.\n \
            It's a data structure with elements indexed by their position, allowing you to access\n \
            and manipulate individual elements based on their index.")
        mutunmut("lists","tuples","strings")
    elif x==2:
        print("Sets are an unordered collection of unique elements, whereas a dictionary is an\n \
            ordered collection of key-value pairs. Sets store unique elements.")
        mutunmut("sets","frozen sets")
    elif x==3:
        print("Mappings are mutable objects. There is currently only one standard mapping type,\n \
            the dictionary . A dictionary's keys are almost arbitrary values. The only types of\n \
            values not acceptable as keys are values containing lists or dictionaries or other \n \
            mutable types that are compared by value rather than by object identity.\n \
            There is only one and that is Dictionary, which uses key/value pairs.")
    else:
        print("Wrong output, Closing...")
try:
    z=int(input("Which one do you wanna know?(1/2/3):"))
except:
    raise TypeError("Brotha! We said to give integer? why testing the program's limit?")
understand_collections(z)

