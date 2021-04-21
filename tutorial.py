# もとのサイトのリンク
# https://colab.research.google.com/github/chainer/tutorials/blob/master/ja/02_Basics_of_Python.ipynb

# 変数
# 数字や文字を一時的に入れておける箱のようなものです。
a = 1   # aという変数に1を格納
print(a)    # aの値を出力し確認

# コメント
# 文の前にハッシュ(#)をつけることで、コメントを書くことができます。
# これは、プログラムの動作に影響を与えることはありません。
'''
また、複数行にわたるコメントは、シングルクォート3つでくくることでまとめてコメントとして書くことができます。
知っていると便利です。
'''

# 型
# 変数には種類があり、整数(Integer)、浮動小数点数(Floating-point number)、文字列(String)があります。
a = 1   # 整数(int)
b = 1.5    # 浮動小数点数(float)
c = 'String'    # 文字列(str)、シングルウォート(')かダブルクォート(")で囲うと文字列となる。
# 中身と型を確認してみよう。すこし実用的なprint文で書いてみようと思う。
print('aの値は' + str(a) + 'で、型は' + str(type(a)) + 'です。')    # Stringに変換して文字列の足し算として出力するパターン
print('bの値は{}で、型は{}です。'.format(b, type(b)))    # .format()を使うパターン
print(f'cの値は{c}で、型は{type(c)}です。')    # f-stringを使うパターン

# 複数同時の代入
# 先ほどではa、b、cをそれぞれで代入しましたが、1行で代入することもできます。
a, b, c = 1, 1.5, 'String'

# 四則演算の演算子
'''
足し算 +
引き算 -
掛け算 * (アスタリスク)
割り算 /
'''
a, b = 2, 3    # 変数を用意しておく
print(a + b)    # 足し算 出力は 5
print(a - b)    # 引き算 出力は -1
print(a * b)    # 掛け算 出力は 6
print(a / b)    # 割り算 出力は 0.6666666666666666

# 比較演算子
'''
小なり <
大なり >
以下 <= (小なりイコール)
以上 >= (大なりイコール)
等しい == (イコールイコール)
等しくない != (ノットイコール)

True : 正しい
False : 誤り
'''
print(1 < 2)    # True
print(1 > 2)    # False
print(1 <= 2)   # True
print(1 >= 2)   # False
print(1 == 2)   # false
print(1 != 2)   # True

# エスケープシーケンス(特殊文字)
# 特殊な文字をパソコンに認識させるために書く文字列のことです。
'''
\n : 改行
\t : タブ(空白*4)
'''
print('Hello\nWorld')   # 改行されたHello Worldが出力される
print('Hello\tWorld')   # ソーシャルディスタンスHello World

# Stringを大文字小文字に操作
# Stringの変数は、.upper()で大文字に、.lower()で小文字に変換できます。
name = 'String'
print(name)    # String
print(name.upper())    # STRING
print(name.lower())   # string

# 配列(List)
# 変数が箱だったのに対して、配列はタンスのようなイメージです。
'''
イメージ
配列 : タンス
インデックス(添字) : 何番目の引き出しか。ただし最初は0番目。-がつくと後ろから何番目となる。
例) list[1] -> 1番目の引き出し
'''
'''
よく使う機能や関数
:(コロン) : 1:3と書くと"1から3"という風に使える
len() : 配列の長さ
.append() : 配列の末尾に値を追加
'''
numbers = [1, 2, 3]    # 配列を宣言
print(numbers[0])      # 1
print(numbers[-1])     # 3
numbers.append('rf')   # numbersの末尾に文字列rfを追加
print(numbers)         # [1, 2, 3, 'rf']
print(numbers[2:])     # [3, rf]
print(numbers[:])      # [1, 2, 3, 'rf']

# タプル(Tuple)
# 配列の中身変更できないバージョン

# 辞書(Dictionary)
'''
辞書型には、キー(Key)と値(Value)を並べて宣言します。
キーを参照すると、値が返ってきます。
'''
scores = {'Math': 90, 'Science': 75, 'English': 80 }
print(scores['Math'])    # 90
print(scores['English']) # 80

# if文、elif文、else文
# 特定の条件でプログラムを分岐させたいときに用います。
name = 'Masaki'
if name == 'Tomoya':    # もしnameが'Tomoya'なら
    print('Your name is Tomoya')
elif name == 'kaito':   # もしnameが'Tomoya'ではなく'Kaito'なら
    print('Your name is Kaito')
else:                   # それ以外なら
    print('I do not know your name.')

# ここから下はこのプログラムの先頭にあるリンクのところを参照してください。