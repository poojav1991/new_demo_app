##
#from utilities import excelutils
from utilities import excelutils


class adduserdata:
    test_adduserdata = [{"firmname": "Mittal Sales",
                         "ownername": "Mittal Patel",
                         "mobileno": "4747441414",
                         "setting_search_add": "maninagar",
                         "city": "Ahmedabad", "status": "In-Active"}
                        ]

    @staticmethod
    def get_user_data():
        # workbook = openpyxl.load_workbook("/home/atpl/Pooja/PycharmProjects/PythonSelfFramework/exceldata/userdata.xlsx")
        file = "/home/atpl/Pooja/PycharmProjects/New_koil_demo/exceldata/userdata.xlsx"

        rows = excelutils.get_row_count(file, "usercreate")
        columns = excelutils.get_column_count(file, "usercreate")
        first_row = []  # The row where we stock the name of the column
        for col in range(1, columns + 1):
            first_row.append(excelutils.get_read_data(file, "usercreate", 1, col))
        data = []
        for row in range(2, rows + 1):
            elm = {}
            for col in range(1, columns + 1):
                elm[first_row[col - 1]] = excelutils.get_read_data(file, "usercreate", row, col)
            data.append(elm)
        return data

    """ @staticmethod
          def get_user_data(test_case_name):
                  #print("1")
                  Dic = {}
                  book = openpyxl.load_workbook("/home/atpl/Documents/pythondemo.xlsx")
                 # print("2")
                  sheet = book.active
                 # print("3")
                  for i in range(1, sheet.max_row + 1):  # this statement is getting all rows
                          if sheet.cell(row=i, column=1).value == test_case_name:
                                  for j in range(2, sheet.max_column + 1):  # This statement is getting all columns
                                          Dic[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value

                  return [Dic]
                  #print(Dic)

  """
