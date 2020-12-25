#python3.7
#Filename:enumerate的使用.py

a = [1,2,3,4,5,6]

b = enumerate(a)

def next_():
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))

def for_():
    for i in b:
        print(i)

if __name__ == '__main__':
    for_()
        
    
#enumerate(sequence[,start=0]) ——sequence是一个可迭代对象
#返回一个可枚举的对象，该对象的next()方法将返回一个tuple。
    #tuple由两个元素组成。第一个为sequence中的元素所对应的索引，第二个为这个元素。


