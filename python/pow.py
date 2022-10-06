def pow(x, y, mod=None):

    if y == -1:
        y = mod - 2

    res = 1
    xx = x
    while y > 0:

        if y & 1:
            res *= xx
        if mod:
            res %= mod

        y >>= 1

        xx *= xx
        if mod:
            xx %= mod

    return res


if __name__ == "__main__":
    print(pow(2, 10, 3))
