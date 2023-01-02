def gcd(a, b):
    # euclid の互除法
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(10, 3))
