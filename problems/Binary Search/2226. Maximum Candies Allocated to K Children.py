def maximumCandies(candies, k):
    def isPossible(mid):
        y=0
        for x in candies:
            y+=(x/mid)
        return True if y>=k else False
    if(sum(candies))<k:
        return 0
    res=0
    low=1
    high=sum(candies)
    while low<=high:
        mid=(low+high)//2
        if(isPossible(mid)):
            res=max(res,mid)
            low=mid+1
        else:
            high=mid-1
    return res
        
candies = [5,8,6]
k = 3
print(maximumCandies(candies, k))