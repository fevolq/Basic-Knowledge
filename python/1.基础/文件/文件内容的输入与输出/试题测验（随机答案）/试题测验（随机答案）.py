#!/usr/bin/python3.7
#Filename:试题测验（随即答案）.py

"""
制作6份试题
每份试题都是将题库中的题随机打乱排序
且不同试卷的同一题的正确答案选项随机
输出6份试卷和相对应的答案，以及一份试题库
"""

import random       #内置的随机模块

#试题库
tests = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9}      #所有测验的问题即答案文本
import pprint
testsFile = open("试题库.txt","w")
testsFile.write(pprint.pformat(tests))
testsFile.close()

for questNum in range(6):   #一共6份试题
    #创建试题文件和答案文件
    questFile = open("试题%s.txt"%(questNum + 1),"w")      #创建试题文件
    answerFile = open("答案%s.txt"%(questNum + 1),"w")     #创建答案文件

    #对试题文件写入相同的格式
    questFile.write("名字：____\n\n日期：____\n\n分数：____\n\n")
    #questFile.write("第%s份试题"%(questNum+1))
    questFile.write("\n\n")

    #准备工作：抽出题目，抽出答案
    tests_key = list(tests.keys())       #将所有题目放到一个列表中
    random.shuffle(tests_key)       #随机打乱题目
    tests_value = list(tests.values())     #将所有答案放到一个列表中
    #print(tests_value)

    #一份试题
    for i in range(9):      #每份试题有9道题目
        #一道题的构造
        question = tests_key[i]     #在题目列表中拿题目（key）
        correctAnswer = tests[question]     #在题库文本中匹配正确答案（value）
        test_value = tests_value[:]     #因为列表可变，所以需要copy一份
        del test_value[test_value.index(correctAnswer)]   #在所有答案中删除正确的
        wrongAnswers = random.sample(test_value,3)      #随机抽取3个错误答案（去除了正确的）
        answers = [correctAnswer] + wrongAnswers        #将4个答案组成列表
        random.shuffle(answers)

        questFile.write("%s. %s对应的是__?\n"%(i+1,question))

        for m in range(4):  #4个选项
            questFile.write("%s.%s\n"%("ABCD"[m],answers[m]))
            questFile.write("\n")
        
        #每份试题对应的答案文本
        answerFile.write("%s.%s\n"%(i+1,"ABCD"[answers.index(correctAnswer)]))
    questFile.close()
    answerFile.close()


print("Done")
