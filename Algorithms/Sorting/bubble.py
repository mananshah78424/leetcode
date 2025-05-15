arr =  [-5,3,-2,1,6,4,-1,0]


def bubble_sort(arr):
    flag = True
    while flag: 
        flag = False
        for i in range(1,len(arr)):
            if(arr[i-1]>arr[i]):
                flag = True
                arr[i-1],arr[i] = arr[i],arr[i-1]
    return arr

print(bubble_sort(arr))