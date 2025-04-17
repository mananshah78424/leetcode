
import heapq
def minStoneSum(piles, k):
    q = []
    for pile in piles:
        heapq.heappush(q, -pile)
    while k > 0:
        largest = -heapq.heappop(q)
        heapq.heappush(q, (-largest + largest // 2))
        k -=1
    return -1 *sum(q)
    
piles = [4,3,6,7]
k=3
print(minStoneSum(piles,k)) # 12