# 比再帰 拡張 Euclid の互除法
# 参考 https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a


def modinv(a, b):
    # 初期状態
    # a * u + b * 0 = a
    # a * v + b * 1 = b
    b_raw = b

    u = 1
    v = 0

    while b:
        q = a // b
        u -= q * v
        u, v = v, u

        a -= q * b
        a, b = b, a

    u %= b_raw

    return u


if __name__ == "__main__":
    for i in range(1, 13):
        print(f"{i:2d}, {modinv(i, 13):2d}")
