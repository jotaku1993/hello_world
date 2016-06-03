import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        #Use Ordered Dict
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        

    def get(self, key):
        """
        :rtype: int
        """
        #if not in cache, return -1
        if key not in self.cache:
            return -1
        #otherwise, change the key to the end
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
        
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.cache.pop(key)
        elif self.capacity <= len(self.cache):
            self.cache.popitem(last=False)
        self.cache[key] = value
