from tableread import read2Dlistint as readtab
from copy import deepcopy

#table,NY,NX = readtab("test.txt")

table,NY,NX = readtab("input.txt")

# List of trailheads (value=0)
heads = [] # per trailhead: y,x,score
for i in range(NY):
    for j in range(NX):
        if table[i][j]==0:
            heads.append([i,j,0])

# Per trailhead make paths
# In part a keeping scores per trailhead not really
# neccessary yet. As result is simply number of paths

neighbours = [(-1,0),(1,0),(0,1),(0,-1)]
totala,totalb = 0,0# total nr of reacable nines and number of paths

for itrail,trailhead in enumerate(heads):
    y0,x0,score = trailhead

    #  List of where we are
    curyxlst = [(y0,x0)]

    # Search for path by finding increasing values

    for value in range(1,10): # 9 steps
        newyxlst = []

        for pos in curyxlst:
            y,x = pos
            for n in neighbours:
                dy,dx = n
                yn, xn = y+dy,x+dx
                if 0<=yn<NY and 0<=xn<NX  and \
                         table[yn][xn]==value: # except for index in table
                    newyxlst.append((yn,xn)) # x,y in xylst!
            
        # Shift xylst for next value = next step            
        curyxlst = newyxlst # deepcopy to be safe?
        #print(value,curyxlst)
        

    
    scorea = len(set(curyxlst))
    scoreb = len(curyxlst)
    #print(curyxlst)
    #print(x0,y0,score)
    totala = totala + scorea
    totalb = totalb + scoreb
    heads[itrail] = (y0,x0,score) # back to y,x in list

# Print result:
print("Score a, total nr of nine = ",totala)
print("Score b, total nr of paths = ",totalb)
            
    



