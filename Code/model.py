# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
#import matplotlib.use('TkAgg')
import matplotlib.pyplot as plot
import bat
import hawk
import matplotlib.animation as animate
#import tkinter

num_of_bats = 50
num_of_hawks = 60
num_of_iterations = 10

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

fig = plot.figure(figsize=(50, 50))
ax = fig.add_axes([0, 0, 1, 1])
    
# make bat
for i in range(num_of_bats):
    
    if i == 0:
        bats.append(bat.NewBat(habitat, hawks, True))
    else:
        bats.append(bat.NewBat(habitat, hawks))
    plot.scatter(bats[i].x, bats[i].y, c = bats[i].colour, s = 10)


# make hawk
for j in range(num_of_hawks):
    hawks.append(hawk.NewHawk(habitat, bats))
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
        hawks[j].update()
        plot.scatter(hawks[j].x, hawks[j].y, c = "black", s = 10)
        plot.show()

animation = animate.FuncAnimation(fig, update, interval=10, repeat=False, frames=num_of_iterations)
#for i in range(num_of_iterations):
    #update(1)

alive_bats = 0
alive_hawks = 0

num_of_infected_bats = 0

for i in range (num_of_bats):
    print(bats[i].alive)
    if bats[i].alive:
        alive_bats += 1
    
    if bats[i].infected:
        num_of_infected_bats += 1
        
for j in range(num_of_hawks):
    if hawks[j].alive:
        alive_hawks += 1
       
print(num_of_bats - alive_bats, num_of_hawks - alive_hawks, num_of_infected_bats)
    
    
'''
def run():
    pass
    canvas.show()
root = tkinter.Tk() 
root.wn_title("Bats and Hawks")
    
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()
'''