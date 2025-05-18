

def searchRange(nums, target):
        def lowest(nums,target,l,h):
            res=h

            while(l<=h):
                mid = (l+h)//2
                if(nums[mid]==target):
                    res=mid
                    h=mid-1
                elif(nums[mid]>target):
                    h=mid-1
                else:
                    l=mid+1

            return res


        def highest(nums,target,l,h):         
            res=l
            while(l<=h):
                mid = (l+h)//2
                if(nums[mid]==target):
                    res=mid
                    l=mid+1
                elif(nums[mid]>target):
                    h=mid-1
                else:
                    l=mid+1
            return res


        
        low,high=0,len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]==target):
                l=lowest(nums,target,low,mid)
                h=highest(nums,target,mid,high)
                return [l,h]
            elif(nums[mid]>target):
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]
        

nums = [5,7,7,8,8,10]
target = 8

print(searchRange(nums,target))
    