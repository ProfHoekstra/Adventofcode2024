f = open("input.txt","r")
#f = open("test.txt","r")

def express(map):
    txt = ""
    for record in map:
        ID = record[0]
        if ID==-1:
            ch = "."
        else:
            ch = str(ID)
        n = record[1]
        for i in range(n):
            txt= txt+ch
    return txt

for rawline in f.readlines():
    diskmapline = rawline.strip("\n")
f.close()
#print("input = ",diskmapline)

# Construct disk uncompressed
disk0 = []
ID = 0
swfile = True
diskmap =[]
for ch in diskmapline:
    nbytes = int(ch)
    if swfile:
        diskmap.append((ID,nbytes))
        swfile = False
        ID = ID + 1
    else:
        diskmap.append((-1,nbytes))
        swfile = True
# Show result
#print("Uncompressed disk:")
#print(diskmap)
#print(express(diskmap))

# Start compressing method 2
# Files from back (right to left)
print("Compressing disk....")
i = len(diskmap)
ID = 9999
while i>0:
    i = i-1
    ID,nbytes = diskmap[i]
    if ID>=0:
        if ID%100==0:
            print(ID)
        #print(ID,":",express(diskmap))

        # Try to find a space
        placed = False
        for j,spaceblock in enumerate(diskmap):
            IDspace,nspace = spaceblock
            if IDspace>=0: # is no space
                continue
            else:
                if nspace==nbytes and j<i:
                    diskmap[i]=(IDspace,nbytes) # remove file
                    diskmap[j]=(ID,nbytes) # put it in record with spaces
                    placed = True
                elif nspace>nbytes and j<i: 
                    diskmap[i]=(IDspace,nbytes)# remove file
                    rest = nspace-nbytes   # Keep rest as spaces
                    diskmap[j]= (-1,rest)
                    diskmap.insert(j,(ID,nbytes)) # Insert a file block
                    i = i+1
                    placed = True
            if placed:
                break
        #Housekeeping: concatenate spaces
        for k in range(len(diskmap)-1):
            if diskmap[k][0]==-1 and diskmap[k+1][1]==-1:
                # Concatenate free space into one record
                diskmap[k][1]= diskmap[k][1]+diskmap[k+1][1]
                diskmap[k+1][1]= 0 #Stub
                

                



# Show result
#print("Compressed disk:")
#print(diskmap)
#disk = express(diskmap)
#print(disk)

# Calculate checksum
idx = 0
checksum = 0
for rec in diskmap:
    ID,nbytes = rec
    for i in range(nbytes):
        if ID>0:
            checksum = checksum+idx*ID
        idx = idx+1
                                   
print("Checksum =",checksum) 
            
            
        


    
