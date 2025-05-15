arr =  [-5,3,-2,1,6,4,-1,0]


def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if(arr[j]<arr[j-1]):
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else:
                break
    return arr

print(insertion_sort(arr))