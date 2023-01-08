def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    primes = []
    for i in range(n):
        if not is_prime[i]:
            continue
        primes.append(i)

        j = i * i
        while j + i <= n:
            j += i
            is_prime[j] = False
    return primes
