# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers s to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


def combinationSum2(candidates, target):
    if not candidates:
        return []
    res = set()
    def backtrack(index, s, arr):
        if s==target:
            res.add(tuple(sorted(arr)))     
            return
        if s>target or index>=len(candidates):
            return
        
        arr.append(candidates[index])
        s+=candidates[index]
        backtrack(index+1,s,arr[:])
        arr.pop()
        s-=candidates[index]
        backtrack(index+1,s,arr[:])

    backtrack(0,0,[])
    return list(res)


array = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(array,target)) #[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

#Time complexity is O(2^n) + O(nlogn) as we are making 2 decisions at each step and sorting the array.
#Space complexity is k * x where k is the number of unique combinations and x is the average length of each combination.


#Above solution is correct but it is not optimal. 


def optimizedSolution (candidates, target):
    if not candidates:
        return []
    res = []
    candidates.sort()
    def backtrack(index,target, arr):
        if(target==0):
            res.append(arr)
            return
        for i in range(index,len(candidates)):
            if(i>index and candidates[i]==candidates[i-1]):
                continue
            if(candidates[i]>target):
                break
            arr.append(candidates[i])
            print(i+1, target-candidates[i],arr, i, index)
            backtrack(i+1,target-candidates[i],arr[:])
            arr.pop()
            print("Backtrack",arr, i, index)
    backtrack(0,target,[])

    return res

array = [1,1,1,2,2]
target = 4
print(optimizedSolution(array,target)) #[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
            