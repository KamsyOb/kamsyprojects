def is_harshad(num):
    #check if number is harshad number
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

def find_nth_harshad(n):
    #Find the nth Harshad number
    count = 0
    num = 1
    while True:
        if is_harshad(num): #if it is a harshad
            count += 1 #add 1 to the count
            if count == n: #if we get the number we want
                return num #print the number
        num += 1 

# Ask the user to input the desired nth Harshad number
n = int(input("Please enter the position (n) of the Harshad number you want: "))
nth_harshad = find_nth_harshad(n)

print(f"The {n}th Harshad number is: {nth_harshad}")
