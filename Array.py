#Working with array

import array as arr
vals = arr.array('i',[1,3,4,5])
for i in range(4):
    print(vals[i])

#Getting values from the user to the array

import array as arr
inarr =arr.array('i',[])
lenarr=int(input("Enter length of the array:"))
for e in range(lenarr):
    x=int(input("Enter value to the array:"))
    inarr.append(x)
print(inarr)


#search the value of the array
srchval = int(input("Enter the value of the array to search:"))
k=0
for i in range(len(inarr)):
    j=i+1
    if inarr[i]==srchval:
        print("Value exists in array")
        k=1
        print(inarr[i])
        break
    elif (j==len(inarr) and k==0):
        print("Value not exists in array")








