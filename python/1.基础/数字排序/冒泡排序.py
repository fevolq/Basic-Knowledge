#python3.7
#Filename:冒泡排序.py

def bubbleSort(arr):
    n = len(arr)
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :  #若较大，则放后面
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i])
    
#print(" ".join(arr))   #TypeError，join需要的是一个字符串列表（元素为字符串）

"""
思路：
i = 0 时：j：(0,n-1)，大的往后排，此时只能找出最大的
i = 1 时：j：(0,n-2)，最大的在最后一个，可以排除比较，所以是n-2
依次类推，每次都找出比较的所有数里最大的，放在（“最”）后面。

即：经过比较，找出最大的，放在最后面，然后再重新比较(去掉最后哪个最大的)，
找出剩下的数组内最大的，放在倒数第二个，然后重复执行。
"""
