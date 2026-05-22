#!/usr/bin/env python3
"""
This module defines a Cache class for storing basic data in Redis.
"""

from typing import Union
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
