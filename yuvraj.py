# import pickle
# # Deleting a record based on roll no:
# def delete(roll):
#     f = open('student.dat', 'rb')
#     flag = False
#     d = []
#     while True:
#         try:
#             rec = pickle.load(f)
#             if rec['Rollno'] != roll:
#                 d = d + [rec]
#             if rec['Rollno'] == roll:
#                 flag = True
#                 continue
#             file = open('student.dat', 'wb')
#             for i in d:
#                 pickle.dump(i, file)
#             file.close()
#         except EOFError:
#             break
#
# # Updating a record based on Rollno
# def update():
#     roll = int(input('Enter roll number:'))
#     f = open('student.dat', 'rb')
#     flag = False
#     d = []
#     while True:
#         try:
#             rec = pickle.load(f)
#             if rec['Rollno'] == roll:
#                 name = input('Enter Updated Name: ')
#                 marks = int(input('Enter Updated Marks: '))
#                 dic = {'Rollno': roll, 'Name': name, 'Marks': marks}
#                 delete(roll)
#                 file1 = open('student.dat', 'ab')
#                 pickle.dump(dic,file1)
#                 file1.close()
#                 flag = True
#         except EOFError:
#             break
#         if flag == False:
#             print('No Records found')
#         f.close()
#
#
# # import pickle
# # #Accepting data for Dictionary
# # def insertRec():
# #     rollno = int(input('Enter roll number:'))
# #     name = input('Enter Name:')
# #     marks = int(input('Enter Marks'))
# #
# #     #Creating the dictionary
# #     rec = {'Rollno':rollno,'Name':name,'Marks':marks}
# #
# #     #Writing the Dictionary
# #     f = open('d:/student.dat','ab')
# #     pickle.dump(rec,f)
# #     f.close()
# # #Searching a record based on Rollno
# #
# # def searchRollNo(r):
# #     f = open('d:/student.dat','rb')
# #     flag = False
# #     while True:
# #         try:
# #             rec = pickle.load(f)
# #             if rec['Rollno'] == r:
# #                 print('Roll Num:',rec['Rollno'])
# #                 print('Name:',rec['Name'])
# #                 print('Marks:',rec['Marks'])
# #                 flag = True
# #         except EOFError:
# #             break
# #     if flag == False:
# #         print('No Records found')
# #     f.close()
# import pickle
#
# def inserting():
#     f = open('voters.dat', 'ab')
#     voter_no = input("Enter voter number")
#     voter_name = input("enter the name of the voter")
#     add = input("enter the address of the voter")
#     sal = input("enter the salary of the voter")
#     l = [voter_no, voter_name, add, sal]
#     pickle.dump(l, f)
#     f.close()
#
#
# def count_with_same_salary():
#     f = open('voters.dat', 'rb')
#     usr_input = input('Enter salary')
#     x = []
#     while True:
#
#         try:
#             l = (pickle.load(f))
#             print(l)
#             if l[3] == usr_input:
#                 x.append(l[1])
#         except EOFError:
#             break
#
#     print(len(x))
#
# inserting()
# count_with_same_salary()
#
#
#
#
#
#
#
#
# d1 ={}
# t = ((1,2,3),(5,6,7),(8,6,7))
# print(str(t).split(','))
#
# sprites = {'red1': 'red1.globalPosition', 'red2':122}
# sprites.fromkeys()
# 0
# #
#
#
# d = []
# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# for i in range(len(color_name)):
#     d.append({'color_name': color_name[i], 'color_code':color_code[i]})
# print(d)

# color_dict = [i for i in {'colorname:': for i in color_code}]
# print(color_dict)

# Color1 = ["red", "orange", "green", "blue", "white"]
# Color2 = ["black", "yellow", "green", "blue"]
# common = []
# for i in Color1:
#     for j in Color2:
#         if i ==j:
#             common.append(i)
# for i in common:
#     Color1.remove(i)
# print(Color1)
# #
# Color1 = ["red", "orange", "green", "blue", "white"]
# Color2 = ["black", "yellow", "green", "blue"]
#
# common = []
# for i in Color1:
#     if i in Color2:
#         Color2.remove(i)
# print(Color2)


# for i in Color2:
#     for j in Color1:
#         if i == j:
#             common.append(i)
# for i in common:
#     Color2.remove(i)
# print(Color2)
#
#
# # print(set(Color1)-set(Color2))
# # print(set(Color2)-set(Color1))
# print(sorted([3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1], reverse=True))
#
# while 0 in []:
#     [].remove(0)
#
#
# l = {}
# for i in range(3):
#     x = input(f"Enter the element no. {i}")
#     l[len(str(x))] = x
#
# for i in sorted(l):
#     print(l[i])
# x = 12
# l = 0
# for i in range(10):
#     x = input(r"c\192\")





import selenium
print('gamers')


