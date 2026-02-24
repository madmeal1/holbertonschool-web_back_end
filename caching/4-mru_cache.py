#!/usr/bin/python3
"""4-mru_cache.py"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """Add an item in the cache using MRU eviction policy."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            if key in self.usage:
                self.usage.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage.pop(-1)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.usage.append(key)

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None

        self.usage.remove(key)
        self.usage.append(key)

        return self.cache_data.get(key)
