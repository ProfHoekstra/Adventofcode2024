
# Read maze and measure dimensions
mazeorg = []
#f = open("test.txt","r")
f = open("input.txt","r")


for line in f.readlines():
    mazeorg.append(list(line.replace("\n","")))
    MX = len(mazeorg[-1])
f.close()
MY = len(mazeorg)

def printmaze():
    global maze,MY
    for y in range(MY):
        print(" ".join(maze[y]))
         
# Find starting position
hdgsymbols = ["^",">","v","<"]
for y in range(MY):
    for x in range(MX):
        if mazeorg[y][x] not in ["#","."]:
            x0 = x
            y0 = y
            hdg0 = hdgsymbols.index(mazeorg[y][x].lower())
            mazeorg[y][x]="X"

# Try different obstacles
nloop = 0
for yobst in range(MY):
    for xobst in range(MX):
        #print(yobst,xobst)
        maze = []
        for y in range(MY):
            maze.append(mazeorg[y].copy())
        swloop = False
        maze[yobst][xobst] = "O"
        
                

        # Start walk, using moves [dy,dx] with hdg as index (%4)
        moves = [[-1,0],[0,1],[1,0],[0,-1]]
        x = x0
        y = y0
        hdg = hdg0

        # Start walking
        while y>=0 and y<MY and x>=0 and x<MX and not swloop:
            newy = y + moves[hdg][0]
            newx = x + moves[hdg][1]
            if newx<0 or newy<0 or newx>=MX or newy>=MY:
                 break
            while maze[newy][newx]=="#" or maze[newy][newx]=="O":
                hdg = (hdg+1)%4
                newy = y + moves[hdg][0]
                newx = x + moves[hdg][1]
                if newx<0 or newy<0 or newx>=MX or newy>=MY:
                    break

            if newx<0 or newy<0 or newx>=MX or newy>=MY:
                 break
      
            x = newx
            y = newy

            if hdgsymbols[hdg]==maze[y][x]:
                swloop = True
                break
 
            maze[y][x]= hdgsymbols[hdg]

        # Check whether we are at start again
        if swloop:
            nloop = nloop+1
print("result =",nloop)
