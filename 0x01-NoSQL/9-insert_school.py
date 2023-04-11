#!/usr/bin/env python3
"""Insert docment in oython"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """python function that inserts a  new document in collection based on kwargs"""
    document = {}
    for key, value in kwargs.items():
        document[key] = value
    result = mongo_collection.insert_one(document)
    return result.inserted_id
