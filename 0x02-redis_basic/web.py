#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()

def url_tracker(method: Callable) -> Callable:
    '''Tracks how many times a URL was accessed.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''The wrapper function for tracking the URL.
        '''
        redis_store.incr(f'count:{url}')
        return method(url)
    return invoker


def data_cacher(expires=10):
    '''Caches the output of fetched data with expiration time.
    '''
    def cache_decorator(method):
        @wraps(method)
        def invoker(url) -> str:
            '''The wrapper function for caching the output.
            '''
            result = redis_store.get(f'result:{url}')
            if result:
                return result.decode('utf-8')
            result = method(url)
            redis_store.setex(f'result:{url}', expires, result)
            return result
        return invoker
    return cache_decorator


@url_tracker
@data_cacher(expires=10)
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(url).text
