#Summary: Given a string S, which represents a phone number, email address, or any other string, mask the string with the following rules:


def main(str):
    if '@' in str:
        return mask_email(str)
    else:
        return mask_phone(str)
    
def mask_email(str):
    str=str.lower()
    split = str.split('@')
    name, domain = split[0], split[1]
    return name[0] + '*****' + name[-1] + '@' + domain

def mask_phone(str):
    digits = [c for c in str if c.isdigit()]
    local = '***-***-' + ''.join(digits[-4:])
    if len(digits) == 10:
        return local
    return '+' + '*' * (len(digits) - 10) + '-' + local

email = "LeetCode@LeetCode.com"
#Output: "l*****e@leetcode.com

phone = "1(234)567-890"
#Output: "***-***-7890"

print(main(email))
print(main(phone))


# Time complexity: O(N) because we are iterating through the string to find the digits where N is the length of the string
# Space complexity: O(N) because we are storing the digits in a list where N is the length of the string

# Can we do better? Yes, we can use regex to find the digits and the '@' symbol in the string. This will reduce the time complexity to O(1) and space complexity to O(1) as well.

