# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:25:22 2021

@author: Eliza
"""

import random

class NewHawk():
    def __init__(self, habitat, bats):
        self.y = 0
        self.x = 0
        self.habitat = habitat
        self.bats = bats
        self.find_woodland()
        self.alive = True
        
    def update(self):
        self.fly()  
        self.find_and_eat_bats()
    
    # Move hawks depending on a random number, as long as they're within the bounds of the map and within woodland
    def fly(self):
        if self.alive == True:
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

                if 0 <= newY <= 49 and 0 <= newX <= 49:
                     if self.habitat[newY][newX] == 1:
                   
                        self.y = newY
                        self.x = newX
                        
                        validMove = True
            
    def find_and_eat_bats(self):
        for bat in self.bats:
           if self.x == bat.x and self.y == bat.y:
              #if random.random() < 0.7:
                  if bat.infected == True:
                    self.alive = False
                    bat.alive = False
                    #print("yummy bat")

    # Choose new coordinates and check if it is woodland, if not, choose another set until it is, then move there
    def find_woodland(self):
        validMove = False
        
        while (validMove == False):
            newX = random.randint(0,49)
            newY = random.randint(0,49)
            
            if self.habitat[newY][newX] == 1:
                self.x = newX
                self.y = newY
                # print("i got wood ladies")
                validMove = True


            
            
            