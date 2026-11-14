coca_calc = 50
while(coca_calc > 0):
    print("Amount Due: "+str(coca_calc))
    x = int(input("Insert Coin:"))
    if(x == 5 or x == 10 or x == 25):
        coca_calc -= x

print("Change Owed: "+str(abs(coca_calc)))



