def countPalindromes(s):
    res = 0
    
    # Odd-length palindromes (single character center)
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
    
    # Even-length palindromes (two-character center)
    for i in range(len(s) - 1):
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

    return res

s = "abaab"
print(countPalindromes(s))  # Output: 8
