#python3.7
#Filename:快速排序.py

#此排序是递归函数由外向内运作
"""##表示个人自己添加的注释"""

def partition(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     ##以最后一个数为基准值，最后将基准值替换到中间
  
    for j in range(low , high): 
  
        # 当前元素小于或等于 pivot 
        if   arr[j] <= pivot:       
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]       
            ##大则原地不动，等待着是否被替换位置
            ##小，则与那些已经比较过后，大的数交换位置
  
    arr[i+1],arr[high] = arr[high],arr[i+1]     ##将基准值替换到中间
    return ( i+1 ) 
  
 
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引
  
# 快速排序函数
def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1)   ##第一个递归
        quickSort(arr, pi+1, high)      ##第二个递归
  
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("排序后的数组:") 
for i in range(n): 
    print ("%d" %arr[i])

"""
思路：
第一次sort函数内的pi中，pa函数会先选取最后一个数为基准值，
（if语句：）然后把前面的数来进行比较，
小的则与a[i]替换（即放到前面部分），大的则不动等待着是否被后面小于的替换，
i表示已经替换了的个数-1，即最后一个替换后的下标。
pa函数剩下的部分则是将最后一个数与最后一个替换的下标（i）后面的一个数交换，则此数前面的都比它小，后面的都比它大。
pa函数返回值为最后一个替换的下标（i）后面的一个数的下标，此下标代表的数是分隔数。

然后在sort函数内进行函数sort的递归，即先将前面的部分(第一个递归)按照pa函数来排序，
然后再将后面的部分(第二个递归)也按照pa函数来排序。

递归函数最内层的是一个元素数量为0或1的列表。
"""


















