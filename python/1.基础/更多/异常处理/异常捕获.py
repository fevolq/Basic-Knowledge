#python3.7
#Filename:异常处理.py

#try ... except语句

while True:
    try:
        a = int(input("输入一个数："))
    except ValueError:
        print("重新试试")
    except (RuntimeError,TypeError,NameError):      #多个异常
        pass        
    except:
        print("异常",a)     #最后一个except子句可以忽略异常的名称，它被当作通配符使用。
                            #可以使用它打印一个错误信息，并将异常再次抛出。
        raise
    else:
        b = 1
        print(a+b)            #try except语句有一个可选的else子句。若有，则必须放在所有except之后。
                     #else将在try子句没有异常时执行。使用else可以避免把所有语句都放在try子句中。避免except没有捕捉的异常。
    finally:        #finally语句，无论有没有异常，都会执行
        pass
    break

"""
先执行try的子句，若没有异常，则忽略所有except子句，继续往下执行。
                 若发生异常，则忽略try子句内余下的部分。
如果异常的类型和except后的名称相符，则执行对应的except子句。
最后执行try...except语句后的代码。
执行顺序：try—>except X—>except—>else—>finally
"""
#一个try语句可能包含多个except子句，用来针对处理try子句中的不同的异常（能处理子句中调用的函数的异常）。
#最多只有一个分支会被执行。
#一个except子句可以同时处理多个异常，这些异常将被放在括号内成为一个元组。

"""
错误类型：

ValueError 传入不期望值

NameError 使用一个未被赋予对象的变量

AttributeError 不存在属性

IoError  输入或输出异常

ImportError 无法引入模块或包。（一般是路径问题或模块名称有误）

IndentationError 语法错误（SyntaxError子类），一般是代码缩进错误

KeyError 字典中不存在关键字

KeyboardInterrupt Ctrl+C被按下

SyntaxError 语法错误

TypeError 传入对象类型与要求不符

UnboundLocalError 变量作用域的问题

"""
