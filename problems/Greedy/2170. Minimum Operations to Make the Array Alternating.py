import heapq
def minimumOperations(self, nums):
    if(len(nums)==1):
        return 0
    if(len(nums)==2):
        return 1 if nums[0]==nums[1] else 0
    
    oddMap = {}
    evenMap = {}
    for i in range(len(nums)):
        if i % 2 == 0:
            evenMap[nums[i]] = 1 + evenMap.get(nums[i], 0)
        else:
            oddMap[nums[i]] = 1 + oddMap.get(nums[i], 0)
    
    evenQueue = [(-v, k) for k, v in evenMap.items()]
    oddQueue = [(-v, k) for k, v in oddMap.items()]
    heapq.heapify(evenQueue)
    heapq.heapify(oddQueue)

    even1 = heapq.heappop(evenQueue)
    odd1 = heapq.heappop(oddQueue)

    # Now check for conflict
    if even1[1] != odd1[1]:
        return len(nums) + even1[0] + odd1[0]  # Values are negative

    # If keys match, we need to try combinations:
    even2 = heapq.heappop(evenQueue) if evenQueue else (0, 0)
    odd2 = heapq.heappop(oddQueue) if oddQueue else (0, 0)

    # Try using even1 + odd2
    option1 = len(nums) + even1[0] + odd2[0]
    # Try using even2 + odd1
    option2 = len(nums) + even2[0] + odd1[0]

    return min(option1, option2)

nums = [3,1,3,2,4,3]
print(minimumOperations(nums)) #3