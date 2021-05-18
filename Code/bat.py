# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:18:54 2021

@author: Eliza
"""
import random

colour = ["white","red", "green", "blue"]

class NewBat():
    def __init__(self, habitat, hawks):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        
        #self.y = 98
        #self.x = 98
        
        self.roosted = False
        self.habitat = habitat
        self.hawks = hawks
        self.species = random.randint(1,3)
        self.colour = colour[self.species]
        
        # testing: print(self.habitat[self.y][self.x])
        
    def fly(self):
        if self.roosted == False:
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
            
                #print (newX, newY, self.habitat[newY][newX])
                if 0 <= newY <= 99 and 0 <= newX <= 99:
                    if self.habitat[newY][newX] == self.species:
                        
                        self.y = newY
                        self.x = newX
                        
                        #print ("new home who dis")
                        
                        self.roosted = True
                        validMove = True
                    else:
                        self.y = newY
                        self.x = newX
                        
                        #print ("inside border not home tho :(")
                        validMove = True
                #else:
                    #print ("not in border wyd here bro")




# make some bats avoid some habitat
# red = woodland
# green = woodland edge
# blue = building

# chose a new x and y value
# check to see if it's in the bounds of the map
# check to see if the environment at that point is something the bat avoids
# check to see if it's the roosting habitat for that bat

# create hawks that spawn randomly and move in the same way as bats
    # create a hawk 'derived' class from the bat 'base class' - didn't work lol who do i think i am
# create function to make hawks 'eat' bats
    # loop through bats, calculate distance to nearest hawk
    # if distance is less than 5(?) bat will be eaten
    # assign it a 'dead' variable
    # amend bat plotting loop - if 'dead' do not plot

# setting roosting habitat in 'fly' function pre-while loop  
# if not self.habitat[self.y][self.x] == self.species:          
''' implement later
def getx(self):
    return self._x
    
    def setx(self, VALUE):
        self._x = VALUE
        
    def delx(self):
        del self._x
        
    #x = property(getx, setx, delx, "i'm the x property")
    
    def gety(self):
        return self._y
    
    def sety(self, VALUE):
        self._y = VALUE
        
    def dely(self):
        del self._x
        
    #y = property(gety, sety, dely, "i'm the y property")
'''