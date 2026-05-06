#!/usr/bin/env python3
"""Liist all documents in the collection"""


def list_all(mongo_collection):
    """List all documents in a collection
    Args:
        mongo_collection: pymongo collection object
    Returns:
        list of documents in collection
    """
    return mongo_collection.find()
