
import heapq
def halveArray(nums):
    q = []
    total = sum(nums)
    orig = total
    orig=total
    for i in nums:
        q.append(-i)
    heapq.heapify(q)
    res = 0
    while total > orig/2.0:
        largest = -heapq.heappop(q)
        heapq.heappush(q, -largest / 2.0)
        total -= largest / 2.0
        res += 1
    return res

    

nums = [32,98,23,14,67,40,26,9,96,96,91,76,4,40,42,2,31,13,16,37,62,2,27,25,100,94,14,3,48,56,64,59,33,10,74,47,73,72,89,69,15,79,22,18,53,62,20,9,76,64]


print(halveArray(nums)) # 36