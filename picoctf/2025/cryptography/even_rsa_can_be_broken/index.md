## EVEN RSA CAN BE BROKEN
### Description

This service provides you an encrypted flag. Can you decrypt it with just N & e?
Connect to the program with netcat:
$ nc verbal-sleep.picoctf.net 51434

要約すると、Nとeだけから平文を求めることができるか？

---

webシェルで、コードを実行してみる。`nc verbal-sleep.picoctf.net 51434`を入力。
下の実行結果と、提供されているソースコードから脆弱な部分を探す必要がある。

```sh
$ nc verbal-sleep.picoctf.net 51434
N: 24455939012508150522461604701960221761452972621364100610345155521699608763891562889709197043290029837345927486420667606789058236974618054388923732714432142
e: 65537
cyphertext: 22362518143570741332775475556167362105556968252846420248639995419508478702221589413920129151925187082020944541842475608870900795195400043000490909975037115
```

```python
# ソースコード
from sys import exit
from Crypto.Util.number import bytes_to_long, inverse
from setup import get_primes

e = 65537

def gen_key(k):
    """
    Generates RSA key with k bits
    """
    p,q = get_primes(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)

def encrypt(pubkey, m):
    N,e = pubkey
    return pow(bytes_to_long(m.encode('utf-8')), e, N)

def main(flag):
    pubkey, _privkey = gen_key(1024)
    encrypted = encrypt(pubkey, flag) 
    return (pubkey[0], encrypted)

if __name__ == "__main__":
    flag = open('flag.txt', 'r').read()
    flag = flag.strip()
    N, cypher  = main(flag)
    print("N:", N)
    print("e:", e)
    print("cyphertext:", cypher)
    exit()
```

複数回実行してみると、Nの1桁目が必ず2の倍数になっている。  
N = p * q (pとqは互いに素) なので、素数の片方が**2で固定**されていることがわかる。  
これよって、p=2、q=N//p で2つの素数が求まる。

ここから、秘密鍵が求められるので、RSAの秘密鍵を作り、暗号文を復号する。  
下を実行する。  
Flagがゲットできた。

```python
from Crypto.Util.number import long_to_bytes


def main():
    p = 2
    e = 65537
    N = 24455939012508150522461604701960221761452972621364100610345155521699608763891562889709197043290029837345927486420667606789058236974618054388923732714432142
    cy = 22362518143570741332775475556167362105556968252846420248639995419508478702221589413920129151925187082020944541842475608870900795195400043000490909975037115

    q = N // 2
    ku_ = (p - 1) * (q - 1)
    d = pow(e, -1, ku_)
    decrypted_long = pow(cy, d, N)
    decrypted_bytes = long_to_bytes(decrypted_long).decode()
    print(f"ans: {decrypted_bytes}")


if __name__ == "__main__":
    main()
```
