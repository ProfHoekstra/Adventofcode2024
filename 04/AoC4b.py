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
tab = []
f = open("input.txt","r")
for line in f.readlines():
    row = list(line.strip())
    tab.append(row)
f.close()

#tab=test

key = "MAS"

MY = len(tab)
MX= len(tab[0])
ncount = 0

for ix in range(1,MX-1):
    for iy in range(1,MY-1):
        word1 = tab[iy-1][ix-1]+tab[iy][ix]+tab[iy+1][ix+1]
        word2 = tab[iy-1][ix+1]+tab[iy][ix]+tab[iy+1][ix-1]
        if (word1==key or word1==key[::-1]) and \
           (word2==key or word2==key[::-1]):
            ncount = ncount+1
        
print(key,"was found",ncount,"times.")
