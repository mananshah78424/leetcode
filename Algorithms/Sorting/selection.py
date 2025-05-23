arr =  [-5,3,-2,1,6,4,-1,0]


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i 
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min_index]):
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

print(selection_sort(arr))

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Stable: No
# In-place: Yes
# Adaptive: No
# Used in: Selection sort is used in the selection sort algorithm.