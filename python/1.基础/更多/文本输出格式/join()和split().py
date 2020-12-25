#!/usr/bin/python3.7
#filename:join()和split().py

#join()传递一个字符串列表，返回一个字符串
print("".join(["a","b","1"]))
print("，".join(["a","b","1"]))

print("_-".join(["abc"]))       #列表内只有一个元素，所以连接符没有用
print("_-".join("abc"))     #传递一个字符串

print("abc".join(["1","2","3"]))


print("\n\n")


#split()调用字符串，返回一个字符串列表。
print("我 的 名 字".split())
print("my name is".split( ))    #括号内为空，则默认选择空格、制表符或换行符等空格符进行拆分

print("我a的a名a字".split("a"))
print("my89name89is".split("89"))


