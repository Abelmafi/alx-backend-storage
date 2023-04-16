#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import requests
import redis
import time

redis_client = redis.Redis()

def get_page(url: str) -> str:
    """ Check if the URL is already cached """
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
