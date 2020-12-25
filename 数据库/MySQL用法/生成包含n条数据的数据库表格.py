#python3.7
#生成包含n条数据的表格

import pymysql
import random,string

#连接数据库
db = pymysql.connect(host='localhost',user='root',password='mysql',db='test',port=3306,charset='utf8')
#使用test库的something表格
cursor = db.cursor()   #游标对象

#插入数据
def insert(name,score,sex,age):
    sql_insert = 'insert into something(name,score,sex,age) values(%s,%s,%s,%s)'
    try:
        cursor.execute(sql_insert,(name,score,sex,age))
        db.commit()
    except Exception as e:
        print('插入数据错误')
        raise e

l = list(string.ascii_letters)      #包含所有字母大小写的列表

def Name():
    name = random.choice(l)
    return name

def Score():
    score = random.randint(50,100)
    return score

def Sex():
    sexs = ['male','female']
    sex = random.choice(sexs)
    return sex

def Age():
    age = random.randint(18,30)
    return age

def main(n):
    for i in range(n):
        insert(Name(),Score(),Sex(),Age())
    db.close()
    print("插入了{}条数据".format(i+1))

if __name__ == '__main__':
    n = int(input("需要多少条数据："))
    main(n)
    print('\nDone')












