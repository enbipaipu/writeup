import string


def f_inv(c, k):
    # 復号: (暗号文文字 - 鍵文字) % 26
    c = ord(c) - ord("a")
    k = ord(k) - ord("a")
    ret = (c - k) % 26
    return chr(ord("a") + ret)


def endode(ciphertext, key):
    p = ""
    idx = 0
    cipher_without_symbols = []
    for c in ciphertext:
        if c in string.ascii_lowercase:
            if idx < len(key):
                k = key[idx]
            else:
                k = cipher_without_symbols[idx - len(key)]
            cipher_without_symbols.append(f_inv(c, k))
            p += f_inv(c, k)
            idx += 1
        else:
            p += c
    return p


# 使用例
ciphertext = "ayb wpg uujmz pwom jaaaaaa aa tsukuctf, hj vynj? mml ogyt re ozbiymvrosf bfq nvjwsum mbmm ef ntq gudwy fxdzyqyc, yeh sfypf usyv nl imy kcxbyl ecxvboap, epa 'avb' wxxw unyfnpzklrq."
key = "rqappgux"


print(endode(ciphertext, key))
