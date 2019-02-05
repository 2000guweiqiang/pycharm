def QuickSort(List,low,high):
    #判断low是否小于high,如果为false,直接返回
    if low < high:
        i,j = low,high
        #设置基准数
        pivotkey = List[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (List[j] >= pivotkey):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            List[i] = List[j]

            #同样的方式比较前半区
            while (i < j) and (List[i] <= pivotkey):
                i = i + 1
            List[j] = List[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        List[i] = pivotkey

        #递归前后半区
        QuickSort(List, low, i - 1)
        QuickSort(List, j + 1, high)
    return List


List = [50,10,90,30,70,40,80,60,20]
print(List)
print("Quick Sort: ")
QuickSort(List,0,len(List)-1)
print(List)