#!/usr/bin/python3
"""0-basic_cache.py"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Fifo cache class"""

    def __init__(self):
        """Overloader"""
        super().__init__()

    def put(self, key, item):
        """
        Put an item to the cache, nothing if is empty
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        Get an item from the cache,
        If key is empty or not exist return none
        """
        if key is None:
            return None
        return self.cache_data.get(key)
