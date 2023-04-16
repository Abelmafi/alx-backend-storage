#!/usr/bin/env python3
"""Cache module"""
import redis
import uuid
import functools
from typing import Callable


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @functools.lru_cache()
    def get(self, key: str, fn: Callable = None):
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str):
        return self.get(key, str)

    def get_int(self, key: str):
        return self.get(key, int)

    @functools.lru_cache()
    @count_calls
    def store(self, data) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapped(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapped
##!/usr/bin/env python3
#"""Cache module"""
#
#import redis
#import uuid
#from typing import Union, Callable, Optional
#import functools
#
#
#def count_calls(func):
#    @functools.wraps(func)
#    def wrapper(self, *args, **kwargs):
#        key = func.__qualname__
#        self._redis.incr(key)
#        return func(self, *args, **kwargs)
#    return wrapper
#
#
#class Cache:
#    """Cache class"""
#
#    def __init__(self):
#        """Constructor method"""
#        self._redis = redis.Redis()
#        self._redis.flushdb()
#
#    def store(self, data: Union[str, bytes, int, float]) -> str:
#        """Store a data string in Redis"""
#        key = str(uuid.uuid4())
#        self._redis.set(key, data)
#        return key
#
#    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
#        """Get data from Redis by key"""
#        data = self._redis.get(key)
#        if data is None:
#            return data
#        if fn is not None:
#            data = fn(data)
#        return data
#
#    def get_str(self, key: str) -> Union[str, None]:
#        """Get string data from Redis by key"""
#        return self.get(key, fn=lambda x: x.decode())
#
#    def get_int(self, key: str) -> Union[int, None]:
#        """Get integer data from Redis by key"""
#        return self.get(key, fn=lambda x: int(x.decode()))
#
#    @count_calls
#    def store(self, data: Union[str, bytes, int, float]) -> str:
#        key = uuid.uuid4().hex
#        self._redis.set(key, data)
#        return key
