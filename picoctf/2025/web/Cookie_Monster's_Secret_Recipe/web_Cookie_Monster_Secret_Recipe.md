## Cookie Monster's Secret Recipe

### Description 

Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?
You can access the Cookie Monster here and good luck

要約すると、クッキーモンスターがレシピをwebサイトの中に隠している。この秘密のレシピを探して！！


---

早速、webサイトにアクセスする。  
下のようなwebサイトが開く。

![](./cookie_monster(1).png)

usernameとpasswordを適当に埋めて、ログインしてみる。  
下のようなサイトが開いた。

![](./cookie_monster(2).png)

ヒント：最近cookiesを見たのはいつですか？と聞かれている。  
開発者ツールでcookiesを開く。

![](./cookie_monster(3).png)

なんか、謎の文字列があった。base64でデコードしてみる。  
```bash
echo -n 'cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzZDMkZCN0YzfQ==' | base64 -d
```

Flagがゲットできた。