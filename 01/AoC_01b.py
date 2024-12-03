import numpy as np
"""
his time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3
For these example lists, here is the process of finding the similarity score:

The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
The fourth number, 1, also does not appear in the right list.
The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
The last number, 3, appears in the right list three times; the similarity score again increases by 9.
"""
# Lists with numbers
lst1 = []
lst2 = []

# Fill lists each with a column of numbers from data file
f = open("data.txt","r")
for line in f.readlines():
    recs = line.strip().split()
    lst1.append(int(recs[0].strip()))
    lst2.append(int(recs[1].strip()))
f.close()

# Similarity score
score = 0
for x in lst1:
    score = score + x*lst2.count(x)

print("Similarity score = ",score)


                
