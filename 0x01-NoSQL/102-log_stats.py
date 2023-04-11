#!/usr/bin/env python3
"""Log stats """
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    ngnix_collection = client.logs.nginx
    
    total_logs = ngnix_collection.count_documents({})
    print("{} logs".format(total_logs))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = ngnix_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    count = ngnix_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{count} status check")
    print("IPs:")

    top_ips = ngnix_collection.aggregate([
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
        ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")    
