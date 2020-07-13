import xlrd
import datetime, xlrd
import read-gmail
book = xlrd.open_workbook("CSDL-CBVC-DHBK.xlsx")
sh = book.sheet_by_index(0)

while 1:
	for i in range(3,sh.ncols):
	    a1 = sh.cell_value(18, i)
	    if len(str(a1)) >10:
	        try:
	            a1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(a1, book.datemode))
	            print ('datetime:',str(a1_as_datetime)[0:10])
	        except:
	            pass
	    elif len(str(a1)) == 0:
	        print("ko co gi ")
	    else:
	        try:
	            print(sh.cell_value(18, i))
	        except:
	            pass

#location = ("TEST_.xlsx")

#workbook = xlrd.open_workbook(location)
#sheet = workbook.sheet_by_index(0)

#for i in range(3,sheet.ncols):
    #if ( sheet.cell_value(11, i) ) == "
    #print(sheet.cell_value(11, i))
