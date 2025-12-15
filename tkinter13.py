def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return prime


# Input range
n = int(input("Enter the upper limit: "))

primes = sieve_of_eratosthenes(n)

print("Prime numbers in the given range:")
for i in range(2, n + 1):
    if primes[i]:
        print(i, end=" ")