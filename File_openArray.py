#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
create by Kaname Takano
ファイルを開けて多次元配列で返すモジュール
file:開けたいファイル
split:分割する文字列
'''
import sys


def file_open(file, split):
    data = []
    try:
        f = open(file, 'r', encoding='utf-8')
    except Exception:
        print("open error. not found file:", str(file))
        sys.exit(1)
    for line in f:
        line = line.strip() #前後空白削除
        line = line.replace('\n','') #末尾の\nの削除
        line = line.split(split) #分割
        data.append(line)
    f.close()

    return data

if __name__ == '__main__':
    data = file_open("test.txt", '   ')
    print(data)