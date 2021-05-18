# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:25:22 2021

@author: Eliza
"""

import random

class NewHawk():
    def __init__(self, habitat):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.habitat = habitat
    
    def fly(self):
            validMove = False

            while (validMove == False):
                if random.random() < 0.5:
                    newY = (self.y + 1)
                else:
                    newY = (self.y - 1)
                    
                if random.random() < 0.5:
                    newX = (self.x + 1)
                else:
                    newX = (self.x - 1)

                if 0 <= newY <= 99 and 0 <= newX <= 99:
                   
                    self.y = newY
                    self.x = newX
                    
                    validMove = True
