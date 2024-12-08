
# Read maze and measure dimensions
maze = []
#f = open("test.txt","r")
f = open("input.txt","r")


for line in f.readlines():
    maze.append(list(line.replace("\n","")))
    MX = len(maze[-1])
f.close()
MY = len(maze)

def printmaze():
    global maze,MY
    for y in range(MY):
        print("".join(maze[y]))
         
# Find starting position
for y in range(MY):
    for x in range(MX):
        if maze[y][x] not in ["#","."]:
            x0 = x
            y0 = y
            hdg = ["^",">","v","<"].index(maze[y][x].lower())
            maze[y][x]="X"

# Start walk, using moves [dy,dx] with hdg as index (%4)
moves = [[-1,0],[0,1],[1,0],[0,-1]]
x = x0
y = y0

# Start walking
while y>=0 and y<MY and x>=0 and x<MX:
    newy = y + moves[hdg][0]
    newx = x + moves[hdg][1]
    if newx<0 or newy<0 or newx>=MX or newy>=MY:
         break
    while maze[newy][newx]=="#":
        hdg = (hdg+1)%4
        newy = y + moves[hdg][0]
        newx = x + moves[hdg][1]
        if newx<0 or newy<0 or newx>=MX or newy>=MY:
            break

    if newx<0 or newy<0 or newx>=MX or newy>=MY:
         break

    x = newx
    y = newy
    maze[y][x]="X"

# Count X's (could have been done along the way but then we might double count
nX = 0
for y  in range(MY):
    for x in range(MX):
        if maze[y][x]=="X":
            nX =nX + 1

print("result =",nX)
