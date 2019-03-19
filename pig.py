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


    def playerChoice(self):
        """Roll or hold?"""
        playerdecision = raw_input("Do you want to roll or hold? [r|h] ")

        while True:
            if playerdecision is 'r':
                roll = playerdecision
                return roll
                break
            elif playerdecision is 'h':
                hold = playerdecision
                return hold
                break
            else:
                print "Invalid choice."
                continue


    def totalScore(self, points=0):
        """Tally player score"""
        self.score += points
        result = self.score
        return result


class pig(object):
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


    def addScore(self, playerscore, total):
        """Add dice roll to turn total"""
        add_score = playerscore + total
        return add_score


    def rollDice(self, player, choice=None):
        """Roll the dice"""
        dice = list(xrange(1, 7))
        roll = 'r'
        hold = 'h'
        turntotal = 0

        while True:
            if choice is None:
                playerchoice = player.playerChoice()
            else:
                playerchoice = choice

            if playerchoice is roll:
                diceroll = random.choice(dice)
                print "You rolled a {}!".format(diceroll)

                if diceroll != 1:
                    turntotal += diceroll
                    continue
                elif diceroll == 1:
                    turntotal += diceroll
                    player.totalScore(self.addScore(player.score, turntotal))
                    turn_ends = True
                    result = "You rolled a {}. Your turn now ends. Your total" \
                             " score is {}. Next player turn starts" \
                             " now.".format(diceroll, player.score)
                    return diceroll, player.score, turn_ends
                    break
            elif playerchoice is hold:
                turn_ends = True
                return playerchoice, turn_ends
                break
