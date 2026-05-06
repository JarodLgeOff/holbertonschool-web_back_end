#!/usr/bin/env python3
"""Simple pagination"""

import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset
        (i.e. the correct list of rows)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dict with pagination metadata:
            page_size (int): Dataset page length.
            page (int): Current page number.
            data (list): The dataset page content.
            next_page (int|None): Next page number or None.
            prev_page (int|None): Previous page number or None.
            total_pages (int): Total number of pages.
        """
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + (len(self.dataset())
                                                          % page_size > 0)
        hypermedia = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return hypermedia
