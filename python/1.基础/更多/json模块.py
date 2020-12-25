#python3.7
#Filename:json.py

#注意事项：1.称必须用双引号（即" "）来包括
#          2.值可以是双引号包括的字符串、数字、true、false、null、javaScipt数组，或子对象

import json

#将python对象编码成json字符串——json.dumps()
data = {'name':'嘿嘿',"age":666}      #python对象
print("json对象：",json.dumps(data))     #返回的结果中，变成了双引号


#将json字符串编码成python对象——json.loads()
data = (1,2,3,4)        #python对象
datas = [1,2,3,4]
a = json.dumps(data)    #json对象
b = json.dumps(datas)
print("python对象：",json.loads(a))       #python对象 —— 元组和列表解析出来的均是数组
print("python对象：",json.loads(b))

"""
#将python内置类型序列化为json对象后写入文件
data = {
    'name':'haha',
    'a':[1,2,3,4],
    'b':(1,2,3)
    }
with open('json_test.txt',"w+") as f:
    json.dump(data,f)


#读取文件中的json形式的字符串元素转化为python类型
with open("json_test.txt","r+") as f:
    print("读取文件的json形式转换为python形式：",json.load(f))
"""

"""
json.dumps()	将 Python 对象编码成 JSON 字符串
json.loads()	将已编码的 JSON 字符串解码为 Python 对象
json.dump()	将Python内置类型序列化为json对象后写入文件
json.load()	读取文件中json形式的字符串元素转化为Python类型
"""
