## head-dump

### Description 
Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.
The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.
Additional details will be available after launching your challenge instance.

要約すると、APIドキュメンテーションに関する記事を含むブログサイトを探索して、Flagを探してね。

---

早速、webサイトにアクセスする。  
下のようなwebサイトが開く。

![](./head-dump(1).png)

\#API Documentation をクリックすると、/api-docs/ に遷移。
APIのドキュメントが開けた。

![](./head-dump(2).png)

怪しい名前 Diagnosingの/headdump がある。
実行してみる。データがダウンロードできた。
picoCTFのWebshellでcurlを叩いて、grepでFlagがないか調べる。  

```bash
curl -X 'GET'   'http://verbal-sleep.picoctf.net:50153/heapdump'   -H 'accept: */*' | grep picoCTF{
```

Flagがゲットできた。