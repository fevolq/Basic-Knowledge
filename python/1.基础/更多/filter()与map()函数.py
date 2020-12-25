#python3.7
#Filename:filter()与map().py

num_list = range(1,20)

def iseven(l):
    return l%2==0

result = filter(iseven,num_list)
print(list(result))     #注意使用返回值时的方法

"""
filter函数用于筛选序列，filter(func,lst)包含两个参数，
第一个参数为函数，第二个参数为列表，
func作用于lst中每一个元素，根据返回的结果TRUE或者FALSE来决定结果的取舍
"""
print('\n\n')

li = [1,2,3,4,5,6]
a = filter(lambda x:x>3,li)
print(type(a))
print(a)
print(list(a))


print('\n\n\n')

b = [1,2,3,4,5]
def f(x):
    return x**2

res = map(f,b)      #map()函数的第一个参数是函数名，第二个参数一般是列表，第三个可选，一般是列表
print(res)
#print(list(res))
res = [i for i in res if i>10]
print(res)
