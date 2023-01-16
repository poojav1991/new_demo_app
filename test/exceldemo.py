import openpyxl

from utilities import excelutils

file="/home/atpl/Pooja/PycharmProjects/PythonSelfFramework/exceldata/userdata.xlsx"

rows =excelutils.get_row_count(file,"usercreate")
columns = excelutils.get_column_count(file, "usercreate")
first_row = []  # The row where we stock the name of the column
for col in range(1, columns + 1):
    first_row.append(excelutils.get_read_data(file,"usercreate",1,col))
data = []
for row in range(2, rows + 1):
    elm = {}
    for col in range(1, columns + 1):
        elm[first_row[col - 1]] = excelutils.get_read_data(file,"usercreate",row,col)
        data.append(elm)
print(data)
