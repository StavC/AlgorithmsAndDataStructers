class MyHashSet:

    def __init__(self):
        self.size = 10000  # the size of the hashtable
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):

        hashed = self.hash_func(key) #hashing the key
        bucket = self.buckets[hashed] #getting the bucket
        for i, k in enumerate(bucket): #checking if the key already exists
            if k == key:
                return
        bucket.append(key)
        '''
        bucket,index=self.search_func(key) #getting the bucket and if theres a bucket search if the key is already there
        if index>=0:
            return 
        bucket.append(key)
        '''

    def remove(self, key):

        hashed = self.hash_func(key)
        bucket = self.buckets[hashed]
        if bucket != None:
            if key in bucket:
                bucket.remove(key)

        '''
        bucket,index=self.search_func(key)
        if index<0:
            return
        bucket.remove(key)
        '''

    def contains(self, key):

        hashed = self.hash_func(key)
        bucket = self.buckets[hashed]
        if bucket != None:
            if key in bucket:
                return 1
        '''
        bucket,index=self.search_func(key)
        return index>=0
        '''

    def hash_func(self, key):
        return key % self.size  # hashing the key by mod the size of hashtable
