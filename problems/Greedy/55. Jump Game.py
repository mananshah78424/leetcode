

def canJump(nums):
    maxInterval = 0
    for i in range(len(nums)):
        if(i>maxInterval):
            return False
        maxInterval = max(maxInterval, nums[i]+i)
        print(maxInterval)
        if(maxInterval>=len(nums)):
            return True
    return True

    

nums = [2,3,1,1,4]
print(canJump(nums))