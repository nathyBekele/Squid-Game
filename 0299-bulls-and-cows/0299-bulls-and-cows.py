class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_set = Counter(secret)
        A, B = 0, 0

        for i, ch in enumerate(guess):
            if secret[i] == guess[i]: 
                A += 1
                secret_set[ch] -= 1

        for i, ch in enumerate(guess):
            if secret_set[ch] > 0 and secret[i] != guess[i]:
                # print(i, ch)  
                B += 1
                secret_set[ch] -= 1


        return f'{A}A{B}B'