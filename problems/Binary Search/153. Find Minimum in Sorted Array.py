
def findMin(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[high]:
            high = mid  # min must be in left half including mid
        else:
            low = mid + 1  # min must be in right half excluding mid
    return nums[low]

nums = [3,4,5,1,2]
print(findMin(nums))