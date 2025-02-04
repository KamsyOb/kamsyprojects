n = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = 0
for i in n:
    if i in vowels:
        count += 1

print(count)
