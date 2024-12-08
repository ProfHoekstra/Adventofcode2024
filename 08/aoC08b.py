# Read maxe and measure dimensions
mazeorg = []
#f = open("testa.txt","r")
#f = open("testb.txt","r")
f = open("input.txt","r")


for line in f.readlines():
    mazeorg.append(list(line.replace("\n","")))
    MX = len(mazeorg[-1])
f.close()
MY = len(mazeorg)
maze = mazeorg

mazedotes= []
for i in range(MY):
    row = maze[i].copy()
    mazedotes.append(row)
    
def printmaze(maze):
    MY = len(maze)
    for y in range(MY):
        print(" ".join(maze[y]))

# Find each antenna
for ya in range(MY):
    for xa in range(MX):

        # Only look for second anenna further down
        # the maze to avoid counting pairs twice
        for yb in range(ya,MY):
            for xb in range(0,MX):
                # On this line skip till incl xb=xa
                if yb==ya and xb<=xa:
                    continue

                if maze[ya][xa]!="." and maze[ya][xa]!="#" and\
                   maze[ya][xa]==maze[yb][xb]:
                    dy = yb-ya # always positive
                    dx = xb-xa # sign may vary

                    # Search direction of a
                    newx0 = xa
                    newy0 = ya
                    while 0<=newx0<MX and 0<=newy0<MY:
                        newy0 = newy0-dy
                        newx0 = newx0-dx
                        if 0<=newx0<MX and 0<=newy0<MY: 
                            mazedotes[newy0][newx0]="#"

                    #Search direction of b
                    newy1 = yb
                    newx1 = xb
                    while 0<=newx1<MX and 0<=newy1<MY:
                        newy1 = newy1+dy
                        newx1 = newx1+dx
                        if 0<=newx1<MX and 0<=newy1<MY:
                            mazedotes[newy1][newx1]="#"
                    


# Count "#"
                    
count = 0
for iy in range(MY):
    for ix in range(MX):
        if mazedotes[iy][ix]=="#" or maze[iy][ix]!=".":
            count = count+1

# Result
print("count = ",count)


                
                
                
