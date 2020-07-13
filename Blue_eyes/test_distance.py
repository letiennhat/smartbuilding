name = "unknow" 
import time
import pymysql

import cv2
frame = cv2.imread("Logo_dhbkdn.jpg")
begin_time = time.time()
database = pymysql.connect("localhost","be","blueeyes",autocommit=True)
try:
    if name.isdigit():
        letiennhat = open('hide_on_push/id.txt','w+')
        letiennhat.write(name)
        letiennhat.close()
    else:
        #letiennhat = open('hide_on_push/name_id.txt','w+')
        #letiennhat.write(splitname(name))
        #letiennhat.close()
        letiennhat = open('hide_on_push/id.txt','w+')
        letiennhat.write(name)
        letiennhat.close()
except:
    traceback.print_exc()
    if name != "Unknow":
        letiennhat = open('hide_on_push/name_id.txt','w+')
        letiennhat.write(splitname(name))
        letiennhat.close()
        letiennhat = open('hide_on_push/id.txt','w+')
        letiennhat.write(name)
        letiennhat.close()
try:
    LeTienNhat= open('hide_on_push/html3.html','w+')
    LeTienNhat.write('<meta http-equiv="refresh" content="2"><img src="scv/'+str(name)+'.jpg" alt="Anh dai dien" width="100%" height="100%">')
    LeTienNhat.close()
    letiennhat = open('best/ten.txt','w+')
    letiennhat.write("EVERYONE")
    letiennhat.close()
except:
    pass
name_linkfile = str(time.localtime(time.time()).tm_mon)+'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)
rutgon_=[]
if name != "Unknow":
    unknow_count=0
    name_file = 'regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt'
    open_file = open(name_file+'/'+name_linkfile+'.txt','a+')#create if not have
    open_file.close()
    
    open_file = open(name_file+'/'+name_linkfile+'.txt','r+')#thang_ngay_nam.txt
    #open_file1 = open(name_file+'/1.txt','a+') #check tinh thuong xuyen
    time_os = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'.txt','r+')
    hiendien_ten = list(time_os.read().split())
    if name in rutgon_:
        if name not in hiendien_ten:
            hiendien += 1
    
    if name not in list(open_file.read().split()):
        
        cursor = database.cursor()
        image_64 = 'sbuilding'+name+str(time.localtime(time.time()).tm_mday)+str(time.localtime(time.time()).tm_mon)+str(time.localtime(time.time()).tm_year)+str(time.localtime(time.time()).tm_hour)+'readbase'
        #image_64 = '../test_options/static/'+image_64+'.jpg'
        cv2.imwrite('../test_options/static/sbuilding/'+image_64+'.jpg',frame)
        # time.sleep(0.5)
        #time.sleep(2
        # image_base = open('status_sv/'+image_64+'.jpg', 'rb')
        
        # imread = image_base.read()
        # image_64 = base64.encodebytes(imread)

        # print(image_64)
        # print(type(image_64))
        #image_base.close()
        #try:
            # os.remove('status_sv/'+image_64+'.jpg')
        #except:
            #pass
        # test_base = open('test64.txt','w+')
        # test_base.write(image_64.decode('utf-8'))
        # test_base.close()

        # image_64=image_64.decode("utf-8")
        # print(type(image_64))

        cursor.execute("use mysqldb1")
        # cursor.execute("insert into b values({})".format(image_64))
        query = """insert into realtime_0 values(%s,%s,%s,%s,%s,%s)"""
        query_1 = """insert into realtime_0 select %s,%s,%s,%s,%s,%s,hovaten,donvi,ngaysinh,gioitinh,\
        chucvu,trinhdo,hocham from manager where maso = %s"""
        value_query = name,str(time.localtime(time.time()).tm_mday),str(time.localtime(time.time()).tm_mon),str(time.localtime(time.time()).tm_year),str(time.localtime(time.time()).tm_hour),image_64,name
        cursor.execute(query_1,value_query)
        database.commit()
        cursor.close()
        #database.close()
        bien_vang=1
        open_file.close()
        open_file = open(name_file+'/'+name_linkfile+'.txt','a+')#thang_ngay_nam.txt
        open_file.write('\n'+str(name))
        open_file.close()
elif name =="Unknow":
    unknow_count +=1
    if unknow_count >=10:
        unknow_count =0
        print("warning")
        image_64 = 'sbuilding'+name+str(time.localtime(time.time()).tm_mday)+str(time.localtime(time.time()).tm_mon)+str(time.localtime(time.time()).tm_year)+str(time.localtime(time.time()).tm_hour)+'readbase'
        
        cv2.imwrite('../test_options/static/sbuilding/'+image_64+'.jpg',frame)
        # time.sleep(0.5)
        #time.sleep(2
        #image_base = open('status_sv/'+image_64+'.jpg', 'rb')
        
        #imread = image_base.read()
        #image_64 = base64.encodebytes(imread)
        

        # print(image_64)
        # print(type(image_64))
        #image_base.close()
        #try:
            #os.remove('status_sv/'+image_64+'.jpg')
        #except:
            #pass
        
        try:
            #print(111)
            # database1 = pymysql.connect(host='localhost',
            #                         user='be',
            #                         password='blueeyes',
            #                         autocommit = True

            #                         )
            #print(222)
            cursor1 = database.cursor()
            #print(333)
            cursor1.execute("use mysqldb1")
            query_3="""insert into realtime_0(id,ngay,thang,nam,gio,url,hovaten,donvi,ngaysinh,gioitinh,chucvu,trinhdo,hocham) values(0,%s,%s,%s,%s,%s,'unknown','unknown',0,0,0,0,0)"""
            values_2 = str(time.localtime(time.time()).tm_mday),str(time.localtime(time.time()).tm_mon),str(time.localtime(time.time()).tm_year),str(time.localtime(time.time()).tm_hour),image_64
            cursor1.execute(query_3,values_2)
            database.commit()
            cursor1.close()
            # database1.close()
        except:
            pass

time_os = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'.txt','a+')
time_os.close()
time_os = open('regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+name_linkfile+'.txt','r+')
print("endtime == ", time.time()-begin_time)