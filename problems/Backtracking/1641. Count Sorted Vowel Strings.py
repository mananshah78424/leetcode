


def countVowelStrings(n):
    str = 'aeiou'
    res=0
    def backtrack(idx, st):
        nonlocal res
       
        if len(st) == n:
            print("ST is: ", st)
            return 1
        if idx >= len(str):
            return 0
        res=0
        for i in range(idx, len(str)):
            st+=str[i]
            print(st)
            res+=backtrack(i, st)
            st=st[:-1]
        print(res)
        return res
    
    backtrack(0, "")
    return res


n=2
print(countVowelStrings(n)) #35