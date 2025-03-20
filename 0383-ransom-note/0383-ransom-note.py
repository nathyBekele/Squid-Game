class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        """
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for key, count in r_count.items():
            if m_count[key] < count:
                return False 
                

        return True
        