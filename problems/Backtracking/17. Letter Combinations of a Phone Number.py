

def letterCombination(digits):
    res=[]
    hmap = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    def backtrack(index,path):
        if len(path)==len(digits):
            res.append("".join(path))
            return 
        for i in range(len(hmap[digits[index]])):
            path.append(hmap[digits[index]][i])
            backtrack(index+1,path[:])
            path.pop()

    backtrack(0,[])
    return res

digits = "23"
print(letterCombination(digits)) #["ad","ae","af","bd","be","bf","cd","ce","cf"]