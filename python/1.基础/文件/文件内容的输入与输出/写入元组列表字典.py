#!/usr/bin/python3.7
#Filename:写入元组列表字典pprint.py

#内置的open——write只能写入字符（串）型

a = (1,2,3)
b = [4,5,6]
c = {"q":7,"w":8,"e":9}
d = "qwert"
e = 666

#使用内置的pprint模块中的pformat()函数
import pprint
txt = open("写入元组列表字典.txt","w")

txt.write(pprint.pformat(a))        #或txt.write(str(a))
txt.write(pprint.pformat(b))        #写入时不会自动换行
txt.write("\n")
txt.write(pprint.pformat(c))
txt.write("\n")
txt.write(d)
txt.write("\n")
txt.write(pprint.pformat(d))        #与上一步比较
txt.write(pprint.pformat("呵呵"))         #与d比较
txt.write("\n")
#txt.write(e)——异常
txt.write(str(e))
txt.write("\n")
txt.write(pprint.pformat(e))            #与e比较，为整型
txt.write("\n")
txt.write(pprint.pformat("666"))        #为字符(串)型

txt.close()


print("Done")

#pprint写入字符型，则写入的内容有引号，写入整形（或元组、列表、字典），则没有引号
#write只能写入字符型，没有引号。若为其他型，需str转换
