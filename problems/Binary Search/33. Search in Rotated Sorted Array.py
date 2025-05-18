


def search(self, nums, target):
    low,high = 0,len(nums)-1
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]==target):
            return mid
        elif(nums[mid]>=nums[low]):
            if(nums[low]<=target and target<=nums[mid]):
                high=mid-1
            else:
                low=mid+1
        else:
            if(nums[mid]<=target and target<=nums[high]):
                low=mid+1
            else:
                high=mid-1
        

    return -1

        
nums = [4,5,6,7,0,1,2]
target = 0


print(search(nums,target))
    