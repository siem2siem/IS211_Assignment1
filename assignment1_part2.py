#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment1-Part 2"""

class Book(object):
    """A class named Book with two attributes.
    	Args:
        author (str): String for Book Author default blank.
        title (str): String for Book Title default blank.
    """
    author = ""
    title = ""

    def __init__(self, author, title):
        """A function that takes in an author and a title, 
		    and sets them to the object variables.
	     """

        self.author = author
        self.title = title

    def display(self):
        """A function which when called, simply prints out a 
		    string representing the book.
        Args: n/a
		  Returns:
            'title' written by author
        Examples:
		      'Of Mice and Men', written by John Steinbeck
            'To Kill a Mockingbird' written by Harper Lee
		  """

        print "{}, written by {}".format(self.title, self.author)

OBJECT1 = Book("John Steinbeck", "'Of Mice and Men'")
OBJECT2 = Book("Harper Lee", "'To Kill a Mockingbird'")

OBJECT1.display()
OBJECT2.display()
