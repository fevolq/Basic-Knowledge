#python3.7
#Filename:素数1.py

#返回一个多少以内的所有素数

def p(t):
    if t==1:
        l = [1]
    elif t==2:
        l = [1,2]
    elif t<=0:
        return "请输入一个正整数"
    else:
        l = [1,2]
        for x in range(3,t+1):
            for y in range(2,x):
                if x%y ==0:     #只要有除尽的，就不是，然后重新迭代下一个数
                    break
            if y == x-1:
                l.append(x)
        l.sort()
    #print(l)
    return l

print(p(10**4))




def is_p(t_int):
    """
    判断一个数是否为素数
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

def get_num(num_max):
    """
    返回多少以内的素数
    """
    return [i for i in range(1,num_max+1) if is_p(i)]

#print(get_num(100))
    

    
