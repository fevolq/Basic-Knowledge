#python3.7
#Filename:归并排序.py

#l:初始下标，m:分组节点的下标，r：分组后的列表内的最后下标

def merge(arr, l, m, r): 
    n1 = m - l + 1      #m-"l"+1
    n2 = r- m 
  
    # 创建临时数组
    L = [0] * (n1)      #用于/先确定了数组内的元素个数
    R = [0] * (n2)
  
    # 拷贝数据到临时数组 arrays L[] 和 R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i]   #["l" + i]
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j]   #[m + 1 + j]
  
    # 归并临时数组到 arr[l..r] 
    i = 0     # 初始化第一个子数组的索引
    j = 0     # 初始化第二个子数组的索引
    k = l     # 初始归并子数组的索引      #k = "l"
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # 拷贝 L[] 的保留元素
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # 拷贝 R[] 的保留元素
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr,l,r): 
    if l < r:        
        m = int((l+(r-1))/2)
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
  
  
arr = [12, 11, 13, 5, 6, 7] 
n = len(arr) 
print ("给定的数组") 
for i in range(n): 
    print ("%d" %arr[i])
  
mergeSort(arr,0,n-1) 
print ("\n\n排序后的数组") 
for i in range(n): 
    print ("%d" %arr[i])


"""
思路：
先将数组均分两组a、b
在a组内再次均分组，以此类推，最终最先执行的是两个均只包含一个元素的列表（处于递归函数的最内核），
且元素为原数组的第一二个。
这两个列表在merge函数内进行比较，并返回到原数组内进行排序，此步操作完结。
再在递归函数往上一层发展，此时的两个临时列表均含有两个元素，且各自均已排序（元素为前4个），
然后从这两个列表中从前到后抽取元素进行比较，结果返回到原数组内进行排序（排前4个），
当两个临时列表中的某一个抽取完毕，而另一个还有多个元素没有抽取时，就使用“拷贝保留元素”的功能
来赋值给原数组对应下标的元素，到此前4个元素排序完成。此为一次简略完成的程序步骤。

最后依照上面的思路来在递归函数中层层往上运行，最后的运行步骤就是上面的“拷贝保留元素”，
而此时的临时列表是由原数组对半分组成的列表。
"""















    
