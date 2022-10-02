try:
    filedata=open("random.txt")
    print(filedata.read())
except FileNotFoundError:
    filedata=open("random.txt","w")
    filedata.write("this is new fiel")
    print("new file created")
else:
    print("file read successfully")
finally:
    filedata.close()

