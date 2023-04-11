#!/usr/bin/env python3
"""a Python function that lists all documents in a collection:"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """a Python function that lists all documents in a collection:"""
    cursor = mongo_collection.find({})
    doc_list = []
    for item in cursor:
        doc_list.append(item)
    return doc_list
