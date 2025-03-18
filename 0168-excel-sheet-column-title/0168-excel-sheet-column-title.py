class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return chr(columnNumber + 64)
        
        if columnNumber % 26 == 0:
            columnNumber -= 26
            return self.convertToTitle(columnNumber//26) + 'Z'

        return self.convertToTitle(columnNumber//26) + chr(columnNumber%26 + 64)