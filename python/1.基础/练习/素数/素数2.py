#python3.7
#Filename:素数2.py

#返回多少以后的多少个素数

def is_p(t_int):
    """
    #判断一个数是否为素数
    """
    if t_int == 1:
        return True
    elif t_int == 2:
        return True
    else:
        for i in range(2,t_int):
            if t_int%i == 0:
                return False
        return True

def get_num(num,num_max):
    """
    返回多少以后的多少个素数
    """
    m = 1
    for i in range(num,num*10**5):
        if is_p(i):
            x = yield i
            if m == num_max:
                break
            else:
                m += 1

l = []
for i in get_num(10**8,100):
    l.append(i)

print(l)

