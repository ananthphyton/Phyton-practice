#Print first 50 fibonacci numbers,using FOR LOOP or WHILE LOOP and with IF/ELSE
cntr=0
for i in range(1,51):
    if i == 1 or i == 2:
        print(i)
        cntr=cntr+1
        print("cntr:", end="")
        print(cntr)
    elif cntr <= 50:
        j=(i-1)+(i-2)
        print(j)
        cntr = cntr+1
        print("cntr:", end="")
        print(cntr)




