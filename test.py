# # #use of readline
# # myfile = open("demo.txt", "r")
# # myline = myfile.readline()
# # print(myline)
# # print(type(myline))
# # myfile.close()
# #
# # #use of readline
# # myfile = open("demo.txt", "r")
# # myline = myfile.readline()
# # print(myline)
# # print(type(myline))
# # myfile.close()
# # Ritu Arora9:44 AM
# # myfile = open("demo.txt", "r")
# # print(myfile)
# # print(type(myfile))
# # for line in myfile:
# #     print(line)
# #     print(type(line))
# # myfile.close()
# # Ritu Arora9:53 AM
# # #reading specific number of characters
# # myfile = open("demo.txt", "r")
# # myline = myfile.readline(10)
# # print(myline)
# # print(type(myline))
# # myfile.close()
# # #readline with loop
# # myfile = open("demo.txt", "r")
# # myline = myfile.readline()
# # while myline:
# #     print(myline)
# #     myline = myfile.readline()
# # myfile.close()
# # #read all the lines from the file
# # myfile = open("demo.txt", "r")
# # mylist = myfile.readlines()
# # print(type(mylist))
# # print(mylist)
# # myfile.close()
# # #read one line at a time using while loop
# # myfile = open("demo.txt", "r")
# # while myfile:
# #     line  = myfile.readline()
# #     print(line)
# #     if line == "":
# #         break
# # myfile.close()
# #
# #
# #
# #
# #
#
#
#
#
#
#
#
#
#
#
#
# #
# #
# # f = open("test.txt",'r')
# # y=f.read(4)
# # print(y)
# # print(type(y))
#
#
#
# f = open("a.txt", 'w')
# line = 'Welcome to python.mykvs.in\n Regularly visit python.mykvs.in'
# f.write(line)
# f.close()
# f = open("a.txt", 'r+b')
# print(f.read())
#
# print(f.tell())
# print(f.read(29)) # read seven characters
# f.seek(20,1)
# print(f.tell())
# print(f.read())
# print(f.tell())
# f.seek(10, 0) # moves to 9 position from begining
# print(f.read(5))
# f.seek(-4,1) # moves to 4 position from current location
# print(f.read(8))
# f.seek(-5, 2) # Go to the 5th byte before the end
# print(f.read(4))
# f.close()
# f = open("numbers.txt","w")
# f.write("ABCDEFGHIJ jdhjfhfjfvh ")
# f.close()
# f = open("numbers.txt","rb")
# print("Location of file pointer after opening the file:",f.tell())
# f.seek(1)
# x=f.read()
# print(x)
# print("Location of file pointer after reading the whole file:", f.tell())
# f.seek(8)
# print("Location of file pointer after five bytes from beginning:", f.tell())
# f.seek(2,1)
# print("Location of file pointer after two bytes from current location:", f.tell())
# f.seek(-2,2)
# print(f.read())


#
# import math
# # print(math.factorial(5))
# s = 0
# r = 0
# t = '342'
# for i in t:
#     s += math.factorial(int(i))
#
# while s:
#     r, s = r + s % 10, s // 10
# print(r)
# [
#     1,2
# ].index()
#
import numpy as np
n = "2556786876869686996869686"
f = []
x = [a for a in n]
# print(x)
for i in range(len(x) + 1):
    for j in range(i):
        f.append(int("".join(x[j: i])))
print(f)
print(sum(f))
# r = 0
# s = 123
# while s:
#     r, s = r + s % 10, s // 10
# print(r)
# return sum(f)

# import itertools
# l = [1,2,3]
# print(list(itertools.permutations(l,3)))
