class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if int(num) == 0 and len(num) > 2:
            return True

        starting_pairs, N = [], len(num)

        for l in range(N - 2):
            n1 = num[:l+1]

            if len(n1) > 1 and n1[0] == '0':
                break

            for r in range(l + 1, N - 1):
                if num[r + 1] == '0': 
                    continue
                
                n2 = num[l+1:r+1]
                
                if len(n2) > 1 and n2[0] == '0':
                    break

                n3 = str(int(n1) + int(n2))

                if n3 == num[r+1:r+1+len(n3)]: 
                    starting_pairs.append((l, r))
        
        def is_additive(n1, n2, idx):
            if idx >= N: 
                return True

            n3 = str(n1 + n2)
            # print(n1, n2, n3, idx, num[idx: idx + len(n3)] == n3)

            return False if num[idx: idx + len(n3)] != n3 else is_additive(n2, int(n3), idx + len(n3))

        for l, r in starting_pairs:
            n1 = int(num[:l+1])
            n2 = int(num[l+1:r+1])

            if is_additive(n1, n2, r + 1): 
                return True

        return False