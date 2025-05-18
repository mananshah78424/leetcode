def singleNonDuplicate(self, nums):
    low,high=0,len(nums)-1
    if(len(nums)==1):
        return nums[0]
    while low<=high:
        mid = (low+high)//2
        if(mid==0 or mid==len(nums)-1):
            if(mid==0 and nums[mid]!=nums[mid+1]):
                return nums[mid]
            if(mid==len(nums)-1 and nums[mid]!=nums[mid-1]):
                return nums[mid]
        if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
            return nums[mid]
        if(nums[mid]==nums[mid-1]):
            if((mid+1-low)%2==0):
                low=mid+1
            else:
                high=mid
        else:
            if((len(nums)-mid)%2==0):
                high=mid-1
            else:
                low=mid
    return -1

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))
        