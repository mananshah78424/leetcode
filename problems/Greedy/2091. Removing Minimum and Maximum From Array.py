

def minimumDeletions(nums):
    res=0
    # Find index of minumum element 
    minI = nums.index(min(nums))
    # Find index of maximum element
    maxI = nums.index(max(nums))
    
    # Case 1: Remove all elements to the left of the minimum element
    leftSide = max(minI, maxI) + 1
    # Case 2: Remove all elements to the right of the maximum element
    rightSide = len(nums) - min(minI, maxI)

    # Case 3: Remove all elements between the minimum and maximum elements
    maxIndex = max(minI, maxI)
    minIndex = min(minI, maxI)
    middleSide = (len(nums)-maxIndex) + minIndex + 1

    # Return the minimum of the three cases
    return min(leftSide, rightSide, middleSide)

nums = [-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28]
print(minimumDeletions(nums)) #5