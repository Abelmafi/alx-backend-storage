#!/usr/bin/env python3
"""Where can I learn Python?"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic:"""
    result_list = []
    result = mongo_collection.find({"topics": topic})
    return result
