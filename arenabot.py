# Simple script that simulates a bot moving inside an Arena, following a series of commands
# by Alberto Tonda, 2018 <alberto.tonda@gmail.com>

import sys

'''This function accepts in input a list of strings, and tries to parse them to update the position of a robot. Then returns distance from objective.'''
def fitnessRobot(listOfCommands, visualize=False) :

	# the Arena is a 100 x 100 pixel space
	arenaLength = 100
	arenaWidth = 100
	
	# let's also put a couple of walls in the arena; walls are described by a set of 4 (x,y) corners (bottom-left, top-left, top-right, bottom-right)
	walls = []

	wall1 = dict()
	wall1["x"] = 30
	wall1["y"] = 0
	wall1["width"] = 10
	wall1["height"] = 80
    

	wall2 = dict()
	wall2["x"] = 70
	wall2["y"] = 20
	wall2["width"] = 10
	wall2["height"] = 80

	walls.append(wall1)
	walls.append(wall2)
    
	
	# initial position and orientation of the robot
	startX = robotX = 10
	startY = robotY = 10
	startDegrees = 90 # 90°
	
	# position of the objective
	objectiveX = 90
	objectiveY = 90
	
	# this is a list of points that the robot will visit; used later to visualize its path
	positions = []
	positions.append([robotX,robotY])
	
    
	# TODO move robot, check that the robot stays inside the arena and stop movement if a wall is hit
    #listOfCommands est de la forme ["move 20","rotate 90",...,]
    
    for command in listOfCommands:
        tab=command.split()
        mode=tab[0]
        deplacement=tab[1]
        
        if mode=="rotate":
            startDegrees+=(y%360)
            
        elif mode=="move":
            etat_mur=0
            
            #le robot va à gauche
            if startDegrees==0:
                proche_mur=walls[0]
                for wall in walls :
                    
                    #si le robot a croisé un mur 
                    if (robotX < wall["x"]) and robotX+deplacement>wall["x"]:
                        #on indique que le mur a croisé un mur
                        etat_mur=1
                        
                        #on actualise le mur le plus proche
                        if wall["x"]<proche_mur["x"]:
                            proche_mur=wall
                
                if etat_mur=1:
                    robotX=proche_mur["x"]
                elif etat_mur=0:
                    robotX=min(robotX+deplacement,100)

               
            #le robot va en haut
            elif startDegrees==90:
                proche_mur=walls[0]
                for wall in walls :
                    
                    #si le robot a croisé un mur
                    if (robotY < wall["y"]) and robotY+deplacement>wall["y"]:
                        #on indique que le mur a croisé un mur
                        etat_mur=1
                        #on actualise le mur le plus proche
                        if wall["y"]<proche_mur["y"]:
                            proche_mur=wall
                
                if etat_mur=1:
                    robotY=proche_mur["y"]
                elif etat_mur=0:
                    robotY=min(100,robotY+deplacement)
                    
                    
                #le robot va à gauche   
            elif startDegrees==180:
                proche_mur=walls[0]
                for wall in walls :
                    
                    #si le robot a croisé un mur
                    if (robotX > wall["x"]) and (robotX+deplacement<wall["x"]):
                        #on indique que le mur a croisé un mur
                        etat_mur=1
                        
                        #on actualise le mur le plus proche
                        if wall["x"]>proche_mur["x"]:
                            proche_mur=wall
                
                if etat_mur=1:
                    robotX=proche_mur["x"]
                elif etat_mur=0:
                    robotX=max(0,robotX-deplacement)
                
                    
                    
                 #le robot va en bas   
            elif startDegrees==270:
               proche_mur=walls[0]
                for wall in walls :
                    
                    #si le robot a croisé un mur
                    if (robotY > wall["y"]) and robotY+deplacement<wall["y"]:
                        #on indique que le mur a croisé un mur
                        etat_mur=1
                        #on actualise le mur le plus proche
                        if wall["y"]>proche_mur["y"]:
                            proche_mur=wall
                
                if etat_mur=1:
                    robotY=proche_mur["y"]
                elif etat_mur=0:
                    robotY=max(0,robotY-deplacement)
                    
        print(robotX,robotY)
        positions.append( [robotX, robotY] )


	# TODO measure distance from objective
    
	distanceFromObjective = abs(robotX-objectiveX) + abs(robotY-objectiveY)
	
	# this is optional, argument "visualize" has to be explicitly set to "True" when function is called
	if visualize :
		
		import matplotlib.pyplot as plt
		import matplotlib.patches as patches
		figure = plt.figure()
		ax = figure.add_subplot(111)
		
		# plot initial position and objective
		ax.plot(startX, startY, 'r^', label="Initial position of the robot")
		ax.plot(objectiveX, objectiveY, 'gx', label="Position of the objective")
		
		# plot the walls
		for wall in walls :
			ax.add_patch(patches.Rectangle( (wall["x"], wall["y"]), wall["width"], wall["height"] ))
		
		# plot a series of lines describing the movement of the robot in the arena
		for i in range(1, len(positions)) :
			ax.plot( [ positions[i-1][0], positions[i][0] ], [ positions[i-1][1], positions[i][1] ], 'r-', label="Robot path" )
		
		ax.set_title("Movements of the robot inside the arena")
		ax.legend(loc='best')
		plt.show()

	return distanceFromObjective




################# MAIN
def main() :
	
	# first, let's see what happens with an empty list of commands
	listOfCommands = [("move",20),("rotate",90),("move",10)]
	fitnessRobot(listOfCommands, visualize=True)
	
	return 0

if __name__ == "__main__" :
	sys.exit( main() )

