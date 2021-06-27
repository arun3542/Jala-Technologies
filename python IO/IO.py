# 1.Write a program to read text from .txt file using InputStream

with open('arun.txt','r') as file:
    print(file.read())


print('--2')

# 2.Write a program to write text to .txt file using OutputStream

with open('arun.txt','w') as file:
    file.write('Hii hello everyone welcome to my world')

print('--3')

# 3.Write a program to read data from excel

import openpyxl
my_wb = openpyxl.Workbook()
my_sheet = my_wb.active
my_sheet_title = my_sheet.title
print("My sheet title: " + my_sheet_title)

print('--4')

# 4.Write a program to write data to excel

import xlsxwriter

book = xlsxwriter.Book('Example2.xlsx')
sheet = book.add_sheet()

# Rows and columns are zero indexed.
row = 0
column = 0

content = ["Parker", "Smith", "John"]

# iterating through the content list
for item in content:
    # write operation perform
    sheet.write(row, column, item)

    # incrementing the value of row by one with each iterations.
    row += 1

book.close()