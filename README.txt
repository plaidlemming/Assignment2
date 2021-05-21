Contents:

'Code' folder contains: 
	- model.py (main source code)
	- bat.py (bat source code)
	- hawk.py (hawk source code)
	- habitat.csv (habitat data that is read in)
	- habitat10cells.csv (small test habitat data)
	- habitat50cells.csv (medium sized test habitat data)

This software is intended to model how a spreading infectious disease in the bat population affects the hawk population that preys on them.

How to run:
	- Open the the code folder in your chosen Python IDE
	- Run program.
	- Runs best on a faster processor.

When the software runs it will:
	- Take in the habitat.csv data to form the habitat to plot bats and hawks on
	- Generate an animation of bats and hawks movement and death in a new window
	- Create a new text file called 'modelStatistics', to write the number of bats and hawks alive at the start and end, along with the number of infected bats at the start and end. This file will be updated every time the model runs.