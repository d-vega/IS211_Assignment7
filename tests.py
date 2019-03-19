##!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 7 by Diandra Vega - Unit tests for pig.py"""


import unittest
import pig


class gameTests(unittest.TestCase):
    """Unit tests for Pig game in pig.py"""
    max_score = 100
    dice_rolls = list(xrange(1, 7))


    def testGameEndsAtMaxScore(self):
        """Game exits when a player reaches a score of 100"""
        piggame = pig.pig()
        player_one = pig.Player()
        player_two = pig.Player()
        plyr_one_score = player_one.score + self.max_score
        plyr_two_score = player_two.score + self.max_score
        with self.assertRaises(SystemExit) as cm:
            piggame.status(plyr_one_score, plyr_two_score)
        self.assertEqual(cm.exception.code, 1, "Game did not exit")


    def testTurnEndsAtOne(self):
        """Player turn ends at dice roll of one"""
        playgame = pig.pig()
        playerone = pig.Player()
        result = playgame.rollDice(playerone, 'r')
        if result[2] == True:
            self.assertEqual(result[2], True, "Turn did not end at 1")


    def testPlayerHold(self):
        """Turn ends if player holds"""
        playgame = pig.pig()
        playerone = pig.Player()
        result = playgame.rollDice(playerone, 'h')
        self.assertEqual(result, ('h', True), "Turn did not end at hold")


    def testScoreAddsToTotal(self):
        """Turn score adds to total"""
        playgame = pig.pig()
        playerone = pig.Player()
        rolldice = playgame.rollDice(playerone, 'r')
        if rolldice[2] == True:
            self.assertEqual(rolldice[1], playerone.score,
                             "Score did not add to total score")


if __name__ == '__main__':
    unittest.main()
