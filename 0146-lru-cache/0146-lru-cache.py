class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lruCache = defaultdict(int)
        self.LRUKeys = deque([])
        self.actionId = 0
        self.recentActionId = defaultdict(int)

    def get(self, key: int) -> int:
        if key not in self.lruCache:
            return -1

        self.recentActionId[key] = self.actionId
        self.LRUKeys.append((key, self.actionId))
        self.actionId += 1

        return self.lruCache[key]
        
            
    def put(self, key: int, value: int) -> None:
        #full capacity reached  
        if key not in self.lruCache and len(self.lruCache) == self.capacity:
            LRUKey = -1
            while self.LRUKeys:
                lruKey, actionId = self.LRUKeys.popleft()
                if self.recentActionId[lruKey] == actionId:
                    LRUKey = lruKey
                    break

            if LRUKey in self.lruCache:
                del self.lruCache[LRUKey]
                del self.recentActionId[LRUKey]

        self.recentActionId[key] = self.actionId
        self.lruCache[key] = value
        self.LRUKeys.append((key, self.actionId))
        self.actionId += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)