def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

m = int(input("Enter a number: "))

def prime_numbers(m):
    primes = []
    for i in range(2, m - 1):
        if isprime(i):
            primes.append(i)
    return sum(primes)

print(prime_numbers(m))
