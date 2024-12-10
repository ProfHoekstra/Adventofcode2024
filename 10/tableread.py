# Read ASCII table from file

# example file:
#  0123
#  1234
#  8765
#  9876

def read2Dlist(fname): # returns ascii chraacter array
    table = []
    f = open(fname,"r")

    for line in f.readlines():
        if len(line.strip())>0:
            table.append(list(line.replace("\n","")))
    
    f.close()

    NY = len(table)
    NX = len(table[-1])

    return table,NY,NX

def read2Dlistint(fname): # returns ascii chraacter array
    table = []
    f = open(fname,"r")

    for line in f.readlines():
        if len(line.strip())>0:
            row = []
            for ch in line.replace("\n",""):
                row.append(int(ch))
            table.append(row)

    f.close()

    NY = len(table)
    NX = len(table[-1])

    return table,NY,NX
