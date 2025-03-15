class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        d1, d2 = defaultdict(list), defaultdict(list)

        for i, conv in enumerate(pairs1):
            d1[conv[0]].append((conv[1], rates1[i]))
            d1[conv[1]].append((conv[0], 1/rates1[i]))

        for i, conv in enumerate(pairs2):
            d2[conv[0]].append((conv[1], rates2[i]))
            d2[conv[1]].append((conv[0], 1/rates2[i]))

        # print(d1)
        # print(d2)

        d1_convertion = defaultdict(int)
        d2_convertion = defaultdict(int)

        def dfs(node, vis, graph, curr_prod, conver_table):
            if node is vis: return 

            vis.add(node)

            for ch, wgt in graph[node]:
                if ch in vis: continue
                conver_table[ch] = curr_prod*wgt
                dfs(ch, vis, graph, conver_table[ch], conver_table)
            
            vis.discard(node)

        vis = set()
        dfs(initialCurrency, vis, d1, 1, d1_convertion)
        dfs(initialCurrency, vis, d2, 1, d2_convertion)

        # print(d1_convertion)
        # print(d2_convertion)

        all_curr = set(d1_convertion.keys()).intersection(set(d2_convertion.keys()))

        max_conv = 1
        for cur in all_curr:
            max_conv = max(max_conv, d1_convertion[cur]*(1/d2_convertion[cur]))

        return max_conv





        

        