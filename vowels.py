vowels = ['a', 'e', 'i', 'o', 'u']

user = input("Enter any sentence: ")
user = user.lower()

vowels_number = sum([1 for char in user if char in vowels])
print(vowels_number)