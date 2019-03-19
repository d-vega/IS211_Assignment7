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
        piggame = pig.Pig()
        player_one = pig.Player()
        player_two = pig.Player()
        plyr_one_score = player_one.score + self.max_score
        plyr_two_score = player_two.score + self.max_score
        with self.assertRaises(SystemExit) as cm:
            piggame.status(plyr_one_score, plyr_two_score)
        self.assertEqual(cm.exception.code, 1, "Game did not exit")


    def testTurnEndsAtOne(self):
        """Player turn ends at dice roll of one"""
        player = pig.Player()
        result = pig.processTurn(player, 'r')
        while True:
            if result == (1, True):
                self.assertEqual(result, (1, True), "Turn did not end at 1")
                break
            else:
                continue


    def testPlayerHold(self):
        """Turn ends if player holds"""
        playgame = pig.Pig()
        playerone = pig.Player()
        result = playgame.rollDice(playerone, 'h')
        self.assertEqual(result[0], 'h', "Turn did not end at hold")


    def testScoreAddsToTotal(self):
        """Turn score adds to total"""
        playgame = pig.Pig()
        playerone = pig.Player()
        rolldice = playgame.rollDice(playerone, 'r')
        self.assertEqual(rolldice[0], playerone.score,
                         "Score did not add to total score")


if __name__ == '__main__':
    unittest.main()
