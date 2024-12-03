"""
safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.

How many reports are safe?
"""

def read2Dlstint(filename):
    """ Read a data file with records of unequal length
        into a 2D list with integers"""
    lst = []
    f = open(filename,"r")
    for line in f.readlines():
        if len(line.strip())==0:
            continue
        lst.append([])
        recs = line.strip().split()
        for txt in recs:
            lst[-1].append(int(txt.strip()))
    f.close()
    return lst
                           

def issafe(row):
    safe = False
    if row[0]==row[1]:
        safe = False
    else:
        if row[0]<row[1]:
            dy = 1
        else:
            dy = -1

        safe = True
        for i in range(len(row)-1):
            # check sign
            delta = row[i+1]-row[i]
            if delta*dy<=0 or abs(delta)<1 or abs(delta)>3:
                safe = False
                continue
    return safe



nsafe = 0

#table = read2Dlstint("test.txt")
table = read2Dlstint("input.txt")

print (len(table),"reports read")

for row in table:    
    rowsafe = False
    if issafe(row):
        rowsafe = True
    else:
        # Remove first element
        newrow = row[1:]
        if issafe(newrow):
            rowsafe = True
        else:
            # remove last element
            newrow = row[:-1]
            if issafe(newrow):
                rowsafe = True
            else:
                for i in range(len(row)-2):
                    j = i+1
                    newrow = row[:j]+row[j+1:]
                    if issafe(newrow):
                        rowsafe = True
                        continue
                   
           

    if rowsafe:
        nsafe= nsafe + 1
        print (row,"safe")
    else:
        print(row,"unsafe")
        

print ("nsafe= ",nsafe)                      
        
    

print("Number of safe records ",nsafe)


                
