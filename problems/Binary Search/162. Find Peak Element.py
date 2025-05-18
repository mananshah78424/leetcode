def findPeakElement(self, nums):
    if len(nums)==1:
        return 0
    if nums[0]>nums[1]:
        return 0
    if nums[-1]>nums[-2]:
        return len(nums)-1
    
    low=1
    high=len(nums)-2
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
            return mid
        elif(nums[mid]>nums[mid-1]):
            low=mid+1
        else:
            high=mid-1
    return -1

nums = [1,2,3,1]
print(findPeakElement(nums))