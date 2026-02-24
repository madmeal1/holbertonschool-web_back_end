#!/usr/bin/python3
"""100-lfu_cache.py"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system with LRU tiebreaker"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage = []
        self.freq = {}

    def put(self, key, item):
        """Add an item using LFU eviction policy (LRU as tiebreaker)."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage.remove(key)
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq[k] for k in self.usage)
                for k in self.usage:
                    if self.freq[k] == min_freq:
                        lfu_key = k
                        break
                self.usage.remove(lfu_key)
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                print(f"DISCARD: {lfu_key}")

            self.freq[key] = 1

        self.cache_data[key] = item
        self.usage.append(key)

    def get(self, key):
        """Get an item by key and update its frequency."""
        if key is None or key not in self.cache_data:
            return None

        self.usage.remove(key)
        self.usage.append(key)
        self.freq[key] += 1

        return self.cache_data.get(key)
