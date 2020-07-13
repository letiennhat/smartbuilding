import xlrd
import datetime, xlrd
#import read_gmail
import email
import imaplib
import ctypes
import getpass
import credentials
import sys
import threading
import pymysql
book = xlrd.open_workbook("CSDL-CBVC-DHBK.xlsx")
sys.setrecursionlimit(10000)
sh = book.sheet_by_index(0)

#read_gmail.main()
#val = '162362 '
def round_certification(cer):
	cer = str(cer)
	if len(cer)<3:
		return cer
	if "+" in cer:
		a=[]
		for i in cer.split("+ "):
			a.append(i)
		return round_certification(a[0])+" & "+ round_certification(a[1]) 
	cer_1 = cer.split(" ")
	

	# print(cer_1)
	a =""
	for i in cer_1:
		if i.upper()==i:
			a+=i
		else:
			a+=i[0].upper()
	# print(a)
	return a
# print(round_certification("Thạc sỹ "))
# def round_names (name):
	# if name <
# print(round_certification('Trưởng Phòng + Chủ tịch Công đoàn Trường'))
# exit()
def loop():
	while 1 :
		try:
			open_id = open('id.txt','r+')
			val = open_id.readline()
			open_id.close()
			#print(int(val))
			val = val.split("\n")[0]
			database = pymysql.connect('localhost','root','letiennhat')
			cursor = database.cursor()
			cursor.execute("use mysqldb1")
			if val.isdigit():
				cursor.execute("select hovaten,donvi,chucvu,trinhdo,hocham from manager where maso={}".format(val))
				data = cursor.fetchall()
				hovaten, donvi, chucvu, trinhdo, hocham = data[0]
				if trinhdo == "Đại học ":
					a = " "
				elif trinhdo == "Thạc sỹ ":
					# print(1)
					a = "ThS "
				else:
					a = " " + round_certification(trinhdo) + " "
				names = round_certification(hocham) + a + hovaten
				# if len(chucdanh)<3:
				# 	chucdanh=" "
				# names = sh.row_values(i)[4]
				print(names)
				# chucdanh = open("chucdanh.txt","w+")
				# chucdanh.write(str(chucdanh))
				# chucdanh.close()
				# chucvu =open('chucvu.txt','w+')
				# chucvu.write(str(sh.row_values(i)[10]))
				# chucvu.close()
				name_on = open('nameonly.txt', 'w+')
				name_on.write(hovaten)
				name_on.close()
				name1 = open('name_id.txt', 'r+')
				check_name = name1.readline()
				name1.close()
				if check_name == names:
					pass
				else:
					name = open('name_id.txt', 'w+')
					name.write(str(names))
					name.close()
				ndonvi = open("donvi.txt", "r+")
				check_donvi = ndonvi.readline()
				ndonvi.close()
				x = round_certification(chucvu)
				if len(x) < 2:
					x = ""
				else:
					x += ", "
				if check_donvi == (x + donvi):
					pass
				else:
					names_1 = open('donvi.txt', 'w+')
				names_1.write(x + donvi)
				names_1.close()
			else:
				pass
		except:
			pass
		'''
		for i in range(10,sh.nrows):
			try:
			    if round(int(sh.cell_value(i,1)))==int(val):
			    	if sh.row_values(i)[11] == "Đại học " :
			    		a = " "
			    	elif sh.row_values(i)[11] == "Thạc sỹ ":
			    		# print(1)
			    		a = "ThS "
			    	else:
			    		a = " "+round_certification(str(sh.row_values(i)[11]))+" "
			    	names = round_certification(str(sh.row_values(i)[12])) + a + sh.row_values(i)[4]
			    	# if len(chucdanh)<3:
			    	# 	chucdanh=" "
			    	# names = sh.row_values(i)[4]
			    	print(names)
			    	# chucdanh = open("chucdanh.txt","w+")
			    	# chucdanh.write(str(chucdanh))
			    	# chucdanh.close()
			    	# chucvu =open('chucvu.txt','w+')
			    	# chucvu.write(str(sh.row_values(i)[10]))
			    	# chucvu.close()
			    	name_on = open('nameonly.txt','w+')
			    	name_on.write(str(sh.row_values(i)[4]))
			    	name_on.close()
			    	name1 = open('name_id.txt','r+')
			    	check_name = name1.readline()
			    	name1.close()
			    	if check_name == names:
			    		pass
			    	else:
			    		name = open('name_id.txt','w+')
			    		name.write(str(names))
			    		name.close()
			    	ndonvi = open("donvi.txt","r+")
			    	check_donvi = ndonvi.readline()
			    	ndonvi.close()
			    	x = round_certification(str(sh.row_values(i)[10]))
			    	if len(x)<2:
			    		x=""
			    	else:
			    		x+=", "
			    	if check_donvi == (x+str(sh.row_values(i)[8])):
			    		pass
			    	else:
			    		names_1 = open('donvi.txt','w+')
			    	names_1.write( x+ str(sh.row_values(i)[8]))
			    	names_1.close()
					#time.sleep(3)
			except:
				print("loi")
				pass
		
				# break
		# name_1 = open('name_id.txt','w+')
		# name_1.write("Welcome")
		# name_1.close()
		# donvi_ = open('donvi.txt','w+')
		# donvi_.write("DUTER")
		# donvi_.close()'
			'''
loop()
	    

# def main():
# 	threading.Thread(target = loop).start()
# main()

	


