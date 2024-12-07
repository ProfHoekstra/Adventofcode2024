goals = []
termen = []

# Read data and make tables
#f = open("test.txt","r")
f = open("input.txt","r")
for line in f.readlines():
    goaltxt,somtxt = line.split(":")
    goals.append(int(goaltxt))
    termtxt = somtxt.replace("\n","").split()
    row = []
    for txt in termtxt:
        row.append(int(txt))
    termen.append(row)
f.close()

# Initialisation
total = 0 # sum of correct outcomes
N = len(goals)

# Try all problems one by one

for i in range(N):
    results = [termen[i][0]] # list to keep potential outcomes

    #for each temrm calculate two offsprings in next generation results
    for term in termen[i][1:]:
        newresults = []
        for result in results:
            newresults.append(result*term)
            newresults.append(result+term)
        results = newresults.copy()
    if goals[i] in results:
        total = total + goals[i]

print("Total =",total)

            
        
