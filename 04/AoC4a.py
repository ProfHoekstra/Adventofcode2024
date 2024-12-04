def sign(ix):
    if ix==0: return 0
    return int(round(abs(ix)/ix,0))

def searchtab(tab,key,diry,dirx):
    """search key in tab with direction -1 0 or +1 for x,y"""
    nkey = 0
    MY = len(table)
    MX = len(table[0])
    L = len(key)
    xlim = [(0,MX),(0,MX-L+1),(L-1,MX)]
    ylim = [(0,MY),(0,MY-L+1),(L-1,MY)]        
    xmin,xmax = xlim[dirx]
    ymin,ymax = ylim[diry] 
    for y0 in range(ymin,ymax):
        for x0 in range(xmin,xmax):
            txt = ""
            for i in range(L):
                iy=y0+i*diry
                ix=x0+i*dirx
                #print(y0,x0,i,iy,ix)
                txt = txt + tab[iy][ix]
            #print()
            if txt==key:
                nkey = nkey+1
    return nkey


testdata = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")
test = []
for line in testdata:
    test.append(list(line))


# Read data
table = []
f = open("input.txt","r")
for line in f.readlines():
    row = list(line.strip())
    table.append(row)
f.close()

#table=test

key = "XMAS"
directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

ncount = 0
for d in directions:
    n = searchtab(table,key,d[0],d[1])
    print(d,":",n)
    ncount = ncount + n

# Print result
print(key,"was found",ncount,"times.")
