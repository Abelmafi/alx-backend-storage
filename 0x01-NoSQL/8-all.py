#!/usr/bin/env python3
"""..."""
from pymongo import MongoClient


def list_all(mongo_collection):
    cursor = mongo_collection.find({})
    doc_list = []
    for item in cursor:
        doc_list.append(item)
    return doc_list
