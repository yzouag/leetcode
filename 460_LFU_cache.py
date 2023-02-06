class LFUCache:

    def __init__(self, capacity: int):
        self.cnt = {}
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cnt[key] += 1
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cnt[key] += 1
            self.cache.pop(key)
            self.cache[key] = value
            return
        
        if len(self.cache) < self.capacity:
            self.cnt[key] = 1
            self.cache[key] = value
        else:
            least_recent_key = list(self.cache.keys())[0]
            minimum_cnt = self.cnt[least_recent_key]
            for k in self.cnt:
                if self.cnt[k] < minimum_cnt:
                    minimum_cnt = self.cnt[k]
                    least_recent_key = k
            
        

# cnt(x) = the use counter for key x
# cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
lfu = LFUCache(2)
lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1)      # return 1
                # cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3)   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                # cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2)      # return -1 (not found)
lfu.get(3)      # return 3
                # cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4)   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                # cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1)      # return -1 (not found)
lfu.get(3)      # return 3
                # cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4)      # return 4
                # cache=[4,3], cnt(4)=2, cnt(3)=3
