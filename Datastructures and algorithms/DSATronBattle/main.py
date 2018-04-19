# Fredrik Stoltz, IoT17, DSA-kursen, Tron-Battle

# Diskussionsgrupp: John, Anton, Philip, Hampa, Patrik


import sys

# Constants:
WIDTH = 30
HEIGHT = 20

# Data structure: store the battlefield as a 2D array of size WIDTH x HEIGHT
# Set all cells to -1 to mark them as empty
grid = []
for i in range(WIDTH):
   x = []
   for j in range(HEIGHT):
       x.append(-1)
   grid.append(x)
   
   
#Recursively determine the direction with most empty spaces (in a straight line)
def recSpace(direction, x, y, counter=0):
        if direction =="LEFT":
            try:
                if x <= 1 or grid[x-1][y] != -1:
                    tempdir="LEFT"
                    return (counter, tempdir)
                else:
                    return recSpace(direction, x-1, y, counter+1)
            except IndexError: # IndexError indicates we are at the edge of the playing field,
                               # we can then return the counter and tempdir
                return counter, tempdir
                
        elif direction =="RIGHT":
            try:
                if x >= 19 or grid[x+1][y] != -1:
                    tempdir="RIGHT"
                    return (counter, tempdir)
                else:
                    return recSpace(direction, x+1, y, counter+1)
            except IndexError:
                return counter, tempdir
                
        elif direction =="UP":
            try:
                if y <= 1 or grid[x][y-1] != -1:
                    tempdir="UP"
                    return (counter, tempdir)
                else:
                    return recSpace(direction, x, y-1, counter+1)
            except IndexError:
                return counter, tempdir
                
        elif direction =="DOWN":
            try:
                
                if y >= 19 or grid[x][y+1] != -1:
                    tempdir="DOWN"
                    return (counter, tempdir)
                else:
                    return recSpace(direction, x, y+1, counter+1)
            except IndexError:
                return counter, tempdir

# Function that returns a list containing directions that does not kill us
def options():
    options = []    
    if (my_x+1) < WIDTH and grid[my_x+1][my_y] == -1:
        options.append("RIGHT")
    if (my_x-1) >= 0 and grid[my_x-1][my_y] == -1:
        options.append("LEFT")
    if (my_y+1) < HEIGHT and grid[my_x][my_y+1] == -1:
        options.append("DOWN")
    if (my_y-1) >= 0 and grid[my_x][my_y-1] == -1:
        options.append("UP")
    return options


# This function runs when it's no longer possible to move in 
# the direction with most free space that we initially chose.
def getNextDir():
    rowspace = [] # max antal steg i varje direction
    dirlist = [] # possible directions will be appended into this array
    directions=options()
        
    for direction in directions:
        (possibleSteps, nameOfDir) =recSpace(direction, my_x, my_y)
        rowspace.append(possibleSteps) # Append an integer, representing the total steps possible in that direction
        dirlist.append(nameOfDir) # Append the actual string, containing the direction. 
        
    bestOption = max(rowspace) # Determine the element with most empty spaces in front(biggest integer)
    
    for i in range(len(rowspace)):
       if rowspace[i] == bestOption:
           nextDir = dirlist[i]
           return nextDir


gameOn=False
nextDir=None

# loop forever
while True:
    # n: total number of players (2 to 4).
    # p: your player number (0 to 3).
    n, myself = [int(i) for i in input().split()]
    
    # Read in data for where all players are right now:
    for player in range(n):
      #x0/y0 - starting position, x1/y1 - current position
       x0, y0, x1, y1 = [int(j) for j in input().split()]
       grid[x1][y1] = player
       grid[x0][y0] = player
       
       if player == myself:
           my_x = x1
           my_y = y1

    printed = False # boolean 'printed' takes care of the Queue issue with printing
    nextAvailable = options() # Get possible directions for our next move
    
    print("nextAvailable: {}".format(nextAvailable), file=sys.stderr)
    
    if gameOn == False: #First turn
        nextDir=getNextDir() # Get initial direction
        gameOn=True # Set gameOn to True so we don't enter this piece of code again
        print(nextDir)
        printed=True
            
    if nextDir not in nextAvailable: # if the direction we are currently going is no longer feasable,
        nextDir = getNextDir()       # get a new direction
        if not printed:
            print(nextDir)
            printed=True
    
    print("Continue going: {}".format(nextDir), file=sys.stderr)
    
    if not printed: # If we haven't printed anything, continue going in the same direction
        print(nextDir, file=sys.stdout)