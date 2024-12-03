"""
or example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding
up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
"""

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

f = open("input.txt","r")
data = f.read() # String with a;l
f.close()

# Test option
#data=test
#print(test)

#Set reading modes for mul(a,b)
# Modes: Search for keys "mul(" , a , "," ,b ,")" consecutively
getmul = 0
geta = 1
getb = 2
getclose = 4
# Minimum length of keys
minlen = [4,1,1,1]


# Start of with searhc for mul(
mode = getmul
i = 0  # cursor location in data
result = 0 # sum of multiplications
buffer = "" # buffer for numbers
a = 0
b = 0

# Go through data
while i<len(data)-minlen[mode]:

    #debug
    #print(data[i],mode)
    #input("")

    # Check syntax
    error = False
    if mode==getmul:
        if data[i:i+4].lower()=="mul(":
            mode = mode+1 # Go to next mode
            buffer = "" # empty buffer
            i=i+3 # Skip 3 extra chars

    elif mode == geta:
        if data[i]=="-" and len(buffer)==0:
            buffer = "-"
        elif data[i].isdigit():
            buffer = buffer + data[i]
        elif data[i]==",":
            a = int(buffer)
            mode = mode+1
            buffer = ""

        elif data[i]==".":
            print("Floats?  i=",i," buffer is",buffer,"next",data[:i+5])
            input("")
        else:
            error = True
            mode = getmul
            buffer = ""
            a = 0
            b = 0

    # Read digit b till ")"
    elif mode == getb:
        if data[i]=="-" and len(buffer)==0:
            buffer = "-"
        elif data[i].isdigit():
            buffer = buffer + data[i]
            
        elif data[i]==")":
            b = int(buffer)
            result = result + a*b
            buffer = ""
            mode = getmul

        elif data[i]==".":
            print("Floats?  i=",i," buffer is",buffer,"next",data[:i+5])
            input("")
        else:
            error = True
            mode = getmul
            buffer = ""
            a = 0
            b = 0
 
    # Next character/byte
    i = i+1
            
            
print("Sum of mul is",result)      
    
