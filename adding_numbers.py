# Subroutine to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main program
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call the subroutine
result = add_numbers(num1, num2)

# Use a for loop to multiply result by 10
for i in range(1, 11):
    print(result * i)
