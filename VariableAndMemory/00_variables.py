print("To store something we use variable")
print("It can be string, integer, boolean, float or etc")
listA=["Variable & Memory", "Variables?",
       "Reference Counting", "Garbage Collection", 
       "Dynamic+Static Typing", "Mutability and Immutability", 
       "Shared REfences", "Variable Equality", 
       "Everything in python are Objects"]
print("\nThe Contents are bellow for this section \n")
for i in range(len(listA)):
    print(f"Content: 0{i+1}_{listA[i]}")