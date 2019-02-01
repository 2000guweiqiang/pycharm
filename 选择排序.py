x=[38,95,1,63,654,46,78,26,11,25,3,66,84,45,8,23,79,100]
print("before:",x)

def selected_sort(x):
    count=len(x)
    for i in range(0,count):
        min=i
        for j in range(i+1,count):
            if x[min]>x[j]:
                x[i],x[j]=x[j],x[i]
    return x
print("after:",selected_sort(x))