x = input("File name:")
x = x.lower().strip(" ")

if(x.find(".gif") != -1 and x.endswith(".gif")):
    print("image/gif")
elif (x.find(".jpg")!= -1 and x.endswith(".jpg")):
    print("image/jpeg")
elif (x.find(".jpeg")!= -1 and x.endswith(".jpeg")):
    print("image/jpeg")
elif (x.find(".png")!= -1 and x.endswith(".png")):
    print("image/png")
elif (x.find(".txt")!= -1 and x.endswith(".txt")):
    print("text/plain")
elif (x.find(".zip")!= -1 and x.endswith(".zip")):
    print("application/zip")
elif (x.find(".pdf")!= -1 and x.endswith(".pdf")):
    print("application/pdf")
else :
    print("application/octet-stream")
