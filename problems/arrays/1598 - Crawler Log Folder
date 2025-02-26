
#Summary: Given a list of logs, we need to find the minimum number of operations required to navigate to the folder
# represented by the logs. We can navigate to a folder by using "../" to move to the parent folder and "./" to stay in the current folder

from typing import List

def minOperations(logs: List[str]) -> int:
    stack = []
    for log in logs:
        if log == "../":
            if stack:
                stack.pop()
        elif log=="./":
            continue
        else:
            stack.append(log)
    return len(stack)
    

strings = ["d1/","d2/","../","d21/","./"]
print(minOperations(strings)) 


# Time complexity: O(n) because we are iterating through the logs where n is the number of logs
# Space complexity: O(n) because we are storing the logs in a stack where n is the number of logs

# Can we optimize by not using a stack?
# Yes, we can use a counter to keep track of the number of folders we are in. If we encounter "../" we decrement the counter

def optimized_minOperations(logs: List[str]) -> int:
    count = 0
    for log in logs:
        if log == "../":
            if count:
                count -= 1
        elif log=="./":
            continue
        else:
            count += 1
    return count