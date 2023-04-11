#!/usr/bin/env python3
"""Top students"""
import pymongo
from pymongo import MongoClient


def top_students(mongo_collection):
    """returns all students soarted by average score"""
    students = mongo_collection.find()
    for student in students:
        total_score = 0
        num_topics = len(student["topics"])
        for topic in student["topics"]:
            total_score += topic["score"]
        averageScore = total_score / num_topics
        mongo_collection.update_one({"_id": student["_id"]},
                                    {"$set": {"averageScore": averageScore}})

    result = mongo_collection.find().sort('averageScore', -1)
    return result
