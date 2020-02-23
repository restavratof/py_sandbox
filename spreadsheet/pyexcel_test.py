import pyexcel as pe

file_name = "test.ods"

sheet = pe.get_book(fileName=file_name)
print(sheet)



