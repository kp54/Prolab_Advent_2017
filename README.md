# FizzBuzzで遊ぼう
この文書は[Prolab Advent Calendar 2017](https://adventar.org/calendars/2526)の4日目として執筆されました.  
前日は宮野さんです. [[ペンタブを買いました - Miyanoji Rapid](http://miyanojirapid.vsw.jp/tsurezure/2017/12/adventcalendar-12-3/)]  
面白い記事を期待されているらしいですが僕は平常運行です. 申し訳ない.
## FizzBuzz [#とは](https://twitter.com/search?q=%23とは)
[Fizz Buzz - Wikipedia](https://ja.wikipedia.org/wiki/Fizz_Buzz)  
一人づつ1から順番に数字を読み上げていきますが, 3で割り切れる場合は代わりに'Fizz', 5で割り切れる場合は'Buzz', 15で割り切れる場合は'FizzBuzz' と発言するというゲームです.  
初歩的なプログラミングの問題として扱われることも多々あります.  
今回はこのFizzBuzzを題材として少しだけ遊んでみようと思います.
## 色々書いてみる
### #1
まずは普通になんの捻りもなく書きます. いわゆる模範解答です.
```python
for i in range(1, 16):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
```
### #2
1つ目のコードにわずかに変更を施すと, 15の倍数の判定を取り除けます.
```python
for i in range(1, 16):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            print('Fizz', end='')
        if i % 5 == 0:
            print('Buzz', end='')
        print()
    else:
        print(i)
```
しかし, 長ったらしいif文が増えてしまいました.
### #Fizz
空文字列がFalse判定されることを利用して, 以下のように簡略化できます.
```python
for i in range(1, 16):
    s = ''
    if i % 3 == 0:
        s = s + 'Fizz'
    if i % 5 == 0:
        s = s + 'Buzz'
    print(s or i)
```
そろそろ(黒か白かはともかく)魔術に片足突っ込んでる気がしなくもない.  
Pythonのorの"Boolとして判定してTrueであれば値をそのまま返す"仕様を利用しています.  
Fizzの処理を行っている箇所は
```python
    if i % 3 == 0:
        s = 'Fizz'
```
としてしまっても問題ないのですが, 見た目の美しさを優先しました.
### #4
お待たせしました, ワンライナータイムです.
```python
print('\n'.join(['FizzBuzz' if not i%15 else 'Buzz' if not i%5 else 'Fizz' if not i%3 else str(i) for i in range(1,16)]))
```
リスト内包表記を利用して"1, 2, Fizz, ..."となるリストを生成し, 改行文字で繋いで出力しています.
しかし, まだまだ見た目が冗長です.
### #Buzz
短絡評価を利用してif文を排除, リストを組むのではなくその場で出力するように.
```python
[(not(i%3 and i%5)or print(i))and((not i%3 and print('Fizz',end=''))or(not i%5 and print('Buzz',end=''))or print())for i in range(1,16)]
```
もはや書いた人以外読めません. 書いた自分もよくわかってません.(ｵｲ  
print()がNoneを返す(=Boolとして判定するとFalseになる)ことを利用しています.  
実はロジックとしては#2のコードと完全に等価です.
### #Fizz
```python
[(all([i%3 or print('Fizz',end=''),i%5 or print('Buzz',end='')])or print())and print(i) for i in range(1,16)]
```
組み込み関数allを利用することによって, "Fizz, Buzz双方とも処理を実行しつつ, どちらかでも実行されていれば分岐を行う"という挙動を実現しています.
### #7
文字列連結とかしてみる.
```python
[print(((lambda x:'' if x%3 else 'Fizz')(i)+(lambda x:'' if x%5 else 'Buzz')(i))or i)for i in range(1,16)]
```
lambdaとifをうまく使うことでスッキリした見た目になりました.
## 最後に
Pythonはちょっとしたデータ処理にかなり便利な言語なのでぜひ使いましょう.  
翌日はふなちさんです. 色々と期待してます.
