f = open("sathish.txt")


# To find file pointer
print(f.tell())  # 0
print(f.readline())
print(f.tell())  # 15

# To control the file pointer
print(f.seek(0))
print("Second Time", f.readline())


# Return file name
print(f.name)


f.close()
