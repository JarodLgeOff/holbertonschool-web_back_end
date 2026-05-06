#!/usr/bin/env python3

"""Insert a document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document in a collection
    Args:
        mongo_collection: pymongo collection object
        kwargs: key/value pairs to insert as a new document in the collection
    Returns:
        The new _id of the inserted document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
