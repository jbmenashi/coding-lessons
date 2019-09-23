class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        for char in s:
            if char in hash:
                hash[char] = hash[char] + 1
            else:
                hash[char] = 1
        for char in s:
            if hash[char] == 1:
                return s.index(char)
        return -1
