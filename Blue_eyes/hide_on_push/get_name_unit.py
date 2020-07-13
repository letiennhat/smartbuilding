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
import queue
import pymysql as my
import time
import json
from PIL import Image  
book = xlrd.open_workbook("CSDL-CBVC-DHBK.xlsx")
sys.setrecursionlimit(10000)
sh = book.sheet_by_index(0)
database = my.connect('localhost','be','blueeyes',db="mysqldb1",autocommit=True)
def round_certification(cer):
	if len(cer)<3:
		return cer
	if "+" in cer:
		a=[]
		for i in cer.split("+ "):
			a.append(i)
		return round_certification(a[0])+" & "+ round_certification(a[1]) 
	cer_1 = cer.split(" ")
	


	a =""
	for i in cer_1:
		if i.upper()==i:
			a+=i
		else:
			a+=i[0].upper()

	return a

def loop():
    global database
    check_query = queue.Queue(maxsize=0)
    val_check = queue.Queue(maxsize=0)
    while 1 :
        # print(1)
        try:
            # with open('emotion_values.txt','r+') as f:
            #     emotion_text = f.read()
            # if emotion_text == "happy":
            #     noframe = Image.open(r'/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/UI/static/convert/happy.png')
            #     noframe = noframe.save('/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/UI/static/status/emotions.png')
            # elif emotion_text == "neutral":
            #     noframe = Image.open(r'/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/UI/static/convert/neutral.png')
            #     noframe = noframe.save('/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/UI/static/status/emotions.png') 
            cursor = database.cursor()
            # print(cursor)
            open_id = open('id.txt','r+')
            
            
            val1 = open_id.readline()
            if val_check == val1:
                key_check = 1
            val_check = val1
            print(val1)
            if not val1:
                pass
                
            else:
                val2=json.loads(val1)
                #print(1111)
                #print(val1)
                val = val2['id']
                if val == "unknown":
                    val = str(0)
                else:
                    pass
                time1 = (val2['time'])
                evidence_path = val2['evident_path']
                '''
                    Time stamp - > date
                '''
                emotion_text = val2['emotion']
                day = time.localtime(time1).tm_mday
                mon = time.localtime(time1).tm_mon
                years = time.localtime(time1).tm_year
                hour = time.localtime(time1).tm_hour
                mins = time.localtime(time1).tm_min
                seconds = time.localtime(time1).tm_sec
                
                chec = val,day,mon,years,hour,evidence_path,mins,val
                if check_query != chec:
                    
                    key_check = 0
                    print(key_check)
                
                
                '''
                try:
                    val = val1.split(',')[0][8:-1].split('\n')[0]#(val.split("\n")[0]).split(',')[0][3:] #id_
                    #print(Val)
                except:
                    val = val1.split(',')[0][8:]
                print(val)
                time1 = val1.split(',')[1][9:-1]#val.split("\n")[0].split(',')[1][5:] #time.time()
                # print(stime.time()+'-'+time)
                print(time1)
                open_id.close()
                '''
                if int(eval(str(time.time())+'-'+str(time1)))>=3 :#val == "unknown" or val=="-1":
                    #print(1111)
                    with open('emotion_values.txt','r+') as f:
                        __emotions = f.read()
                        print(__emotions)
                    if f'<center><h1>{"noframe".upper()}</h1><img src="https://thumbs.dreamstime.com/b/salut-hello-french-vector-splash-paint-word-salut-word-means-hello-french-vector-calligraphic-splash-paint-letters-157761460.jpg" width="10%"/></center>' != __emotions:
                        with open('emotion_values.txt','w+') as f:
                        
                            f.write(f'<center><h1>{"noframe".upper()}</h1><img src="https://thumbs.dreamstime.com/b/salut-hello-french-vector-splash-paint-word-salut-word-means-hello-french-vector-calligraphic-splash-paint-letters-157761460.jpg" width="10%"/></center>')
                        # if f'<center><img src ="/static/status/{str(emotion_text)}' not in __emotions:
                        #     f.write('<center><img src ="/static/status/no_frame.jpg" width ="10%"/></center>')
                    #noframe = Image.open(r'/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/UI/static/convert/noframe.png')
                    #noframe = noframe.save('/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/UI/static/status/emotions.png')
                    print("parce temp")
                    name_id = open('name_id.txt','r+')
                    if name_id.readline() == "WELCOME TO":
                        name_id.close()
                        pass
                    else:
                        name = open('name_id.txt','w+')
                        name.write("WELCOME TO")
                        name.close()
                        names_1 = open('donvi.txt','w+')
                        names_1.write("DUT")
                        names_1.close()
                        
                    # continue
                elif val == "0":
                    with open('emotion_values.txt','r+') as f:
                        __emotions = f.read()
                        print(__emotions)
                    if emotion_text == "neutral":
                        if f'<center><h1>{emotion_text.upper()}</h1><img src="https://cdn4.iconfinder.com/data/icons/multisizeicon/512/baru-87-512.png" width="10%"/></center>' != __emotions:
                            with open('emotion_values.txt','w+') as f:
                                f.write(f'<center><h1>{emotion_text.upper()}</h1><img src="https://cdn4.iconfinder.com/data/icons/multisizeicon/512/baru-87-512.png" width="10%"/></center>')
                    elif emotion_text=="happy":
                        if f'<center><h1>{emotion_text.upper()}</h1><img src="https://previews.123rf.com/images/karolinamadej/karolinamadej1808/karolinamadej180800459/106249410-social-media-icon-happy-emoji-vector-.jpg" width="10%"/></center>' != __emotions:
                            with open('emotion_values.txt','w+') as f:
                                f.write(f'<center><h1>{emotion_text.upper()}</h1><img src="https://previews.123rf.com/images/karolinamadej/karolinamadej1808/karolinamadej180800459/106249410-social-media-icon-happy-emoji-vector-.jpg" width="10%"/></center>')
                        # if f'<center><img src ="/static/status/{str(emotion_text)}' not in __emotions:
                        #     f.write(f'<center><img src ="/static/status/{str(emotion_text)}.png" width ="10%"/></center>')
                    print("parce val = 0")
                    query_0 = """insert into realtime_0 select %s,%s,%s,%s,%s,%s,hovaten,donvi,ngaysinh,gioitinh,\
                            chucvu,trinhdo,hocham,%s from manager where maso = %s"""
                    value_0 = val,day,mon,years,hour,evidence_path,mins,val
                    check_query = value_0
                    if key_check == 0:
                        
                        cursor.execute(query_0,value_0)
                        cursor.close()
                        key_check= 1
                    #cursor.execute(query_0,value_0)
                    #cursor.close()
                    #cursor = database.cursor()
                    #noframe = Image.open(r'/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/UI/static/convert/noframe.png')
                    #noframe = noframe.save('/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/UI/static/status/emotions.png')
                    name_id = open('name_id.txt','r+')
                    if name_id.readline() == "WELCOME TO":
                        name_id.close()
                        pass
                    else:
                        name = open('name_id.txt','w+')
                        name.write("WELCOME TO")
                        name.close()
                        names_1 = open('donvi.txt','w+')
                        names_1.write("DUT")
                        names_1.close()
                else:
                    #print("aaa")
                    with open('emotion_values.txt','r+') as f:
                        __emotions = f.read()
                        print(__emotions)
                    if emotion_text == "neutral":
                        if f'<center><h1>{emotion_text.upper()}</h1><img src="https://cdn4.iconfinder.com/data/icons/multisizeicon/512/baru-87-512.png" width="10%"/></center>' != __emotions:
                            with open('emotion_values.txt','w+') as f:
                                f.write(f'<center><h1>{emotion_text.upper()}</h1><img src="https://cdn4.iconfinder.com/data/icons/multisizeicon/512/baru-87-512.png" width="10%"/></center>')
                    elif emotion_text=="happy":
                        if f'<center><h1>{emotion_text.upper()}</h1><img src="https://previews.123rf.com/images/karolinamadej/karolinamadej1808/karolinamadej180800459/106249410-social-media-icon-happy-emoji-vector-.jpg" width="10%"/></center>' != __emotions:
                            with open('emotion_values.txt','w+') as f:
                                f.write(f'<center><h1>{emotion_text.upper()}</h1><img src="https://previews.123rf.com/images/karolinamadej/karolinamadej1808/karolinamadej180800459/106249410-social-media-icon-happy-emoji-vector-.jpg" width="10%"/></center>')
                        # if f'<center><img src ="/static/status/{str(emotion_text)}' not in __emotions:
                        #     f.write(f'<center><img src ="/static/status/{str(emotion_text)}.png" width ="10%"/></center>')
                    
                    print("ok")
                    query_ok = """insert into realtime_0 select %s,%s,%s,%s,%s,%s,hovaten,donvi,ngaysinh,gioitinh,\
                            chucvu,trinhdo,hocham,%s from manager where maso = %s"""
                    
                    value_ok = val,day,mon,years,hour,evidence_path,mins,val
                    check_query = value_ok
                    if key_check == 0:
                        
                        cursor.execute(query_ok,value_ok)
                        cursor.close()
                        key_check= 1
                    cursor = database.cursor()
                    cursor.execute("select hovaten,donvi,chucvu,trinhdo,hocham from manager where maso={}".format(val))
                    data = cursor.fetchall()
                    cursor.close()
                    try:
                        hovaten,donvi,chucvu,trinhdo,hocham = data[0]
                    except Exception as e:
                        import logging
                        logging.warning(e)
                        continue
                    print(data[0])
                    if len(hovaten)<2:
                        print(val)
                        name = open('name_id.txt','w+')
                        name.write(str(val))
                        name.close()
                        # time.sleep(3)
                        continue
                        
                    if trinhdo == "Đại học " :
                        a = " "
                    elif trinhdo == "Thạc sỹ ":
                        a = "ThS "
                    else:
                        a = " "+round_certification(str(trinhdo))+" "
                    names = round_certification(str(hocham)) + a + hovaten

                    print(names)
                    
                    name_on = open('nameonly.txt','w+')
                    name_on.write(str(hovaten))
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
                    x = round_certification(str(chucvu))
                    if len(x)<2:
                        x=""
                    else:
                        x+=", "
                    if check_donvi == (x+str(donvi)):
                        pass
                    else:
                        with open('donvi.txt','w+') as f:
                            f.write(x+str(donvi))
                        #names_1 = open('donvi.txt','w+')
                    #names_1.write( x+ str(donvi))
                    #names_1.close()
        except KeyboardInterrupt:
            break
            

loop()
database.close()	    



	


