import numpy as np

# Lists to sort
lst1 = []
lst2 = []

# Fill lists each with a column of numbers from data file
f = open("data.txt","r")
for line in f.readlines():
    recs = line.strip().split()
    lst1.append(int(recs[0].strip()))
    lst2.append(int(recs[1].strip()))
f.close()

# Sort both
lst1.sort()
lst2.sort()

# Calculate distance
dist = sum(np.abs(np.array(lst1)-np.array(lst2)))

print("Distance =",dist)



                
