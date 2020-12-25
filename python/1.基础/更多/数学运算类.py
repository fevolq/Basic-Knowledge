#python3.7
#Filename:数学运算类.py

#abs(x)：求绝对值。参数可是整型，也可是复数（返回模）
print(abs(-6),abs(2+3j))    #6   3.605551275463989

#complex([real,[imag]])：创建一个复数
print(complex(2,3))         #(2+3j)

#divmod(a,b)：两个数相除，分别取商和余数。整型、浮点型都可以
print(9,5)                  #9   5

#float([x])：将一个字符串或数转换为浮点数。如果无参数，将返回0.0
print(float(),float(6),float('35'))     #0.0   6.0   35.0

#int([x[,base]])：将一个字符转换为int型，base表示进制。无参数返回0
print(int(),int('66'))      #0   66

#pow(x,y[,z])：返回x的y次幂
print(pow(2,3))             #8

#range([start],stop[,step])：产生一个可迭代序列，没有start则从0开始，不包括stop这个数
range(1,10,3)

#round(x[,n])：四舍五入。n可选，n为0，则四舍五入，否则保持不变。有n则保留初始的小数位数
print(round(3.9),round(3.9,0),round(3.9,1))     #4   4.0   3.9

#sum(iterable[,start])：对可迭代对象求和
List = [1,2,3,4]
print(sum(List),sum(List,6))    #10   16

#oct(x)：将一个数字转化为8进制
print(oct(21))                  #0o25

#hex(x)：将整数x转化为16进制字符串
print(hex(21))                  #0x15

#bin(x)：将整数x转化为二进制字符串
print(bin(21))                  #0b10101

#chr(x)：返回整数x对应的ASCII字符
print(chr(21))                  #

#bool([x])：将x转换为Boolean类型
print(bool(),bool(6),bool('a'))           #False  True  True
