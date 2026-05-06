#!/usr/bin/env python3

"""Update a document in a collection"""


def update_topics(mongo_collection, name, topics):
    """Update a document in a collection
    Args:
        mongo_collection: pymongo collection object
        name: name of the school to update
        topics: list of topics about the school
    Returns:
        The new _id of the inserted document
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
