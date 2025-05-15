arr =  [-5,3,-2,1,6,4,-1,0]

def quick_sort(arr):
    if(len(arr)<=1):
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x<pivot]
    right = [x for x in arr if x>pivot]

    L = quick_sort(left)
    R = quick_sort(right)
    return L+[pivot]+R

print(quick_sort(arr))