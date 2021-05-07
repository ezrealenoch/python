SpaceInvaders README
Enoch Wang
4/30/2020
Final Project: Space Invaders
CSCI 6651
Professor Gulnora Nurmatova 


INSTRUCTIONS:

	1) Install pygame module. This can be done by opening your python enviorment and executing the command "pip install pygame"
	Ensure that the enviorment has pip already installed. Versions of pip can be displayed with the command "pip freeze"
	
	2) Navigate to SpaceInvaders.py directory with python enviorment and run with command "python SpaceInavders.py"
	
	3) Ship controls are "left and right arrow keys" to move, "space" to launch rockets, and "z" shoots a bomb that clears the whole level (no points for using bomb).
	
	4) Aliens will speed up!
	
	5) Each level spawns in a increasing number of obsticles that cannot be shot through
	
	6) Goal is to destroy all alien ships before they cross to the user's side! Good luck!
	
	
Extra Credit 1: Auto-generated levels 
	- Each round has obsticles that are generated in random locations. Each round has an increasing number of obsticles. 
	- The first three rounds introduces a new row of aliens to fight
	- Each round past the round three speeds up the alien's approach by 0.05 
	- For every 100 points the user scores, the aliens also speed up by 0.05
	
Extra Credit 2: Different Shooting Ability
	- User has the option to launch a Bomb with "z"
	- Bomb will whipe out all the remaining aliens in the level if it hits an alien
	- User gain a new bomb every 100 points. 
	- Bombs move slower and are indicated by a different shape and color.
	
	