def vigenere_crib_attack(ciphertext, crib, crib_position):
    """
    ciphertext: 暗号文（英小文字のみ、記号やスペースも含めてOK）
    crib: 既知の平文（クリブ、例: 'tsukuctf'）
    crib_position: クリブが暗号文中に現れる位置（インデックス、0始まり）
    戻り値: cribに対応する鍵部分の文字列
    """
    key_fragment = ""
    for i in range(len(crib)):
        c = ciphertext[crib_position + i]
        p = crib[i]
        if c.isalpha() and p.isalpha():
            # 小文字前提
            k = (ord(c) - ord(p)) % 26
            key_fragment += chr(ord("a") + k)
        else:
            key_fragment += "?"
    return key_fragment


# 例
ciphertext = "ayb wpg uujmz pwom jaaaaaa aa tsukuctf, hj vynj? mml ogyt re ozbiymvrosf bfq nvjwsum mbmm ef ntq gudwy fxdzyqyc, yeh sfypf usyv nl imy kcxbyl ecxvboap, epa 'avb' wxxw unyfnpzklrq."
crib = "tsukuctf"
crib_position = ciphertext.index(crib)  # 「tsukuctf」が現れる位置を自動で取得

key_fragment = vigenere_crib_attack(ciphertext, crib, crib_position)
print(f"鍵のこの部分: {key_fragment}")
