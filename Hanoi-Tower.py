"""
@author : unnumsykar
Recursive program to generate the sequence of moves to solve Tower of Hanoi problem for any number of disks
"""

"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 
1) Only one disk can be moved at a time. 
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack. 
3) No disk may be placed on top of a smaller disk.
"""
def HanoiTower(n,source,aux,dest):
    if n==1:
        print(f"Move disk from {source} to {dest}")
   
    else:
        HanoiTower(n-1,source,dest,aux)
        print(f"Move disk from {source} to {dest}")
        HanoiTower(n-1,aux,source,dest)

n = 5
HanoiTower(5,'X','Y''Z')   # X,Y,Z are name of rods
