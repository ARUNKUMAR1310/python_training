name = input("User: ")

print(f"Python: Welcome to {name}'s calculator, what operation do you want to do")
operation = input("User: ")

print("Python: Enter the current year")
num1 = input("User: ")

print("Python: Enter the birth year")
num2 = input("User: ")

# Convert inputs to numbers
Current_year = int(num1)
birth_year  = int(num2)

if operation.upper() == "SUBTRACT":
    #SUBTRACT here
    result =Current_year - birth_year

else:
    result = "Unknown operation"

# Display the result
print(f"Python: The answer is {result}")
