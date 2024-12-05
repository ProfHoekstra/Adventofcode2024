#f = open("test.txt","r")

f = open("input.txt","r")


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
for rec in recs:
    correct = True
    for rule in rules:
        if rule[0] in rec and rule[1] in rec:
            i0 = rec.index(rule[0])
            i1 = rec.index(rule[1])
            if i0>i1:
                correct = False
                print(rec,"breaks",rule)
                break
                
    # Correct? Multiply
    if correct:
        print(rec,"is correct.")
        ictr = int(len(rec)/2)
        result = result+rec[ictr]
        print(result,rec[ictr])
#    else:
#        print(rec,"is not correct.")
        

# Print result
print("result = ",result)

    
                
