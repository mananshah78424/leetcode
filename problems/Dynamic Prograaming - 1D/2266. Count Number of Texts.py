#Summary: Given a string and a list of words, find the number of ways to form the string using the words in the list. 

def countTexts(pressedKey):
    dp = [1] + [0]*len(pressedKey)
    print(dp)
    for i,n in enumerate(pressedKey):
        dp[i+1]=dp[i]
        #Check if it is continous
        if i>=1 and pressedKey[i-1] == n:
            dp[i+1]+=dp[i-1]
            
            # why is the above step done - because if the previous number is the same as the current number, then we can combine the two numbers to form a new number.
            if i>=2 and pressedKey[i-2] == n:
                dp[i+1]+=dp[i-2]
                # why is the above step done - because if the previous number is the same as the current number, then we can combine the two numbers to form a new number.
                if i>=3 and pressedKey[i-3] == n and (n in '79'):
                    dp[i+1]+=dp[i-3]
        print("Step at" , i , dp)
                    # why is the above step done - because if the previous number is the same as the current number, then we can combine the two numbers to form a new number.
    

pressedKey = "22233"
MOD = 10**9+7
print(countTexts(pressedKey)) #8