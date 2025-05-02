ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 26
A = -3  # ax+b の a
B = 25  # ax+b の b


def main():
    result = []
    y_input = input("cr = ")
    for s in y_input:
        y = ALPHABET.find(s)  # アルファベット -> 数値
        x = pow(y - B, 1, MOD) * pow(A, -1, MOD)  # x = (y - b) / a (mod 26)
        result.append(ALPHABET[pow(x, 1, MOD)])  # 数値 -> アルファベット
    print("".join(result))


if __name__ == "__main__":
    main()
