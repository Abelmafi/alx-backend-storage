#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import functools
import redis
import requests


redis_client = redis.Redis()


def cache(expiration_time=10):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Generate a Redis key based on the function name and its arguments
            key = f"{func.__name__}:{args}:{kwargs}"
            # Check if the result is already cached
            cached_result = redis_client.get(key)
            if cached_result is not None:
                return cached_result.decode('utf-8')
            # Call the function and cache its result
            result = func(*args, **kwargs)
            redis_client.setex(key, expiration_time, result)
            return result
        return wrapper
    return decorator


@cache()
def get_page(url: str) -> str:
    # Check if the URL is already cached
    cached_html = redis_client.get(url)
    if cached_html is not None:
        # Increment the access count for this URL
        redis_client.incr(f"count:{url}")
        return cached_html.decode('utf-8')

    # Make a GET request to obtain the HTML content
    response = requests.get(url)

    # Cache the HTML content with an expiration time of 10 seconds
    redis_client.setex(url, 10, response.content)

    # Set the access count for this URL to 1
    redis_client.set(f"count:{url}", 1)

    return response.content.decode('utf-8')

