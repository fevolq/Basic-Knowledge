#python3.7
#Filename:插入排序.py

def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i]    #选取值
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j]   #选取值较小，则先替换，再继续执行while，直到选取值较大或比到第一个为止
                j -= 1
        arr[j+1] = key      #将选取值插入
  
  
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("排序后的数组:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])

"""
思路：
初始时，arr[j]代表的是选取的值前面的一个数，所以第一次while语句是：
若选取的值比前面小，则交换，若较大，则不交换，
且不再继续执行while(此时的数组，前面的数已经经过比较，是由小到大排列，所以不用再比较)。
while语句不符后，执行的是将选取值插入到刚刚比较后比他小的数的后面，所以比选取值大的数也会逐个往后退一个，
所以，还为进行选取的数的位置(下标)不变。


即：依次选取数作为选取值，与前面的数比较，若选取值小，则继续往前比较，若较大，则将选取值插入到该数之后，再重新选取。
"""










