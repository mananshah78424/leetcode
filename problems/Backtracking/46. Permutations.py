def permute(nums):
    res=[]
    def backtrack(index, arr):
        if(len(arr)==len(nums)):
            res.append(arr)
            return 
        for i in range(index,len(nums)):
            nums[index],nums[i]=nums[i],nums[index]
            backtrack(index+1,arr+[nums[index]])
            nums[index],nums[i]=nums[i],nums[index]
    
    backtrack(0,[])
    return res



nums = [1,2,3]
print(permute(nums)) #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]