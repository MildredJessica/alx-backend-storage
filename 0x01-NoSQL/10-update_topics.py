#!/usr/bin/env python3
""" Change school topics"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name"""
    condition = {"name": name}
    data = {"$set": {"topics": topics}}
    return mongo_collection.update_many(condition, data)
