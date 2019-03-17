##!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 7 by Diandra Vega - Unit tests for pig.py"""


import unittest
import pig


class gameTests(unittest.TestCase):
    """Unit tests for Pig game in pig.py"""
    max_score = 100


    def testGameEndsAtMaxScore(self):
        """Game exits when a player reaches a score of 100"""
        piggame = pig.playPig()
        player_one = pig.Player()
        player_two = pig.Player()
        plyr_one_score = player_one.score + self.max_score
        plyr_two_score = player_two.score + self.max_score
        with self.assertRaises(SystemExit) as cm:
            piggame.status(plyr_one_score, plyr_two_score)
        self.assertEqual(cm.exception.code, 1, "Game did not exit")


#    def testGameScoreDoesNotExceedMax(self):
#        """Docstring"""#


if __name__ == '__main__':
    unittest.main()
