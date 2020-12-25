#python3.7
#Filename:选择排序.py

A = [64, 25, 12, 22, 11] 
  
for i in range(len(A)): 
    min_idx = i     #min_idx：最小数的索引   #1-1
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j     #先将小的数的索引赋值给min_idx
                
    A[i], A[min_idx] = A[min_idx], A[i]     #1-2
  
print ("排序后的数组：") 
for i in range(len(A)): 
    print("%d" %A[i])


for i in range(len(A)):
    A[i] = str(A[i])   
print(" ".join(A))


"""
思路：
if语句：将最小的数与取得数比较，若取得数更小，则将其索引赋值给最小索引所代表的变量。
第二个for循环：找出需要比较的数组内最小的数的索引值，这个索引值是相对于初始数组而言。
1-2：将比较前的最小项与比较后的实际最小项的数值交换，达到将最小的数(参与比较的数组内)放在前面的目的。

1-1：先将需要比较的数组内的第一个数当作是最小的，用来与后面的比较
第一个for循环：用来依次将原数组的每个数都作为一次“临时最小数”，用来与后面的比较。

即：先找出最小的放在第一个(原第一个相应的移到原最小的位置)，然后找出剩下的最小的放在第二个，依次进行。
"""
