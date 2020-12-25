#!/usr/bin/python
# Filename:sys.argv.py

#此程序在此版本无法运行

import sys              #调用sys模块

def readline(fname):
    '''将文件打印到标准输出
'''
    f = file(fname)         #file为内置的模块，但3版本后以取消。所以下面程序在此版本无法运行
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)
    f.close()               

if len(sys.argv) < 2:       #如果sys模块内的argv列表内的字符串小于2个
    print('没有指定任何行动')
    sys.exit()

if sys.argv[1].startswith('--'):    #如果argv列表内的第二个字符串是以--开始
    option = sys.argv[1][2:]        #--占了两个字符，将列表内的第二个字符串除--外全部赋值
    if option == 'version':
        print('version 1.2')
    elif option == 'help':
        print('''\
该程序将文件打印到标准输出。
可以指定任意数量的文件。
选项包括：
  --  version：打印版本号
  --help：显示此帮助''')
    else:
        print('未知选项')
    sys.exit()
else:
    for fname in sys.argv[1:]:
        readfile(fname)

print('Done')

    
    
