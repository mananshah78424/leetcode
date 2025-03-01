#Summary: We have an array A of integers, and an array queries of queries. For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index]. Then we return the even array.


def sumEvenAfterQueries(arr, queries):
    res= []
    for value,index in queries:
        arr[index] += value
        evenSum = sum(x for x in arr if x % 2 == 0)
        res.append(evenSum)
    
    
    return res

arr = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
#Output: [8,6,2,4]

print(sumEvenAfterQueries(arr, queries)) # [8,6,2,4]

#Time complexity: O(n^2) because we are iterating through the array twice.
#Space complexity: O(n) because we are storing the sum of the even numbers in the array.

#Optimized solution: We can optimize this solution by checking if the number is even or odd. If the number is even, we can add it to the sum. If the number is odd, we can check if the new number is even. If it is, we can add it to the sum. If it is not, we can subtract the old number from the sum. This way, we only need to iterate through the array once.

def sumEvenAfterQueriesOptimized(arr, queries):
    res = []
    evenSum = sum(x for x in arr if x % 2 == 0)
    
    for value,index in queries:
        if arr[index] % 2 == 0:
            evenSum -= arr[index]
        arr[index] += value
        if arr[index] % 2 == 0:
            evenSum += arr[index]
        res.append(evenSum)
    
    return res

print(sumEvenAfterQueriesOptimized(arr, queries)) # [8,6,2,4]

#Time complexity: O(n) because we are iterating through the array once.
#Space complexity: O(1) because we are not storing the sum of the even numbers