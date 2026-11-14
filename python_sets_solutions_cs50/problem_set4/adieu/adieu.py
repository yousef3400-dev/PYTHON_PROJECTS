res = []
while(True):
    try:
        x = input("Name: ")
        x = x.strip(" ")
        res.append(x)
    except EOFError:
        break
str ="Adieu, adieu, "
count = len(res)
if(count == 1):
    print("\nAdieu, adieu, to "+res[0])
elif(count == 2):
    print("\nAdieu, adieu, to "+res[0]+" and "+res[1])
else :
    for x in range(count):
        if(x == count-1):
            str += ("and "+res[x])
        else:
            if(x == 0):
                str += ("to "+res[x]+", ")
            else:
                str += (res[x]+", ")
    print("\n",end="")
    print(str)
