#learned today about getting input from user, sys module and writing a small program.
#Assignment was to find the cube value of the number by taking input from user. Below is the code for finding cube value.
import sys,math as m
a = int(sys.argv[1])**3
b = m.pow(int(sys.argv[1]),3)
print(a,b)
