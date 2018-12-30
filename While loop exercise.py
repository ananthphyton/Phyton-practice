#while loop quiz question from telusuko.
#Question print all numbers from 1 to 100 except which are divisable by 3 or 5.
i = 1
while i <= 100:
    if (i%3!=0) and (i%5!=0):
        print(i)
    i = i +1
    
#print # 5 times in each line in 4 lines.
j=1
while j <= 4:
    print("#",end="")
    k=1
    while k<=4:
        print("#",end="")
        k=k+1
    j= j+1
    print()


