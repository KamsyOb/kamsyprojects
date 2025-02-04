#convert string of numbers to list of numbers

n = str(input("Enter a string of numbers: "))

def convert_to_list(n):
    return [int(i) for i in n]

m = convert_to_list(n)

