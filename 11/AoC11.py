"""
If the stone is engraved with the number 0, it is replaced by a stone
engraved with the number 1.
If the stone is engraved with a number that has an even number of digits,
it is replaced by two stones. The left half of the digits are engraved on
the new left stone, and the right half of the digits are engraved on the new
right stone. (The new numbers don't keep extra leading zeroes: 1000 would
become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone;
the old stone's number multiplied by 2024 is engraved on the new stone.
"""
from copy import deepcopy

# To avoid runtime and memory problems, use a frequency table
# i.s.o the actual row of stones
# So stonedict[a]=n means: value a occurs n times in row

# Add N to valeu for key in keydict, to update frequency table
def addtodict(key,keydict,N=1):
    if key in keydict:
        keydict[key]+=N
    else:
        keydict[key] = N 

#line = "125 17"
Nblinks = 75
line = "41078 18 7 0 4785508 535256 8154 447"
stonedict = {}
for txt in line.split():
    stone = int(txt)
    addtodict(stone,stonedict)
    
print("Start dict:",stonedict)
input("Press enter to start")

for blink in range(Nblinks):

    newstones = {}
    total = 0
    for stone in stonedict:
        N = stonedict[stone]
        if stone==0:
            addtodict(1,newstones,N)
            total = total+1
        elif len(str(stone))%2==0:
            L = len(str(stone))
            n1 = int(str(stone)[:int(L/2)])
            n2txt = str(stone)[int(L/2):]
            # remove leading zeroes
            while len(n2txt)>1 and str(n2txt)[0]=="0":
                n2txt = n2txt[1:]
            n2 = int(n2txt)
            addtodict(n1,newstones,N)
            addtodict(n2,newstones,N)
            total = total+2*N
        else:
            addtodict(2024*stone,newstones,N)
            total = total+N
            
    stonedict = deepcopy(newstones)

    if (blink+1)%5==0:
        print(blink+1,":",total)
    
    #print(blink+1,stones)
    #input(" ")

print(Nblinks,":",sum(stonedict.values())
)
