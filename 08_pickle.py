# importing pickle
import pickle

"""only working in sequence object
"""
cars = ["audi", "benz", "BMW"]
file = "mycars.py"
fileObj = open(file, "wb")
pickle.dump(cars, fileObj)
fileObj.close()
# file = "mycars.pkl"
# fileObj = open(file, "rb")
# print(pickle.load(fileObj))

# picklemodule = dir(pickle)
# file1 = "picklemodule.pkl"
# fileObj1 = open(file1, "wb")
# pickle.dump(picklemodule, fileObj1)
# fileObj1.close()
# file1 = "picklemodule.pkl"
# fileObj1 = open(file1, "rb")
# print(pickle.load(fileObj1))