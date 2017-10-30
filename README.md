python-File_openArray
====
pythonにてファイルを開き、多次元配列を返却するライブラリ

## Description
Pythonにてデータが格納してあるファイルを開き多次元ファイルを返却するライブラリ

## Demo
ターゲットファイル
```
//test.txt
1   hello
2   test
3   python
4   windows
```
```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import File_openArray as FA

out = FA.file_open("test.txt", "   ") #FA.file_open(file_name, split)
print(out) #[['1', 'hello'], ['2', 'test'], ['3', 'python'], ['4', 'windows']]
```


## Requirement
* 動作環境
    * python 3.5系
    * python2.7系でも動くが、日本語は文字化けをする可能性がある


## Usage
1. 解析したいファイルを作成します

2. 一行をsplitで分割をするので、分割をしたい単語もしくは文章の間に特定の文字列を入れてください

## Install
```python
import File_openArray as FA
```

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Twitter](https://twitter.com/momijinn_aka)

[Blog](http://www.autumn-color.com/)