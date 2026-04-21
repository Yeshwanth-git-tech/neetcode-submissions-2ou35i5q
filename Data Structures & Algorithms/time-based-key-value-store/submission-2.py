class TimeMap:

    def __init__(self):
        #we are setting a key and value with a list whihc include timestamp with it 
        #timestamp is always in increasing order

        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #here we just add to the store 
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value , timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key , [])
    

        print(values)
        print(len(values))

        l = 0 
        r = len(values)-1

        while l<=r:
            mid = (l+r)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid+1
            else:
                r = mid-1
        return res



        
