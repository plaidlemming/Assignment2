# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:18:54 2021

@author: Eliza
"""
import random


colour = ["white","red", "green", "blue"]

class NewBat():
    def __init__(self, habitat, bats):
        self.y = random.randint(0,100)
        self.x = random.randint(0,100)
        
        
        self.habitat = habitat
        self.bats = bats
        self.species = random.randint(1,3)
        self.colour = colour[self.species]
        
        #print(self.habitat[self.y][self.x])
        
        #print(self.colour)
    def fly(self):
        # Check to see if the current habitat under the bat
        # has the same value as the bat species
        # If is is different then keep moving 
        # Other wise stay still (do nothing)
        #if not self.habitat[self.y][self.x] == self.species:
        
            if random.random() < 0.5:
                self.y = (self.y + 1) % 100
            else:
                self.y = (self.y - 1) % 100
                
            if random.random() < 0.5:
                self.x = (self.x + 1) % 100
            else:
                self.x = (self.x - 1) % 100