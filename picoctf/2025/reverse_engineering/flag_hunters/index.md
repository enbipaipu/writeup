## Flag Hunters

### 問題文
Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you.
The program's source code can be downloaded here.
Connect to the program with netcat:
`$ nc verbal-sleep.picoctf.net 59014`

---

この問題は、ソースコードが配布されている。  
実際に動かしてみると、文字列の途中から表示され始める。  
そして、下のコードが今回大きく関わってくるところだ。

```python
  line_count = 0
  lip = start
  while not finished and line_count < MAX_LINES:
    line_count += 1
    for line in song_lines[lip].split(';'):
      if line == '' and song_lines[lip] != '':
        continue
      if line == 'REFRAIN':
        song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
        lip = refrain
      elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])
      elif line == 'END':
        finished = True
      else:
        print(line, flush=True)
        time.sleep(0.5)
        lip += 1
``` 
ここを読むに、`;`区切りで文字列のをlineに格納して、  
lineの値によって、次に行う動作が変わってくるようだ。  
そして、文字列は改行ごとに分割して、song_linesに格納されている。  
flagは、4行目あたりにあるので、0行目から順に出せばゲットできそう。
そして、lipの値によって、どの行を取り出すかを決めている。

これらの情報から`something;RETURN 0`を入力する。
Flagがゲットできた。
