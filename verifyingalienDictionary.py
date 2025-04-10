class Solution:
    # TC : O(n)
    # SC : O(1)
    def check(self, mp, word1, word2):
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            if mp[word1[i]] > mp[word2[j]]:
                return False
            elif mp[word1[i]] < mp[word2[j]]:
                return True
            i += 1
            j += 1
        return len(word1) <= len(word2)
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        for i, c in enumerate(order):
            mp[c] = i
        for i in range(len(words) - 1):
            if not self.check(mp, words[i], words[i + 1]):
                return False
        return True