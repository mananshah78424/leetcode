#Summary: You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

# t is a subsequence of the string s.
# The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
# Return the length of the longest ideal string.


def longestIdealString(s,k):
    dp = {}
    for ch in s:
        newval = 0
        for prev in dp:
            if abs(ord(ch)-ord(prev)) <= k:
                newval = max(newval,dp[prev])
        dp[ch] = newval+1
    return max(dp.values())


s="acfgbd"
k=2
print(longestIdealString(s,k)) #4

#Logic to solve it - Mark longest length ending at each character.