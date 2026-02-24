#!/usr/bin/python3
"""3-lru_cache.py"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """Add an item in the cache using LRU eviction policy."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            if key in self.usage:
                self.usage.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.usage.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.usage.append(key)

    def get(self, key):
        """Get an item by key and refresh its usage position."""
        if key is None or key not in self.cache_data:
            return None

        if key in self.usage:
            self.usage.remove(key)
        self.usage.append(key)

        return self.cache_data.get(key)
