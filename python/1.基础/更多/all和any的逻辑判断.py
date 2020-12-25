#python3.7
#Filename:all和any的逻辑判断.py

#all(iterable)：集合中的元素 都 为真的时候为真。若为空串返回True
#any(iterable)：集合中的元素 有一个 为真的时候为真。若为空串返回False
a = [1,2,3]
b = [0,1,2]
c = [0,0]
d = []
print(all(a),all(b),all(c),all(d))      #True False False True
print(any(a),any(b),any(c),any(d))      #True True False False
