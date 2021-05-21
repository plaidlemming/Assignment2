# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:18:54 2021

@author: Eliza
"""
# Import the required libraries.
import random

# Create a "colour" variable and assign it a list of colours representing different bat species.
colour = ["white","red", "green", "blue"]

# Create "NewBat" class to make the bats fly, move to a valid tile and roost, and pass on infection.
class NewBat():
    # Set up class constructor.
    def __init__(self, habitat, habitat_size, hawks, bats, infection_distance, infected = False):
        self.habitat = habitat  # Save a link to the "habitat" variable within the class.
        self.bats = bats        # Save a link to the "bats" variable within the class.
        self.hawks = hawks      # Save a link to the "hawks" variable within the class.
        self.habitat_size = habitat_size    # Save a link to the "habitat_size" variable within the class.
        self.alive = True                   # Set the default state of bats to alive.
        self.roosted = False                # Set the default state of bats to be not roosted.
        self.species = random.randint(1,3)  # Assign each bat a random number between 1 and 3 correspnding to 3 different species.
        self.colour = colour[self.species]  # Assign each bat a colour corresponding to it's species.
        self.infected = infected            # Create a variable to save whether or not this bat is infected.
        self.infection_distance = infection_distance # Create a link to the "infection_distance" variable.
        self.y = random.randint(0, habitat_size - 1) # Set random y coordinate of the bat to within the habitat size.
        self.x = random.randint(0, habitat_size - 1) # Set random x coordinate of the bat to within the habitat size.
        
        # Testing to find value of habitat underneath bat (for roosting).
        # print(self.habitat[self.y][self.x])
    # Create function to make bats fly, move to a valid tile and get infected by other bats if within a given distance.
    def update(self):
        self.fly()
        
        # Iterate over each bat, if it is alive and infected, and the distance is greater than or equal to the "infection_distance", infect this bat.
        # Could split this out in to a "check_for_infection" function
        for bat in self.bats:
            if bat.infected == True:
                if bat.alive == True:
                    if self.distance_between(bat) <= self.infection_distance:
                        self.infected = True
                        
    # Create function to check if the bat is alive and not roosted, then run "move_to_valid_tile" function.                    
    def fly(self):
        if self.alive == True:
            if self.roosted == False:
                self.move_to_valid_tile()
                
    # Create function to move the bats (pre-select a tile and move there if valid) and have them stay in their preferred environment ('roost').            
    def move_to_valid_tile(self):           
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
                # And the habitat matches the species preference
                if self.habitat[newY][newX] == self.species:
                    # Move to that tile and roost (stay there).
                    self.y = newY
                    self.x = newX
                    # Testing that bats are roosting.
                    # print ("new home who dis")
                    self.roosted = True
                    validMove = True
                # If the habitat does not match the species preference, move but do not roost.
                else:
                    self.y = newY
                    self.x = newX
                    # Testing that bats are moving.
                    # print ("inside border not home tho :(")
                    validMove = True
            # Testing that no bats are travelling outside of the plot.
            # else:
                # print ("not in border why am I here")
                
    # Create a function to calculate the distance between the current bat and the others.
    def distance_between(self, bats):
        return (((self.x - bats.x)**2) + ((self.y - bats.y)**2))**0.5
        

# Make each species have a preference for it's habitat.
# red = woodland
# green = woodland edge
# blue = building
