word1 = input("Enter your first word: ")
word2 = input("Enter your second word: ")

def check(word1, word2):
    # Check if all characters in word1 are in word2
    for char in word1:
        if char not in word2:
            print("Sorry, the first word cannot be created from the second word")
            return
    print("The first word can be created using the letters from the second word")



check(word1, word2)
