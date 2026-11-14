x = input("camelCase:")
result = ""
for i in x :
    if(i.isupper()):
        result += "_"+i.lower()
    else:
        result += i
print(result)

