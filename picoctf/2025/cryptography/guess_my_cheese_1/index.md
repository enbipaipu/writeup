## Guess My Cheese (Part 1)
### Description
Try to decrypt the secret cheese password to prove you're not the imposter!
Connect to the program on our server: `nc verbal-sleep.picoctf.net 59244`  
要約すると、パスワードを解読する

---

早速アクセスする

```
The super evil Dr. Lacktoes Inn Tolerant told me he kidnapped my best friend, Squeexy, and replaced him with an evil clone! You look JUST LIKE SQUEEXY, but I'm not sure if you're him or THE CLONE. I've devised a plan to find out if YOU'RE the REAL SQUEEXY! If you're Squeexy, I'll give you the key to the cloning room so you can maul the imposter...

Here's my secret cheese -- if you're Squeexy, you'll be able to guess it:  HUMSUCWBQMW
Hint: The cheeses are top secret and limited edition, so they might look different from cheeses you're used to!
Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
```

暗号化されたチーズ名を復号できれば、Flagをゲットできそう。  
アクセスするたびに暗号文が変わっている。  
どのようにチーズ名が暗号化されているか調べる必要がありそう。  

e を押してみる  
適当なチーズ名を入力する  

```
What cheese would you like to encrypt? cheddar
Here's your encrypted cheese:  ZOFCCTS
Not sure why you want it though...*squeak* - oh well!

I don't wanna talk to you too much if you're some suspicious character and not my BFF Squeexy!
You have 2 more chances to prove yourself to me!

Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
```
cheddar -> ZOFCCTS  
CHEDDAR -> ZOFCCTS  
provolone -> MSJEJAJGF  
pecorino -> MFZJSRGJ  

このような結果になった。  
一瞬、シーザー暗号かと思ったが、うまく復号できなかった。  

ヒントは、`Remember that cipher we devised together Squeexy? The one that incorporates your affinity for linear equations???`  
なにやら線形方程式の暗号が使われていそう。  
そのような暗号を知らないので、Geminiに聞くと、基本的なものに**アフィン暗号**というものがあるらしい。  
アフィン暗号の暗号化式
```
E(x) = (ax + b) mod m
```
アルファベットは26個なので、m=26となり、

複合式は
```
x = (E(x) - b) / a mod m
```
となる。  
変数a, bは、その都度変わるので、手計算で求めて、decode.pyを動かす。  
暗号文からeで入力した値へ復号できることを確認出来たら、下の質問で g を押す

```
What would you like to do?
```

先ほどと同じように暗号化されたチーズ名をdecode.pyに入力する。  
復号されたチーズ名をシェルに入力する。

Flagがゲットできた。