import pyexcel as pe

file_name = "test.ods"

sheet = pe.get_book(file_name=file_name)
print(sheet)



