
def correct(rec,rules):
    correct = True
    for rule in rules:
        if rule[0] in rec and rule[1] in rec:
            i0 = rec.index(rule[0])
            i1 = rec.index(rule[1])
            if i0>i1:
                correct = False
                break
    return correct            


f = open("input.txt","r")
#f = open("test.txt","r")


# Instructions first, store in rules
rules = []
recs = []
swrules = True
for line in f.readlines():
    if swrules:
        # Empty line => break
        if line.strip()=="" or line.count("|")==0:
            swrules = False
            continue
        
        cols = line.strip().split("|")
        rules.append([int(cols[0]),int(cols[1])])

# Now records
    else:
        if line.strip()=="":
            continue
        strings = line.strip().split(",")
        print("strings=",strings)
        record = []
        for txt in strings:
            record.append(int(txt))

        # Add the record
        recs.append(record)

# Check rules and multiply middle
result = 0
tosort = []
for rec in recs:
    # Correct? Multiply
    if not correct(rec,rules):
#    else:
        tosort.append(rec+[])

# Sort them:
for irec in range(len(tosort)):
    while not correct(tosort[irec],rules):
        for rule in rules:
            if rule[0] in tosort[irec] and rule[1] in tosort[irec]:
                i0 = tosort[irec].index(rule[0])
                i1 = tosort[irec].index(rule[1])
                if i0>i1:
                    tosort[irec][i0] = rule[1]
                    tosort[irec][i1] = rule[0]

# For now correct tosort, get sum centers
for rec in tosort:
    print(rec,"is now correct.")
    ictr = int(len(rec)/2)
    result = result+rec[ictr]


# Print result
print("result = ",result)

    
                
