# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import matplotlib.pyplot as plot
import bat
import matplotlib.animation as animate
import time

num_of_bats = 10
num_of_iterations = 10

habitat = []
bats = []

file = open('environment.csv', newline='')
reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []		
    for value in row:
        rowlist.append(value)
    habitat.append(rowlist)
file.close()

fig = plot.figure(figsize=(100, 100))
ax = fig.add_axes([0, 0, 1, 1])


#plot.ylim(0, 100)
#plot.xlim(0, 100)


plot.imshow(habitat)
plot.show()

    
# make bat
for i in range(num_of_bats):
    bats.append(bat.NewBat(habitat, bats))
    #print(bats[i].colour)
    plot.scatter(bats[i].x, bats[i].y, c = bats[i].colour, s = 10)
    #plot.scatter(bats[i].x,bats[i].y)
           
        
def update(frame_number):
    #fig.clear()
    
    #plot.imshow(habitat)
    for j in range (num_of_bats):
        bats[i].fly()
        
        plot.scatter(bats[i].x, bats[i].y, c = bats[i].colour, s = 10)
    
    '''
    for j in range(100):
        for k in range (100):
            plot.scatter(k,j,habitat[k][j])
 
    '''

'''    
for j in range (num_of_iterations):
    for i in range(num_of_bats):
        bats[i].fly()
    time.sleep(1)
    print("i work")
'''  
'''  
plot.scatter(bats[i].x, bats[i].y, c = bats[i].colour, s = 10)
plot.show
update()
'''
'''  
update()
time.sleep(1)
update()
time.sleep(1)
update()
time.sleep(1)
update()
time.sleep(1)
update()
time.sleep(1)
'''
'''
for k in range(10):
    update()
    time.sleep(1)
'''   
    
#animation = animate.FuncAnimation(fig, update, interval=1000, repeat=False, frames=num_of_iterations)
#plot.show()