#!/usr/bin/env python
'''A Bioinformatics Algorithms script containing scoring matrices.'''


class BLOSUM62(object):
    """The BLOSUM62 scoring matrix class."""

    def __init__(self):
        """Initialize the scoring matrix."""
        import os

        with open('BLOSUM62.txt', 'r') as input_data:
            items = [line.strip().split() for line in input_data.readlines()]
            self.scoring_matrix = {(item[0], item[1]):int(item[2]) for item in items}

    def __getitem__(self, pair):
        """Returns the score of the given pair of protein."""
        return self.scoring_matrix[pair[0], pair[1]]