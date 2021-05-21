# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import required libraries.
import csv
#import matplotlib.use('TkAgg')
import matplotlib.pyplot as plot
import bat
import hawk
import matplotlib.animation as animate
#import tkinter

# Assign values to variables.
habitat_size = 100       # Create variable and assign it a habitat size corresponding to the inputted habitat csv.
num_of_iterations = 50  # Create variable and assign it a number of iterations for the model.

num_of_bats = 60        # Create variable and assign it a number of bats.
num_of_hawks = 30        # Create variable and assign it a number of hawks.

starting_infected_bats = 20 # Create variable and assign it a number of bats to start with an infection.
infection_distance = 5  # Create variable and assign it a distance at which bats transmit infection.


# Create empty lists for the habitat, bats and hawks.
habitat = []
bats = []
hawks = []

# Open the habitat csv and save it to the variable "file".
file = open('habitat.csv', newline='')
# Parse the file and save to a "reader" variable.
reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)

# Iterate over the "reader" variable and save it to "habitat".
for row in reader:
    rowlist = []		
    for value in row:
        rowlist.append(value)
    habitat.append(rowlist)
file.close()

# Create a plot that the model will be viewed on.
fig = plot.figure(figsize=(habitat_size, habitat_size),facecolor="purple") # Set the extent of the plot using the habitat size variable and assign it the variable "fig".
ax = fig.add_axes([0, 0, 1, 1]) # Add axes and assign them the variable "ax".

    
# Make the bats by iterating over the number of bats variable and appending the new instant of the bat to the "bats" variable.
for i in range(num_of_bats):
    # Make the specified number of bats "infected" with a disease.
    if i < starting_infected_bats:
        bats.append(bat.NewBat(habitat, habitat_size, hawks, bats, infection_distance, True))
    # The rest of the bats are not infected.
    else:
        bats.append(bat.NewBat(habitat, habitat_size, hawks, bats, infection_distance))
    # Plot all of the bats. The colour of each bat species is set in the bat class and referenced here.
    plot.scatter(bats[i].x, bats[i].y, c = bats[i].colour, s = 10)


# Make the hawks by interating over the number of hawks variable and appending the new instant of the hawk to the "hawks" variable.
for j in range(num_of_hawks):
    hawks.append(hawk.NewHawk(habitat, habitat_size, bats))
    # Plot the hawks. 
    plot.scatter(hawks[j].x, hawks[j].y, c = "black", s = 10)

# Create "update" function to advance one step for every iteration.      
def update(frame_number):
    fig.clear()
    plot.imshow(habitat)
    
    # Iterate over each bat, running the "bats.update" function.
    for i in range (num_of_bats):
        bats[i].update()
        # print(bats[i].x, bats[i].y) # Used to check the bats' location was updating.
        # Only show the bats on the plot when they are alive.
        if bats[i].alive:
            plot.scatter(bats[i].x, bats[i].y, c = bats[i].colour, s = 10,)
            plot.show()

    # Iterate over each hawk, running the "hawks.update" function.        
    for j in range(num_of_hawks):
        hawks[j].update()
        # Only show the hawks on the plot if they are alive.
        if hawks[j].alive:
            plot.scatter(hawks[j].x, hawks[j].y, c = "black", s = 10)
            plot.show()
            
    # Print the statistics at the final iteration of the model.     
    if frame_number == num_of_iterations - 1:
        print_stats()

# Animate the model using the FuncAnimation function from the matplotlib library, refreshing every 150 ms without repeating.
animation = animate.FuncAnimation(fig, update, interval=150, repeat=False, frames=num_of_iterations)

# Testing without any plots or animation turned on.
# for i in range(num_of_iterations):
#     update(1)
#     print(i)

# Create the "print_stats" function to print the statistics at the final iteration.
def print_stats():
    alive_bats = 0              # Create variable and assign it the number of alive bats at the start of counting.
    alive_hawks = 0             # Create variable and assign it the number of alive hawks at the start of counting.
    num_of_infected_bats = 0    # Create variable and assign it the number of infected bats at the start of counting.
    
    # Iterate over each bat, adding 1 to the "alive_bats" variabe if the bat is alive at the end.
    for i in range (num_of_bats):
        if bats[i].alive:
            alive_bats += 1
        # If a bat is infected, add 1 to the "num_of_infected_bats" variable.
        if bats[i].infected:
            num_of_infected_bats += 1
            
    # Iterate over each hawk, adding 1 to the "alive_hawks" variabe if the hawk is alive at the end.    
    for j in range(num_of_hawks):
        if hawks[j].alive:
            alive_hawks += 1
    
    
    # Print starting and ending conditions to a text file.
    
    initial_conditions = "Starting Bats: {}, Starting Hawks: {}, Starting Infected Bats: {}\n".format(num_of_bats, num_of_hawks, starting_infected_bats)    
    final_conditions = "Final Alive Bats: {}, Final Alive Hawks: {}, Final Infected Bats: {} \n".format(alive_bats, alive_hawks, num_of_infected_bats)
    
    # Print to console.
    print(initial_conditions)
    print(final_conditions)
    
    # Write to text file.
    with open('modelStatistics.txt', "a") as txt:
        txt.write(initial_conditions)
        txt.write(final_conditions)
        txt.write("\n")
