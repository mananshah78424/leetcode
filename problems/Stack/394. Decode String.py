


def decodeString(s):
    res=""
    stack = []
    for i in range(len(s)):
        if(s[i] == ']'):
            temp=[]
            while(stack[-1]!='['):
                x= stack.pop()
                temp.append(x)
            stack.pop()
            temp = temp[::-1]
            tempstr = ''.join(temp)
            num = ""
            while stack and stack[-1].isnumeric():
                num = stack.pop() + num
            
            tempstr = int(num)*tempstr
                
            stack.append(tempstr)
        else:
            stack.append(s[i])
    
    for i in stack:
        res+=i
    
    return res

s = "100[leetcode]"

print(decodeString(s)) #accaccacc