#convert string of numbers to list of numbers

n = (input("Enter a string of numbers: "))

def convert_to_list(n):
    return [int(i) for i in n]

m = convert_to_list(n)

p = input("Enter a string of words:")

def convert_to_list_str(p):
    return p.split()

q = convert_to_list_str(p)

print(f"Here is your list of numbers: {m} and here is your list of words: {q}")

