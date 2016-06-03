Use orderedDict to solve the LRU cache.

OrderedDict: the pairs will be stored in the dict as the sequence you add.

Every time we get or set the key, pop it and add it to the end

Once the cache is full, delete the first element and set the new one

Actually you can use normal dict and linked list to do it.

Maybe try it after.
