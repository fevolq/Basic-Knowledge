#复利
def a(months,money,earn):
    i = 1
    alls = 0
    while i <= months:
        alls = (alls + money)*(1 + earn)
        i = i + 1
    return alls

#提取利息
def b(months,money,earn):
    i = 1
    earns = 0
    alls = 0
    while i <= months:
        earns = earns + i * money * earn
        i = i + 1
    alls = money * months + earns
    return alls

if __name__ == '__main__':
    months = int(input('总月数：'))
    money = int(input('单月定投金额：'))
    earn = float(input('月利率：'))
    a1 = a(months,money,earn)
    b1 = b(months,money,earn)
    print('总投资金额：',money*months)
    print('复利总额：',a1)
    print('提取利息的总额：',b1)
'''
总月数：36
单月定投金额：2000
月利率：0.1
总投资金额： 72000
复利总额： 658078.971723156
提取利息的总额： 205200.0
'''
