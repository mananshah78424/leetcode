# Assign more cookies hence greedy

def findContentChildren(g,s):
    g.sort()
    s.sort()
    l,r=0,0
    res=0
    while l<len(s) and r<len(g):
        if(s[l]>=g[r]):
            res+=1
            l+=1
            r+=1
        l+=1
    return res



g = [1,2,3]
s = [1,1]
print(findContentChildren(g,s))