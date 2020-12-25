#python3.7
#Filename:字符替换.py

a1 = "a啊b</p><p> 吧  66"

b1 = a1.replace("</p><p>","1")
b2 = a1.replace("</p><p>","")

c1 = a1.replace("b","6")
c2 = b1.replace("b","6")

d1 = a1.replace(" ","")   #替换空格

print("a1:",a1)
print("b1:",b1)
print("b2:",b2)
print("c1:",c1)
print("c2:",c2)
print("d1:",d1)
