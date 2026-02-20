#!/usr/bin/python3
"""0-basic_cache.py"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching class"""

    def put(self, key, item):
        """
        Put an item to the cache, nothing if is empty
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache,
        If key is empty or not exist return none
        """
        if key is None:
            return None
        return self.cache_data.get(key)
