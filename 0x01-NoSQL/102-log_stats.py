#!/usr/bin/env python3
"""Nginx logs stored in MongoDB"""


from pymongo import MongoClient


if __name__ == "__main__":
    """ Python script that provides some stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.log.nginx
    nginx_logs = nginx_collection.count_documents()
    print("{} logs".format(nginx_logs))
    print("Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for met in method:
        count = nginx_collection.count_documents({"methods": met})
        print("\tmethod {}: {}".format(met, count))
    status_check = nginx_collection.count_documents(
            {"methods": "GET", "path": "/status"})
    print("{} status check".format(status_check))
    print("IPs:")
    top_ips = nginx_collection.aggregate(
            [{
                "$group": {
                    "_id": "$ip",
                    "count": {"$sum": 1}
                }
            }, {"$sort": {"count": -1}},
            {"$limit": 10},
            {
                "$project": {
                    "_id": 0, "ip": "$_id", "count": 1
                }
            }
            ])
    for ips in top_ips:
        ip = ips.get("ip")
        count = ips.get("count")
        print("{} {}".format(ip, count))
