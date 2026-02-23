#!/usr/bin/python3
"""2-lifo_cache.py"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self._order = []

    def put(self, key, item):
        """
        Add an item in the cache using LIFO eviction policy
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            if key in self._order:
                self._order.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = self._order.pop()
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

        self.cache_data[key] = item
        self._order.append(key)

    def get(self, key):
        """Get an item by key."""
        if key is None:
            return None
        return self.cache_data.get(key)
