#!/usr/bin/env python3
"""..."""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''The module-level Redis instance.
'''


def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    count_key = f'count:{url}'
    result_key = f'result:{url}'

    redis_store.incr(count_key)
    result = redis_store.get(result_key)

    if result:
        return result.decode('utf-8')
    else:
        response = requests.get(url)
        redis_store.setex(result_key, 10, response.text)

        return response.text


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''The wrapper function for caching the output.
        '''
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


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


@url_tracker
@data_cacher
def get_page_decorated(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(url).text
