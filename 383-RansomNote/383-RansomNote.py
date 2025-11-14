# Last updated: 11/14/2025, 8:47:57 AM
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for ch, freq in ransom_count.items():
            if magazine_count[ch] < freq:
                return False
        return True
