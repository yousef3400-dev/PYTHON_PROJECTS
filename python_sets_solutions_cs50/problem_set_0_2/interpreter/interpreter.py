x = input("Expression:")
x = x.strip(" ")
z = x.split(" ")
z[0] = float(z[0])
z[2] = float(z[2])
if(z[1] == "+"):
    print(f"{z[0]+z[2]:.1f}")

elif(z[1]=="-"):
    print(f"{(z[0]-z[2]):.1f}")

elif(z[1]=="*"):
    print(f"{(z[0]*z[2]):.1f}")

elif(z[1]=="/"):
    print(f"{(z[0]/z[2]):.1f}")
