# coding:utf-8

import os

print (__file__)

# 获取当前脚本的真实路径
curpath = os.path.realpath(__file__)
print (curpath)

# 获取当面脚本名称
name = os.path.basename(curpath)
print (name)

# 获取当前脚本的文件夹
file_path = os.path.dirname(curpath)
print (file_path)

# 获取当前文件夹得上一级文件夹
par_path = os.path.dirname(file_path)
print (par_path)

# 拼接文件路径，获取其他文件路径
ta_path = os.path.join(file_path, "123")
print ta_path

t = os.path.exists(ta_path)
print t

if not t:
    os.mkdir(ta_path)

n = os.path.join(ta_path, "1231.txt")
fp = open(n, "w")
fp.write("2222222")
fp.close()
#
# filename = ta_path = os.path.join(file_path, "123.txt")
# fp = open(filename, "r")
# print fp.read()
# fp.close()



