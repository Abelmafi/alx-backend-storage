#!/usr/bin/env python3
"""Top students"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """returns all students soarted by average score"""
    result = mongo_collection.find.sort({"averageScore", pymongo.ASCENDING})
    return result
