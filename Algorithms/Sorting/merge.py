arr =  [-5,3,-2,1,6,4,-1,0]


def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    

    sorted_arr = []
    i = j = 0
    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

print(merge_sort(arr))

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Stable: Yes
# In-place: No
# Adaptive: No
# Used in: Merge sort is used in the merge sort algorithm.
