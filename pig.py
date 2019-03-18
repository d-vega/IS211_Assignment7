#!/usr/bin/env
# -*- coding: utf-8 -*-
"""IS211 Assignment 7 by Diandra Vega"""


import sys
import random


class Player(object):
    """Players in game of Pig"""
    def __init__(self, score=0):
        """Constructor"""
        self.score = score


    def score(self, points=0):
        """Tally player score"""
        self.score += points
        result = self.score
        return result


    def playTurn(self):
        """Player's turn results"""
        dice = list(xrange(1, 7))
        roll = "r"
        hold = "h"
        playerdecision = raw_input("Do you want to roll or hold? [r|h] ")

        if playerdecision is roll:
            diceroll = random.choice(dice)
            return diceroll
        elif playerdecision is hold:
            return playerdecision


class playPig(object):
    """Play a game of Pig"""
    playerone = Player()
    playertwo = Player()

    def status(self, firstscore, secondscore):
        """Check if any player hit a score of 100"""
        if firstscore >= 100:
            sys.exit(1)
        elif secondscore >= 100:
            sys.exit(1)
        else:
            return False


    def rollDice(self):
        """Play the game"""
        hold = "h"

        while self.status(playerone.score, playertwo.score) == False:
            playerone_turn = playerone.playTurn()

            if playerone_turn != 1 and playerone_turn is not hold:
                print playerone_turn
                continue
            elif playerone_turn == 1:
                print playerone_turn
                turn_ends = True
                return playerone_turn, turn_ends
                break
            elif playerone_turn is hold:
                print "Player holds"
                turn_ends = True
                return playerone_turn, turn_ends
                break


playerone = Player()
playertwo = Player()
playgame = playPig()


print playgame.rollDice()
