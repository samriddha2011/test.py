
 

def sum(num1,num2):
    print(num1+num2) 
    return num1+num2  

def sub(num1,num2):
    print(num1-num2)    
    return num1-num2

def mul(num1,num2):
    print(num1*num2)    
    return num1*num2

def div(num1,num2):
    if num2 == 0:
        print("Error: You cannot divide a number by zero!")
        return None
    else:
        print(num1/num2)    
        return num1/num2
    

print("Welcome to the calculator program!")
print("This program can perform addition, subtraction, multiplication, and division.")
print("You will be prompted to enter two numbers and select an operation.")
print("The program will then display the result of the operation.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

try:

  result = num1 / num2

  print(f"The result is: {result}")

except ZeroDivisionError:

  print("Error: You cannot divide a number by zero!")

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:

    if choice == '1':
        sum(num1, num2)
    elif choice == '2':
        sub(num1, num2)
    elif choice == '3':
        mul(num1, num2)
    elif choice == '4':
        div(num1, num2)
else:
    print("Invalid input")