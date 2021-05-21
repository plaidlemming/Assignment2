# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:25:22 2021

@author: Eliza
"""
# Import the required libraries.
import random

# Create "NewHawk" class to move the hawks, make them find and eat bats and die if they eat an infected bat.
class NewHawk():
    # Set up class constructor.
    def __init__(self, habitat, habitat_size, bats):
        self.habitat = habitat           # Save a link to the "habitat" variable within the class.
        self.habitat_size = habitat_size # Save a link to the "habitat_size" variable within the class.
        self.bats = bats                 # Save a link to the "bats" variable within the class.
        self.y = 0              # Set the starting y coordinate to 0 (this is changed in the "find_habitat" function).
        self.x = 0              # Set the starting x coordinate to 0 (this is changed in the "find_habitat" function).
        self.alive = True       # Set the default state of the hawks as alive.
        self.hunting_ground = 0 # Set the habitat type that the hawks are spawned in and stay in.
        self.find_habitat(self.hunting_ground) # Run the find habitat function to find initial habitat of new hawk.
        
    # Create update function to run the "fly" and "find_and_eat_bats" functions.    
    def update(self):
        self.fly()  
        self.find_and_eat_bats()
    
    # Create function to move hawks depending on a random number, as long as they're alive, within the bounds of the map and within the chosen hunting ground.
    def fly(self):
        if self.alive == True:
            validMove = False
            # If the pre-selected tile is not valid, select another tile.
            while (validMove == False):
                # Based on a random number, select one tile up or down.
                if random.random() < 0.5:
                    newY = (self.y + 1)
                else:
                    newY = (self.y - 1)
                # Based on a random number, select one tile left or right.                        
                if random.random() < 0.5:
                    newX = (self.x + 1)
                else:
                    newX = (self.x - 1)
                # If the newly selected tile is within the bounds of the map
                if 0 <= newY <= self.habitat_size - 1 and 0 <= newX <= self.habitat_size - 1:
                    # And within the chosen hunting ground
                    if self.habitat[newY][newX] == self.hunting_ground:
                        # Move there.
                        self.y = newY
                        self.x = newX
                        validMove = True
        
    # Create a function to find and eat bats. If the bat is infected, the hawk dies.        
    def find_and_eat_bats(self):
        # Iterate over each bat, and catch and eat it with a 70% success rate.
        for bat in self.bats:
           # Testing that the hawk and bat are at the same location. 
           # print(bat.x, bat.y, self.x, self.y)
           
           # If the hawk and bat are at the same location, it can be eaten.
           if self.x == bat.x and self.y == bat.y:
                if random.random() < 0.7: # This is where the 'success rate' is set.
                   bat.alive = False
                   # Testing that the hawks are 'eating' the bats.
                   # print(bat.alive,"yummy bat")

                   # If the bat is infected, the hawk dies.
                   if bat.infected == True:
                       self.alive = False
                       # Testing that the hawks are 'dying'.
                       #print(self.alive, "oh no, I died")
            
    # Choose new coordinates and the habitat at that location, if not the chosen habitat type in self.hunting_ground, choose another set until it is, then move there
    def find_habitat(self, habitat_type):
        validMove = False        
        
        # Select another tile randomly.
        while (validMove == False):
            # Randomly select a new tile.
            newX = random.randint(0, self.habitat_size - 1)
            newY = random.randint(0, self.habitat_size - 1)
            
            # If the new tile is in the chosen habitat type, move there.
            if self.habitat[newY][newX] == habitat_type:
                self.x = newX
                self.y = newY
                validMove = True
        

            