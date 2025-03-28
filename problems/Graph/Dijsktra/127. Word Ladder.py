
from collections import Counter
import heapq
def char_difference(word1,word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count


def ladderLengthBruteForce(begin, end, wordList):
    wordList = set(wordList)
    if end not in wordList:
        return 0

    
    # Create the adjacency list
    adj = {}

    # First do for the begin word
    for word in wordList:
        if char_difference(begin, word) == 1:
            if begin in adj:
                adj[begin].append(word)
            else:
                adj[begin] = [word]
    
    # Now do for the rest of the words
    wordList.add(begin)
    for word in wordList:
        adj[word] = []
        for word2 in wordList:
            if char_difference(word, word2) == 1:
                adj[word].append(word2)
    wordList.remove(begin)

    # Now do the BFS
    pq = []
    heapq.heappush(pq, (1, begin))
    visited = set()
    visited.add(begin)
    while pq:
        d, node = heapq.heappop(pq)
        if node == end:
            return d
        for i in adj[node]:
            if i not in visited:
                visited.add(i)
                heapq.heappush(pq, (d+1, i))
    
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLengthBruteForce(beginWord, endWord, wordList)) # 5




# Optimized version
def ladderLengthOptimized(begin,end,wordList):
    wordList = set(wordList)
    if end not in wordList:
        return 0
    pq = []
    heapq.heappush(pq, (1, begin))
    visited = set()
    visited.add(begin)
    
    # Do for begin -> Replace each character from a-z and check if it is in wordList
    # If yes, then add to the queue

    while pq:
        d, node = heapq.heappop(pq)
        if node == end:
            return d
        for i in range(len(node)):
            for j in range(26):
                new_word = node[:i] + chr(ord('a')+ j) + node[i+1:]
                if new_word in wordList and new_word not in visited:
                    visited.add(new_word)
                    heapq.heappush(pq, (d+1, new_word))
        
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLengthOptimized(beginWord, endWord, wordList)) # 5