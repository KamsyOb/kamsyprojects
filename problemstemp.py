def is_anagram():
    n = input("Enter a word: ")
    m = input("Enter another word: ")
    list1 = list(n)
    list2 = list(m)
    for i in list1:
        if i in list2:
            list2.remove(i)
    if len(list2) == 0:
        print("True")
    else:
        print("False")

is_anagram()