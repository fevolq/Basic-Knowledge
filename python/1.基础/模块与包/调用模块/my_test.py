#!/usr/bin/python
# Filename：my_test.py

def sayhi():
    if __name__ == '__main__': 
        print('这是本地的模块')
    else:
        print('这是导入的模块')

v = '0.1'
print("嘿嘿")

if __name__=="__main__":
    sayhi()
