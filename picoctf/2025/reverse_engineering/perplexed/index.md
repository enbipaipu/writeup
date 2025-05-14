## perplexed
### 問題文

Download the binary here.

---


問題文が何も無かった。

`wget https://challenge-files.picoctf.net/c_verbal_sleep/2326718ce11c5c89056a46fce49a5e46ab80e02d551d87744306ae43a4767e06/perplexed`  
でバイナリファイルを習得する。

Ghidraを使用して、逆アセンブルしてみる。  
そして、これをGPTでｃ言語に直してもらう。

perplexed.cができた。

これを見ると、local_58の値と、入力値の値が、bitごとにすべて同じであれば、成功するようだ。  

しかし、flagを出力するような機構も無いので、local_58をいい感じに直すと、picoCTF{~}という形のFlagをゲットできることが推論できる。


とりあえず、すべてをビットに変換して、CyberChefで変換してみる。

Flagがゲットできた。