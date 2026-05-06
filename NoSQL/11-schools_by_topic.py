#!/usr/bin/env python3
"""List of schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic

    Args:
        mongo_collection: The pymongo collection object
        topic: The topic searched for

    Returns:
        The list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
