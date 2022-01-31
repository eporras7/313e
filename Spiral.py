#  File: Spiral.py

#  Description:

#  Student Name: Nicholas Webb

#  Student UT EID: nw6887   

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 1/29/2022

#  Date Last Modified:

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

def create_spiral(n):
    if n % 2 == 0:
        n = n + 1

    x = n/2 #spiral starting positions
    y = n/2

    filler = 1 #This is the number we're going to start with!
    
    p1 = []  #this initializes the 2-d array
    for i in range(n):
        p2 = []
        for j in range(n):
            p2.append(0)
        p1.append(p2)

    p1[x][y] = filler #Fill the first num in the center
    filler += 1 #We increment this number as we traverse the spiral

    for i in range(1, n):
        if i % 2 != 0:
            for j in range(i): #since the spiral expands outward, we go by the increasing range of i
                y+=1
                p1[x][y] = filler
                filler+=1
            for j in range(i):
                x+=1
                p1[x][y] = filler
                filler += 1
        else:
            for j in range(i):
                y -=1
                p1[x][y] = filler
                filler += 1
            for j in range(i):
                x-=1
                p1[x][y] = filler
                filler += 1
    for i in range(1,n):
        p1[0][i] = p1[0][0] + i
    
    #return p1
    print(p1)

    
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    total_list = []

    x = 0
    y = 0

    for i in range(len(spiral)): #this sets location of n
        for j in range(len(spiral[0])):
            if spiral[i][j] == n:
                x = i
                y = j

    if x-1
    





def main():
    
    n = int(input("Enter a dimension: "))
    create_spiral(n)


# read the input file
    input_file = open("spiral.in", "r")
    line = input_file.readline()
    

# create the spiral
    spiral = create_spiral(line)


# add the adjacent numbers

# print the result

if __name__ == "__main__":
    main()