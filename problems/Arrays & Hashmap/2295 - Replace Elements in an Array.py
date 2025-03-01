


def replaceElements(nums, operations):
    swaps = {}
    for s,e in reversed(operations):
        swaps[s] = swaps[e] if e in swaps else e
    print(swaps)
    for i, num in enumerate(nums):
        if num in swaps:
            nums[i] = swaps[num]
    return nums

nums = [1,2]
operations = [[1,3],[2,1],[3,2]]
print(replaceElements(nums, operations)) # [3,2,7,1]


# logic: Let say we have the following operations: a -> b, b -> c, c -> d, we know that in the end a will be transformed to d. So we want to build a hashmap that contains a -> d key-value pair