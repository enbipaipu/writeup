
## a8tsukuctf
### 問題文
適当な KEY を作って暗号化したはずが、 tsukuctf の部分が変わらないなぁ...

---

事前に渡されるもの
- output.txt : 暗号文
- enc.py : 暗号化するpythonファイル

問題文から
- 平文には、tsukuctfという文字列が含まれる。
- 暗号化前後で、tsukuctfという文字列が変化しない。

output.txtの中身から
- この問題の題名の通り、tsukuctfという文字列の前に8個の`a`がある

enc.pyの中身から
- wikipediaのurlがあり、ビジュネル暗号が使われている
- keyが足りなくなったら、暗号文の先頭の文字から順にkeyとする。
    - keyの長さが、10。平文の長さが30のとき、
    - 平文の10文字目まではkeyで暗号化する
    - 平文の11文字目からは暗号文の1文字目からkeyとして使う。

```python
    for c in plaintext:
        if c in string.ascii_lowercase:
            if idx < len(key):
                k = key[idx]
            else:
                k = cipher_without_symbols[idx - len(key)]
            cipher_without_symbols.append(f(c, k))
            ciphertext.append(f(c, k))
            idx += 1
        else:
            ciphertext.append(c)
```

ここまでの情報を整理
- ビジュネル暗号で、暗号化の前後で文字列が変わらないのは、keyが`a`だから
- keyが足りなくなったら、暗号文をkeyとして使う。
- tsukuctfの長さは、8
- 暗号文のtsukuctfの前には、8つの`a`がある

推論
-  暗号文のtsukuctfの前にある、8つの`a`を使って、平文のtsukuctfが暗号化されている。

暗号文
```
ayb wpg uujmz pwom jaaaaaa aa tsukuctf, hj vynj? mml ogyt re ozbiymvrosf bfq nvjwsum mbmm ef ntq gudwy fxdzyqyc, yeh sfypf usyv nl imy kcxbyl ecxvboap, epa 'avb' wxxw unyfnpzklrq.
```

使うツール
- cryptii : https://cryptii.com/pipes/vigenere-cipher


暗号文は、tsukuctfからの文字列
```
tsukuctf, hj vynj? mml ogyt re ozbiymvrosf bfq nvjwsum mbmm ef ntq gudwy fxdzyqyc, yeh sfypf usyv nl imy kcxbyl ecxvboap, epa 'avb' wxxw unyfnpzklrq.
```


keyは、8個のaからの文字列。keyが暗号文より多くならないように気をつける。
```
aaaaaaaatsukuctfhjvynjmmlogytreozbiymvrosfbfqnvjwsummbmmefntqgudwyfxdzyqycyehsfypfusyvnlimykcxbylecxvboapepaavbwxxwuny
```

平文
```
tsukuctf, or both? the flag is concatenate the seventh word in the first sentence, the third word in the second sentence, and 'fun' with underscores.
```
1文目の7番目の単語は、`tsukuctf`  
2文目の3番目の単語は、`is`
それと `fun` という単語を `_` でつなげてFlagができるようだ。  

`TsukuCTF25{tsukuctf_is_fun}`  
正解した。