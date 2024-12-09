f = open("input.txt","r")
#f = open("test.txt","r")

for rawline in f.readlines():
    diskmap = rawline.strip("\n")
f.close()

# Construct disk uncompressed
disk0 = []
ID = 0
swfile = True
for ch in diskmap:
    nbytes = int(ch)
    if swfile:
        for j in range(nbytes):
            disk0.append(str(ID))
        swfile = False
        ID = ID + 1

    else:
        for j in range(nbytes):
            disk0.append(".")
        swfile = True
        
# Show result
print("Read uncompressed disk.")
#print("".join(disk0))

# Start compressing
disk1 = disk0.copy()
i = 0
while i <len(disk1):
    # Check for empty space and fill it
    if disk1[i]==".":
        j = -1
        while len(disk1)>0 and disk1[j] == ".":
            del disk1[j]
        else:
            if i<len(disk1)-1:
               disk1[i] = disk1[j]
               del disk1[j]
    i = i+1

for k in range(len(disk1),len(disk0)):
    disk1.append(".")

print("\nCompressed disk.")
#print("".join(disk1))

# Calculate checksum
checksum = 0
for i,byte in enumerate(disk1):
    if byte==".":
        continue
    checksum = checksum + i*int(byte)

print("\nChecksum =",checksum)
    
            
            
        


    
