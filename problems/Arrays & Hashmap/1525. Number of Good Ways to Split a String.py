

def numSplits(s):
    res=0
    hmap={}
    hmap2={}
    for i in range(len(s)):
        hmap[s[i]]=1+hmap.get(s[i],0)

    for i in range(len(s)):
        hmap2[s[i]]=1+hmap2.get(s[i],0)
        hmap[s[i]]-=1
        if hmap[s[i]]==0:
            del hmap[s[i]]
        if len(hmap)==len(hmap2):
            res+=1
    return res

s="aacaba"
print(numSplits(s)) #2

#Time complexity is O(n) where n is the length of the string.
#Space complextiy is O(n) + O(n) = O(n) where n is the length of the string.

