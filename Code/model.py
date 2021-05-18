# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import matplotlib.pyplot as plot
import bat
import hawk
import matplotlib.animation as animate

num_of_bats = 20
num_of_hawks = 10
num_of_iterations = 100

habitat = []
bats = []
hawks = []

file = open('habitat.csv', newline='')
reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []		
    for value in row:
        rowlist.append(value)
    habitat.append(rowlist)
file.close()

fig = plot.figure(figsize=(100, 100))
ax = fig.add_axes([0, 0, 1, 1])
    
# make bat
for i in range(num_of_bats):
    bats.append(bat.NewBat(habitat, hawks))
    #testing: print(bats[i].colour)
    plot.scatter(bats[i].x, bats[i].y, c = bats[i].colour, s = 10)

# make hawk
for j in range(num_of_hawks):
    hawks.append(hawk.NewHawk(habitat))
    plot.scatter(hawks[j].x, hawks[j].y, c = "black", s = 10)

           
# move bat        
def update(frame_number):
    fig.clear()
    plot.imshow(habitat)
    for i in range (num_of_bats):
        bats[i].fly()
        plot.scatter(bats[i].x, bats[i].y, c = bats[i].colour, s = 10,)
        plot.show()
        #testing: print("i work")
        
    for j in range(num_of_hawks):
        hawks[j].fly()
        plot.scatter(hawks[j].x, hawks[j].y, c = "black", s = 10)
        plot.show()
    
animation = animate.FuncAnimation(fig, update, interval=100, repeat=False, frames=num_of_iterations)


