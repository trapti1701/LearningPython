# # File Io basics
# """
# "r" - open file for reading - defualt mode
# "w" - open file for writing
# "x" - exclusive creation - creates file if not exists
# "a" - append - add more content to a file
# "t" - text more - default mode
# "b" - binary mode
# "r+" - read and write
# """
#
# # to open a file and read the content of the file
#
# f= open("while loop.py")
# # content = f.read()
# # print(f.read())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readlines())
#
# f= open('file name', 'w') # to open the file in write mode
# f.write("whatever you want to write in above file, existing content of the file will be replaced with this")
#
# f= open('file name', 'a') # to open the file in append mode
# f.write("whatever you want to add in this file ")
# #this will keep adding the statement as many times as we run the program
# f.close()
#
# pritnt(f.tell())           #to know where the file handle is, at which character
# print(f.seek(0))             #to bring the file handle at initial stage again
# #Video number 31 of Harry

with open ('while loop.py') as f:
#to open a file using block, in this we need not to close the file

    print(f.readlines())


