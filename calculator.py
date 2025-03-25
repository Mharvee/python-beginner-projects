def add(numb1, numb2):
    return numb1+numb2
def subtract(numb1, numb2):
    return numb1-numb2
def multiply(numb1,numb2):
    return numb1*numb2
def divide(numb1,numb2):
    if numb1==0 or numb2 == 0:
        print("Error! Division by zero")
        return None
    return numb1/numb2
while True:
    choice = int(input("Select your operation: 1 for Addition 2 for Subtraction 3 for Multiplication 4 for Division and 5 to quit "))
    if choice == 5:
        print("Goodbye!")
        break  # Exit loop

    if choice not in [1, 2, 3, 4]:  # Invalid operation check
        print("Invalid input! Please select a valid option.")
        continue
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if choice == 1:
        print(f"The sum is {add(num1,num2)}")
    elif choice == 2:
        print(f"The difference is {subtract(num1,num2)}")
    elif choice == 3:
        print(f"The product is {multiply(num1,num2)}")
    elif choice == 4:
        print(f"The quotient is {divide(num1,num2)}")
    elif choice == 5:
        print("Goodbye")
        break
    else:
        print("Please enter a valid input")


