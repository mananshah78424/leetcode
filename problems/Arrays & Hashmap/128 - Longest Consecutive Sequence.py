#Summary: We have an array of integers. We need to find the length of the longest consecutive elements sequence.

#Status - Had to see solution. 

def longestConsecutive(nums):
    num_set, res = set(nums), 0
    for num in num_set:
        if num -1 in num_set:
            continue
        count = 1
        while num+count in num_set:
            count += 1
        res = max(res, count)
    return res


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums)) # 4

#Brute force solution: Sort the array and then iterate through the array. If the current element is equal to the previous element + 1, increment the count. If not, update the result with the maximum of the current result and the count. Return the result.
#Time complexity: O(nlogn) because we are sorting the array.



