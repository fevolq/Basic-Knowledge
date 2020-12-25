#python3.7
#Filename:排序.py

l = []

def Input():
    """
需要比较的数
    """
    print("每输入一个数按下回车，输入“over”结束数字的输入。")
    while True:
        math = input("输入要比较的数：")
        if math == 'over':
            break
        else:
            l.append(int(math))
    return l

def Sort(l):
    print("\n一共有%s个数需要比较"%len(l))
    for x in range(0,len(l)-1):
        for y in range(1+x,len(l)):
            if l[x] < l[y]:
                l[x],l[y]=l[y],l[x]
    print("\n从大到小是：%s"%l)
    l.reverse()
    print("\n从小到大是：%s"%l)

if __name__ == '__main__':
    Sort(Input())
