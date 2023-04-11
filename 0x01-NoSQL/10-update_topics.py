#!/usr/bin/env python3
"""Change school topics"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """this function changes all topics of school document base on name"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
