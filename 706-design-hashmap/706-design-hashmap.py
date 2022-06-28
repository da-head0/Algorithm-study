class MyHashMap:

    def __init__(self):
        self.MyHashMap = {}
        

    def put(self, key: int, value: int) -> None:
        self.MyHashMap[key] = value
        

    def get(self, key: int) -> int:
        try:
            return self.MyHashMap[key]
        except KeyError:
            return -1        

    def remove(self, key: int) -> None:
        try:
            del self.MyHashMap[key]    
        except KeyError:
            return -1 

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)