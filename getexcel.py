import xlrd
#import xlwt
#from xlrd import open_workbook
exlpath =r"C:\Users\Administrator\Desktop\testcase.xls"
print(exlpath)
xlBook = xlrd.open_workbook(exlpath)
exltable = xlBook.sheets()[0]
print(exltable)
exlrow =exltable.nrows
exlcol =exltable.ncols
print(exlrow)
print(exlcol)
#print(exltable.cell_value(7,2))

for i in range(1,exlrow):
    for j in range(i,exlcol):
        print(f"这是第 {i} 行{j}列")
