#!/usr/bin/env python3
"""redis basics"""
import redis
import uuid
from typing import Union


class Cache:
    """uses the Redis client from the redis package,
    generates a random key using the uuid module,
    and stores the data in Redis using the set method."""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """The return type of the store method is a string,
        which is the key used to store the data in Redis."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
