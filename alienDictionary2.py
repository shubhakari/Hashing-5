from typing import List
from collections import deque

class Solution:
    # TC : O(n)
    # SC : O(1)
    def alienOrder(self, words: List[str]) -> str:
        
        graph = [[False] * 26 for _ in range(26)]
        seen = [False] * 26
        unique_char_count = 0
        words_count = len(words)
      
        # Process all the words for character presence and ordering
        for i in range(words_count - 1):
            for char in words[i]:
                if unique_char_count == 26:
                    break
                index = ord(char) - ord('a')
                if not seen[index]:
                    unique_char_count += 1
                    seen[index] = True
            word_length = len(words[i])
    
            for j in range(word_length):
                # If the next word is shorter than the current word, there is an issue with the order
                if j >= len(words[i + 1]):
                    return ''
              
                char1, char2 = words[i][j], words[i + 1][j]
                if char1 == char2:
                    continue
                index1, index2 = ord(char1) - ord('a'), ord(char2) - ord('a')
                if graph[index2][index1]:  # If there is a cycle, return empty string
                    return ''
                graph[index1][index2] = True
                break
      
        # Check the last word for new characters
        for char in words[words_count - 1]:
            if unique_char_count == 26:
                break
            index = ord(char) - ord('a')
            if not seen[index]:
                unique_char_count += 1
                seen[index] = True
      
        # Calculate in-degree for each character that is seen
        in_degree = [0] * 26
        for i in range(26):
            for j in range(26):
                if i != j and seen[i] and seen[j] and graph[i][j]:
                    in_degree[j] += 1
      
        
        queue = deque()
        ordered_chars = []
      
    
        for i in range(26):
            if seen[i] and in_degree[i] == 0:
                queue.append(i)
      
       
        while queue:
            current_char_index = queue.popleft()
            ordered_chars.append(chr(current_char_index + ord('a')))
          
            
            for i in range(26):
                if seen[i] and i != current_char_index and graph[current_char_index][i]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)
      
        
        return '' if len(ordered_chars) < unique_char_count else ''.join(ordered_chars)
