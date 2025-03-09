# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.


def combinationSum(candidates, target):
    if not candidates:
        return []
    res=[]
    def backtrack(index, sum, arr):
        if (index>=len(candidates) or sum>target):
            return
        if(sum==target):
            res.append(arr)
            return
        
        arr.append(candidates[index])
        backtrack(index,sum+candidates[index],arr[:])

        arr.pop()
        backtrack(index+1,sum,arr[:])

    backtrack(0,0,[])
    return res

array = [2,3,6,7]
target = 7
print(combinationSum(array,target)) #[[2, 2, 3], [7]]

#Time complexity is O(2^n) as we are making 2 decisions at each step.
#Space complexity is O(n) as we are storing the path in the recursion stack.