class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1
        vowels = set(['a', 'e', 'i', 'o','u'])

        print(s)
        while l < r:
            while l < r and s[l].lower() not in vowels:
                l += 1

            while r > l and s[r].lower() not in vowels:
                r -= 1

            if s[l].lower() in vowels and s[r].lower() in vowels:
                s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1

        return ''.join(s)



                
            
