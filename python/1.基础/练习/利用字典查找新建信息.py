#!/usr/bin/python
#Filename.利用字典查找新建信息.py

tel = {'a':1,'b':2,'c':3}

while True:
    x = input('请输入“新建（new）”、“删除（del）”、“查找（search）”或“离开（leave）”：')

    if x == '新建' or x == "new":
        name1 = input('\n请输入姓名：')
        y = input('请输入信息：')
        tel[name1] = y
        print('已保存\n')
        m = input('请输入“继续（again）”或“离开（leave）”：')
        if m == '继续' or m == "again":
            continue
        else:
            break
        
    elif x == '删除' or x == "del":
        name2 = input('\n请输入姓名：')
        del tel[name2]
        print('已删除\n')
        m = input('请输入“继续（again）”或“离开（leave）”：')
        if m == '继续' or m == "again":
            continue
        else:
            break
        
    elif x == '查找' or x == "search":
        name3 = input('\n请输入姓名：')
        print('%s的信息是：%s'%(name3,tel[name3]),'\n')
        m = input('请输入“继续（again）”或“离开（leave）”：')
        if m == '继续' or m == "again":
            continue
        else:
            break
        
    elif x == '离开' or x == "leave":
        break
    else:
        continue

print('\nDone')
        
