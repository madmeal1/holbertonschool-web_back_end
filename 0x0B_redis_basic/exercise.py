#!/usr/bin/env python3
"""
This module defines a Cache class for storing basic data in Redis.
"""

from typing import Callable, Optional, Union
import uuid
import redis


class Cache:
    """
    Cache provides basic methods for storing data in a Redis database.
    """

    def __init__(self) -> None:
        """
        Initialize the Redis client and clear the current database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random UUID key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, int, bytes]]] = None
    ) -> Union[str, int, bytes, None]:
        """
        Retrieve data from Redis and optionally convert it with a function.
        """
        data = self._redis.get(key)

        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis and decode it as a UTF-8 string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis and convert it to an integer.
        """
        return self.get(key, int)
