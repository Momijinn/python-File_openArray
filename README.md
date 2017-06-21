# python-File_openArray
pythonにてファイルを開き、多次元配列を返却するライブラリ

# 動作環境
* python 3.5系
* python2.7系でも動くが、日本語は文字化けをする

# 使い方
解析したいファイルを作成します

一行をsplitで分割をするので、分割をしたい単語もしくは文章の間に特定の文字列を入れてください

exampleではスペース3個で分割するようにしています

## example(test.txt)
```
1   hello
2   test
3   python
4   windows
```

あとはライブラリをインポートし、下記のように記述すれば多次元配列を返してくれます

## example.py
```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import File_openArray as FA

out = FA.file_open("test.txt", "   ") #FA.file_open(file_name, split)
print(out) #[['1', 'hello'], ['2', 'test'], ['3', 'python'], ['4', 'windows']]
```