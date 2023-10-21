#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """ Python function that lists all documents in a collection"""
    doc = list(mongo_collection.find({}))
    return doc
