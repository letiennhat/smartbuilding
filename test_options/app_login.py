#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template,session, \
     request, url_for
import xlrd
import os
import threading
import queue
import time
import pymysql
import base64
import random as rd
from pynput.keyboard import Key,Controller
from werkzeug.utils import secure_filename
####
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import face_detec as facedetect
# import recording_video
import cv2
keyboard = Controller()
app = Flask(__name__)
id_=0 #id_ : id input data
video_url = ""
dropzone = Dropzone(app)
database = pymysql.connect('localhost','be', 'blueeyes',autocommit=True,db="mysqldb1")

import export_to_excel_from_db as exp 
app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings
try:
    if not os.path.exists(os.getcwd()+'/uploads'):
        os.mkdir(os.getcwd()+'/uploads')
    else:
        pass
except:
    pass
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

@app.route('/uploadnhieuanh', methods=['GET', 'POST'])
def uploadnhieuanh():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
    # try:
    #     files = os.listdir(os.getcwd()+'/uploads')
    #     for f in files:
    #         print(f)
    #         os.remove(os.getcwd()+'/uploads/'+f)
    # except:
    #     pass

        global photos
        # set session for image results
        if "file_urls" not in session:
            session['file_urls'] = []
        # list to hold our uploaded image urls
        file_urls = session['file_urls']
        # print(session['file_urls'])
        # handle image upload from Dropszone
        if request.method == 'POST':
            file_obj = request.files
            for f in file_obj:
                file = request.files.get(f)
                
                # save the file with to our photos folder
                filename = photos.save(
                    file,
                    name=file.filename    
                )

                # append image urls
                file_urls.append(photos.url(filename))
                
            session['file_urls'] = file_urls
            return "uploading..."
        # return dropzone template on GET request    
        return render_template('uploadnhieuanh.html')
    else:
        return render_template('trangchu.html')


@app.route('/results')
def results():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        # redirect to home if no images to display
        if "file_urls" not in session or session['file_urls'] == []:
            return redirect(url_for('uploadnhieuanh'))
            
        # set the file_urls and remove the session variable
        file_urls = session['file_urls']
        session.pop('file_urls', None)
        
        return render_template('resultsnhieuanh.html', file_urls=file_urls)
    else:
        return render_template('trangchu.html')
book = xlrd.open_workbook("data.xlsx")
sh = book.sheet_by_index(0)

data_2 = queue.Queue(maxsize = 1)
data_1 = queue.Queue(maxsize = 1)
data_id = queue.Queue(maxsize=1)
list_name = queue.Queue(maxsize=1)
list_name_vang = queue.Queue(maxsize=1)
data_rung = []
# t = queue.Queue(maxsize=1)
# list_SV = queue.Queue(maxsize=1)
# ten_input = queue.Queue(maxsize=1)
# ten_input = "HELLO ˆ_^"
danhsachvang = ["a",'b']

danhsachvang = ["a",'b']
donvi = []
donvi_dachon = queue.Queue(maxsize=1)
infor_result = queue.Queue(maxsize=1)
donvi_dachon = "Ban Giám hiệu"
bomon=queue.Queue(maxsize=1)
bomon=""

# list_name = ['']
try:
     danhsachcomat = open('../Blue_eyes/regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+\
        str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)+'.txt','r')
     list_name=danhsachcomat.read().split('\n')
     danhsachcomat.close()
     # re_name(list_name)
     # time.sleep(2)
except:
        danhsachcomat = open('../Blue_eyes/regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+\
        str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)+'.txt','w+')
     # list_name=danhsachcomat.read().split('\n')
        danhsachcomat.close()
def re_name(d):
    '''
        không dùng
    '''
    for i in range(len(d)):
        d[i]=namez(d[i])
    #print(d)

    return d
def name():
    '''
        không dùng
    '''
    global list_name
   # global list_SV
    global list_name_vang   
   # global ten_input
   # 
   # global t
    global bomon
    global sh
    global donvi_dachon
    global donvi
    while 1:
      # bomon = loop_bomon(donvi_dachon)
      donvi = loop_donvi()
      # time.sleep(2)
      danhsachcomat =["b", 'e']
      try:
         danhsachcomat = open('../Blue_eyes/regular_review/hour'+str(time.localtime(time.time()).tm_hour)+'.txt/'+\
            str(time.localtime(time.time()).tm_mon) +'_'+str(time.localtime(time.time()).tm_mday) +'_'+str(time.localtime(time.time()).tm_year)+'.txt','r')
         list_name=danhsachcomat.read().split('\n')
         danhsachcomat.close()
         # re_name(list_name)
         # time.sleep(2)
      except:
         pass
def find_data_byid(id_):
  global database
  cursor = database.cursor()
  #cursor.execute("use mysqldb1")
  
  # print(cursor.execute("show tables;"))
  # cursor.execute("select gio from realtime_0 where id=10542")

  # data = cursor.fetchall()
  # cursor.close()
  # cursor = database.cursor()
  
  cursor.execute("select id,hovaten,donvi,ngaysinh,gioitinh,chucvu,trinhdo,hocham,ngay,thang,nam,gio,url from realtime_0 where id={0} and nam={1}".format(str(id_),str(time.localtime(time.time()).tm_year)))
  
  data_11 = cursor.fetchall()
  #database.commit()
  # cursor1.close()
  cursor.close()
  #database.close()
  return data_11
def loop_realtime():
    # global cursor
    # global data
    # global database
    try:
        global database
        cursor_looprealtime = database.cursor()
        cursor_looprealtime.execute("select * from key_login")
        key = cursor_looprealtime.fetchone()[0]
        cursor_looprealtime.close()
        if str(key)=="1":
            global data_1
            global data_id
            #global database
            #while 1:
            # database = pymysql.connect(host='localhost',
            #                             user='be',
            #                             password= 'blueeyes',
            #                             autocommit=True,
            #                             )
            try:
                cursor_looprealtime = database.cursor()
                # cursor1 = database.cursor()
                #cursor.execute("use mysqldb1")
                # cursor1.execute("use mysqldb1")
                # print(cursor.execute("show tables;"))
                # cursor.execute("select gio from realtime_0 where id=10542")

                # data = cursor.fetchall()
                # cursor.close()
                # cursor = database.cursor()
                cursor_looprealtime.execute("select id,hovaten,donvi,ngay,thang,nam,gio,phut,url from realtime_0 where ngay = {} and thang={} and nam = {}".format(str(time.localtime(time.time()).tm_mday),str(time.localtime(time.time()).tm_mon),str(time.localtime(time.time()).tm_year)))
                # cursor.execute("select ngay,gio,hovaten,chucvu from realtime_0 where id=1")
                # data_id = cursor1.fetchall()
                data_1 = cursor_looprealtime.fetchall()
                #database.commit()
                # cursor1.close()
                cursor_looprealtime.close()
                #database.close()
            except:
                pass
        else:
            return render_template('trangchu.html')
    except:
        return render_template('trangchu.html')
def standard_name(name):
    name_ = name.split()
    name_1 = name_[0]
    print(name_)
    for i in name_[1:]:
        if len(i)>=2:
            name_1+=" "+i
    return name_1

def loop_ten(donvi,name):
    '''
        không dùng 
    '''
    data =[]
    global sh
    for i in range(0,sh.nrows):
        try:

            if (str(sh.row_values(i)[7])==donvi) and standard_name(str(sh.row_values(i)[3]))==standard_name(str(name)):
                for i in (sh.row_values(i)[0:2]+sh.row_values(i)[3:]):
                    if type(i)==float:
                        data.append(int(i))
                    else:
                        data.append(str(i))
                return data
        except:
            print("loi")
            pass
    return data

def loop_donvi():
    '''
        Không dùng
    '''
    data =[]
    global sh

    for i in range(0,sh.nrows):
        try:
            if str(sh.row_values(i)[7]) not in data:
                if len(sh.row_values(i)[7]) >=3 :
                    data.append(str(sh.row_values(i)[7]))
                
        except:
            print("loi")
            pass
    return data
def loop1():
    '''
        Không dùng
    '''
    data =[]
    global sh

    for i in range(0,sh.nrows):
        try:
            if str(sh.row_values(i)[3]) not in data:

                data.append(str(sh.row_values(i)[3]))
                
        except:
            print("loi")
            pass
    return data
def loop2(index):
    '''
        Không dùng
    '''
    data = []
    global sh
    for i in range(0,sh.nrows):
        try:
            if str(sh.row_values(i)[3]) == str(index):
                for j in sh.row_values(i)[6:]:
                    data.append(j)
                break

        except:
            pass
    x=" "
    for i in data:
        x+=str(i)+" "
    return x

def read_form (names_):
  fi = open('../Blue_eyes/best/input_1.txt','w+')
  fi.write(str(names_))
  fi.close()


try :
    if not os.path.exists('../Blue_eyes/video/'):
        os.mkdir('../Blue_eyes/video/')
    else:
        pass
except:
    pass
app.config["VIDEO_UPLOADS"] = "/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/Blue_eyes/video/"
app.config['MAX_CONTENT_PATH'] = 500*1024*1024
@app.route('/uploadedvideo',methods=['GET','POST'])
def cut_box_face():
    global id_
    global video_url
    value = request.form.get("uploadedvideo")
    if value == "Begin-detect":
        facedetect.run(str(video_url),id_)
        print("Done")
        return redirect(url_for('uploadnhieuanh'))
    else:
        pass


# app.config["IMAGE_UPLOADS"] = "/home/blueeyes1/smartbuilding/smartbuilding/Blue_eyes/image_css/"
@app.route('/uploadvideo',methods=['GET','POST'])
def uploadvideo1():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        try:
            global video_url
            global id_
            print(id_)

            # image = request.files['image']
            image = request.files["image"]
            filename = secure_filename(image.filename)

            print(type(filename))
            try:
                if not os.path.exists('/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/Blue_eyes/video/'+str(id_)+'/'):
                    os.mkdir('/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/Blue_eyes/video/'+str(id_)+'/')
                else:
                    
                    pass
            except:
                print('"loi permission"')
                pass
            image.save(os.path.join(app.config["VIDEO_UPLOADS"]+str(id_)+'/',filename))
            video_url = app.config["VIDEO_UPLOADS"]+str(id_)+'/'+filename
            #va_choose = request.form.get('reset_system')
            #if va_choose == "Reset-System":

                #keyboard.press('r')
            return render_template('uploadvideo.html',va = "đã upload thư mục url ="+'/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/Blue_eyes/video/'+str(id_)+'/',ba='input type=submit formaction=/uploadedvideo value=Begin-detect đã upload name=uploadedvideo')
        except:
            pass
    else:
        return render_template('trangchu.html')
app.config["IMAGE_UPLOADS"] = "/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/Blue_eyes/image_css/"
app.config['MAX_CONTENT_PATH'] = 500*1024*1024
@app.route('/uploadimage',methods=['GET','POST'])
def uploadimage1():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        try:
            global id_
            print(id_)

            image = request.files['image']
            filename = secure_filename(image.filename)
            print(type(filename))
            if not os.path.exists('/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/Blue_eyes/image_css/'+str(id_)+'/'):
                os.mkdir('/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/Blue_eyes/image_css/'+str(id_)+'/')
            else:
                pass
            image.save(os.path.join(app.config["IMAGE_UPLOADS"]+str(id_)+'/',filename))
            va_choose = request.form.get('reset_system')
            if va_choose == "Reset-System":

                return render_template('resetsystem.html')
            return render_template('uploadanh.html',va="đã Lưu vào thư mục : " + '/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/Blue_eyes/image_css/'+str(id_)+'/')
        except:
            pass
    else:
        return render_template('trangchu.html')
@app.route('/uploaded_data',methods = ['GET','POST'])
def uploaded_data():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        try:
            value = request.form.get('input_data')
            if value=="Xác nhận chính xác":
                try:
                    if os.path.exists('../Blue_eyes/image_css/'+str(id_)):
                        pass
                        #os.rename('/home/blueeyes1/smartbuilding/smartbuilding/Blue_eyes/image_css/'+str(id_),'/Users/letiennhat/racruoi/'+str(id(id_)))
                    else:
                        pass
                    for i in os.listdir(os.getcwd()+'/uploads'):
                        os.rename(os.getcwd()+'/uploads/'+i,'../Blue_eyes/image_css/'+str(id_)+'/'+i)
                    #os.rename(os.getcwd() + '/uploads/','/home/blueeyes1/smartbuilding/smartbuilding/Blue_eyes/image_css/'+str(id_))
                    #os.mkdir(os.getcwd() + '/uploads/')
                except:
                    #os.rename(os.getcwd() + '/uploads/','/home/blueeyes1/smartbuilding/smartbuilding/Blue_eyes/image_css/'+str(id_))
                    os.mkdir(os.getcwd() + '/uploads/')
                    pass
                return render_template('resetsystem.html')
                return "<h1> UPLOADED </h1>"
        except:
            return render_template('trangchu.html')
    else:
        return render_template('trangchu.html')

@app.route('/hocnguoi_2',methods=['GET','POST'])
def hocnguoi_1():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        try:
            #global database
            global id_
            choose = str(request.form.get('text'))
            try:
                if str(request.form.get('get_value_recording'))=="Stop-recording":
                    cursor = database.cursor()
                    #cursor.execute("use mysqldb1")
                    cursor.execute("update learn_values set val = 2")
                    cursor.close()
                    cursor = database.cursor()
                    time.sleep(1)
                    cursor.execute("update learn_values set val = 0")
                    os.rename('video/outpy.avi','video/output1.avi')
                    # cv2.VideoWriter('video/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,850))
                    database.commit()
                    cursor.close()
                    return render_template("uploadvideo.html",va="",ba="")
                    return "DA RECORDING"
            except:
                pass
            if len(choose)>0 and str(choose) == str(id_):
                #print(choose)
                #print(str(request.form.get('get_value_recording')))
                if (str(request.form.get('get_value_recording'))=="Start-Recording"):
                    #start recording and display button stop recording
                    cursor = database.cursor()
                    #cursor.execute("use mysqldb1")
                    cursor.execute("update learn_values set val = 1")
                    #print(1)
                    #database.commit()
                    #print(2)
                    cursor.close()
                    #print(3)
                    # return "OK"
                    # return render_template('hocnguoi_step_2.html',va='''input type=submit  value = Stop-recording name =get_value_recording''')
                    # recording_video.run(id_)
                    try:
                        # threading.Thread(target=run_video).start()
                        # run_video()
                        return render_template('hocnguoi_step_2.html',va='''input type=submit  value = Stop-recording name =get_value_recording''')
                    except:
                        return render_template('trangchu.html')

                if (str(request.form.get('get_value_recording'))=="LOAD-AUTOMATION-LEARN"):
                    #print(1293921391)
                    #fi = open('../Blue_eyes/best/input_1.txt','w+')
                    #fi.write(str(choose))
                    #fi.close()
                    read_form(choose)
                    return "PRESS A (50 time) IN FRAME TO LEARN NEW PERSON"
                
                #return render_template('index1.html')
        except:
            pass
    else:
        return render_template('trangchu.html')
@app.route('/reset',methods=['GET','POST'])
def reset_system():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        try:
            #global database
            if request.form.get('get_value_reset') == "RESET-NOW":
                cursor = database.cursor()
                #cursor.execute("use mysqldb1")
                cursor.execute("update values_reset set val = 1")
                cursor.close()
            elif request.form.get('get_value_reset') == "RESET-TIMER-00:00":
                cursor = database.cursor()
                #cursor.execute("use mysqldb1")
                cursor.execute("update values_reset set val = 2")
                cursor.close()
            else:
                pass
            return render_template('begin.html')
        except:
            pass
    else:
        return render_template('trangchu.html')

@app.route('/hocnguoi',methods=['GET','POST'])
def hocnguoi():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        try:
            choose1 = str(request.form.get('chon_options_hocnguoi'))
            if choose1 == "1.Từ camera":
                return render_template('hocnguoi_step_2.html')
            elif choose1 == "Tải ảnh":
                va = "Chọn ảnh là .jpg và upload từng ảnh một theo format classe0.jpg càng tốt"
                return render_template('uploadanh.html',va = va)
            elif choose1 == "3.Tải lên nhiều ảnh":
                va = "Chọn những ảnh là .jpg và upload từng ảnh một theo format classe0.jpg càng tốt"
                return render_template('uploadnhieuanh.html',va = va)
            elif choose1 == "2.Tải lên Video":
                va = "Chọn những video là .mp4 và upload 1 video chất lượng tốt"
                return render_template('uploadvideo.html',va=va)
        except:
            pass
    else:
        return render_template('trangchu.html')

@app.route('/realtime')
def realtime():
    try:

        global database
        cursor = database.cursor()
        cursor.execute("select * from key_login")
        key =  cursor.fetchone()[0]
        cursor.close()
        if str(key)=="1":
            try:
                loop_realtime()
                global data_1
                data_2 = data_1[::-1]
                return render_template('test_pysql.html',data=data_2)
                #return render_template('hienthirealtime.html',lit_comat = list_name,)
            except:
                return render_template('trangchu.html')
                pass
        else:
            return render_template('trangchu.html')
    except:
        return render_template('trangchu.html')
@app.route('/exported',methods=['GET','POST'])
def export_to_excel():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        #realtime tables to excel from all time
        
        exp.run('realtime_0')
        return "<h1> DA EXPORT "+str(os.getcwd())+'/ds_realtime_0.xlsx</h1>'+'''<style> button{
        border-radius:10% 30% 50% 20%;
            /*block-size: 28px;*/
            color: red;
            font-size: 39pt;
            size: "10";
            width: 200px; height: 300px;
        }</style><form  action="/" align="center"><button >BACK</button></form>'''
    else:
        return render_template('trangchu.html')


@app.route('/hienthi',methods=['GET','POST'])
def hienthi():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        #global database
        try: 
            # global data_id
            # data_main = data_id[::-1]
            #database = pymysql.connect('localhost','be', 'blueeyes',autocommit=True,)
            cursor = database.cursor()
            #cursor.execute("use mysqldb1")
            cursor.execute("select distinct donvi from manager")
            donvi = cursor.fetchall()
            #database.commit()
            cursor.close()
            #database.close()

            choose = request.form.get('hienthi')
            if choose == 'Theo thời gian':
                return redirect(url_for('realtime'))
            elif choose == 'Thông tin cá nhân':
                return render_template('hienthidonvi.html',donvi=donvi,bomon=bomon)
            elif choose == "Theo Đơn vị / Cá nhân":
                return render_template('hienthidonvicanhan.php',donvi=donvi)
                return render_template('hienthidonvicanhan.html',donvi=donvi)
        except:
            pass
    else:
        return render_template('trangchu.html')
@app.route('/hocanh',methods=['GET','POST'])
def save_data():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        try:
            global id_
            #global database
            id_input = request.form.get('id')
            hovaten = request.form.get('hovaten')
            ten = request.form.get('ten')
            ngaysinh = request.form.get('ngaysinh')
            gioitinh = request.form.get('gioitinh')
            donvi_1 = request.form.get('donvi')
            bomon_1 = request.form.get('bomon')
            chucvu_1 = request.form.get('chucvu')
            trinhdo = request.form.get('trinhdo')
            hocham = request.form.get('hocham')
            #database = pymysql.connect('localhost','be', 'blueeyes',autocommit=True,)
            #cursor = database.cursor()
            #cursor.execute("use mysqldb1")
            # while 1:
            #   id_ = rd.randint(7000,10000000000)
            #   cursor.execute("select maso from manager where maso={}".format(str(id_)))
            #   if len(cursor.fetchall())<1:
            #     print("ok")
            #     break
            #   else:
            #     pass
            if len(id_input)>=1:
                id_ = id_input
            else:
                while 1:
                    id_ = rd.randint(7000,10000000000)
                    cursor = database.cursor()
                    cursor.execute("select maso from manager where maso={}".format(str(id_)))
                    if len(cursor.fetchall())<1:
                        print("ok")
                        cursor.close()
                        break
                    else:
                        pass
            query_1 = """select maso from manager where maso = %s"""
            cursor = database.cursor()
            cursor.execute(query_1,id_)
            check_id = cursor.fetchall()
            cursor.close()
            if len(check_id)>=1:
                #database.commit()
                
                #database.close()
                return render_template('hocnguoi.html',id_ = str(id_)+" Đã có trong database, xin mời kiểm tra lại, nếu bạn chắc chắn thì mời gữi ảnh vào để train")
            else:
                


                query = """insert into manager(maso, hovaten, ten, ngaysinh, gioitinh, donvi, bomon, chucvu, trinhdo, hocham) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                values_query = str(id_),hovaten,ten,ngaysinh,gioitinh,donvi_1,bomon_1,chucvu_1,trinhdo,hocham
                cursor = database.cursor()
                cursor.execute(query,values_query)
                #database.commit()
                cursor.close()
                #database.close()
                return render_template('hocnguoi.html',id_ = str(id_)+ " Hãy lưu lại mã số id của bạn để nhập vào thay vì nhập họ và tên")
        except:
            pass
    else:
        return render_template('trangchu.html')
a='ac'
def handle_base64(bs):
    
    try:
        global a
        image_64 = bs.encode("UTF-8");
        # print(type(image_64))
        try:
            os.remove('static/'+a+'.jpg')
        except:
            pass 
        ba = base64.decodebytes(image_64)
        a='base64/'+str(time.time())
        ne = open('static/'+a+'.jpg','wb')
        ne.write(ba)
        ne.close()
    except:
        pass

@app.route('/hienthi_anh',methods=['GET','POST'])
def hienthi_anh():  
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        try:
            global data_2 
            # print(data_2)
            global a
            choose = request.form.get('clicktoview')
            if not str(choose).startswith('-'):
            # print(type(data_2))
            # print(choose)
            # print(choose)
            # name = request.form.get('name_input')
            # choose = str(data_2.index(choose))
            # print(data_2[int(choose)][-1])
                if "sbuilding" in (data_2[int(choose)][-1]):
                    a=data_2[int(choose)][-1]
                else:
                    handle_base64(data_2[int(choose)][-1])
                print(a)
                return render_template("hienthianh.html",tenanh=a) # fucntion 
            else:
                cursor = database.cursor()
                cursor.execute(f"select url from realtime_0 where ngay = {time.localtime(time.time()).tm_mday} and thang = {time.localtime(time.time()).tm_mon}")
                data_ = cursor.fetchall() #((,),(,)...,(,))
                print(data_)
                b=data_[int(choose)-1][0]
                print(b)
                return render_template("hienthianh.html",tenanh=b)
        
        except:
            pass
    else:
        return render_template('trangchu.html')

@app.route('/name',methods=['GET','POST'])
def name1():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        global data_rung
        return render_template('hienthi_ten.html',da=data_rung)
    else:
        return render_template('trangchu.html')


#app = Flask(__name__)
# @app.route('/thongke')
def thongke():
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        #global database
        cursor = database.cursor()
        #cursor.execute("use mysqldb1")
        cursor.execute("select distinct donvi from manager")
        donvi_1=cursor.fetchall()
        cursor.close()
        #print(donvi)
        x = []
        max_values = []
        for i in donvi_1:
            cursor = database.cursor()
            #cursor.execute("use mysqldb1")
            #print(i[0])
            cursor.execute("select count(id) from realtime_0 where donvi like '%{}%'".format(i[0]))
            value = cursor.fetchall()
            #print(value)
            cursor.close()
            x.append([i[0],value[0][0]])
            max_values.append(value[0][0])
        #print(x)
        max_val = max(max_values)
        return x,max_val
    else:
        return render_template('trangchu.html')

	

	#return render_template('chart.html',data1=x,max = max_val)

@app.route('/hienthi_donvi_ten',methods=['GET','POST'])
def hienthi_bomon(): 
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        try:
            global donvi_dachon
            global infor_result 
            #global database  
            choose = request.form.get('choose_donvi_1')
            name = request.form.get('name_input')
            if choose =="unknown":
                name = ""
            #database = pymysql.connect('localhost','be', 'blueeyes',autocommit=True,)
            
            #cursor.execute("use mysqldb1")
            if len(name)>0:
                cursor = database.cursor()
                cursor.execute("select * from manager where donvi like '%{0}%' and hovaten like '%{1}%'".format(choose,standard_name(name)))
                data_rung = cursor.fetchall()
                cursor.close()
            else:
                cursor = database.cursor()
                cursor.execute("select * from manager where donvi like '%{0}%'".format(choose))
                data_rung = cursor.fetchall()
                cursor.close()
            
            #database.commit()
            #cursor.close()
            #database.close()
            return render_template('hienthi_ten.html',da=data_rung)
            #infor_result = loop_ten(choose,name)
            #return name1(data_rung)
            #return redirect(url_for('name1')) # fucntion 
            # print(len(name))
        except:
            return render_template('trangchu.html')
    else:
        return render_template('trangchu.html')
@app.route('/hienthi_donvi_canhan',methods=['GET','POST'])
def hienthi_donvi_canhan(): 
    global database
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        global donvi_dachon
        global infor_result  
        global data_2
        #global database
        choose = request.form.get('choose_donvi_canhan')
        name = request.form.get('name_input')
        if choose == "unknown":
            name = "unknown"
        else:
            pass
        if len(name)>0:
            try:
                
                #database = pymysql.connect('localhost','be', 'blueeyes',autocommit=True,)
                cursor = database.cursor()
                #cursor.execute("use mysqldb1")
                cursor.execute("select maso from manager where donvi like '%{0}%' and hovaten like '%{1}%'".format(choose,standard_name(name)))
                infor_r = cursor.fetchall()[0][0]
                print(infor_r)
                #database.commit()
                cursor.close()
                #database.close()
                data_2=find_data_byid(infor_r)[::-1]
                
                #infor_result = loop_ten(choose,name)[0]
            except:
                pass
        else:
            try:
                #database = pymysql.connect('localhost','be', 'blueeyes',autocommit=True,)
                cursor = database.cursor()
                #cursor.execute("use mysqldb1")
                cursor.execute("select id,hovaten,donvi,ngaysinh,gioitinh,chucvu,trinhdo,hocham,ngay,thang,nam,gio,phut,url from realtime_0 where donvi like '%{0}%'".format(choose))
                data_2 = cursor.fetchall()
                if len(data_2)<=0:
                    return "Nothing"
                else:
                    pass

                database.commit()
                cursor.close()
                #database.close()
            except:
                pass
        if len(data_2[0])>=14:
            xxx=0
        else:
            xxx = 1
            


        
        return render_template('test_pysql1.html',data=data_2,name=name,xxx=xxx) # fucntion 
    else:
        return render_template('trangchu.html')
@app.route('/trangchu',methods=['GET', 'POST'])
def trangchu():
    global database
    cursor = database.cursor()
    cursor = database.cursor()
    cursor.execute("select * from key_login")
    key =  cursor.fetchone()[0]
    cursor.close()
    if str(key)=="1":
        #global database
        choose = request.form.get('trangchu')
        x,y = thongke()
        print(type(choose))
        if choose == "Học thông tin cá nhân mới":
            return render_template('input_data.html')
            #return render_template('hocnguoi.html')
        elif choose == "Thông tin ra vào tòa nhà":
            return render_template('hienthi_choose.html')
            #return render_template('choose_hienthi.html')
            # return "Xem Thông tin người vào ra tòa nhà"
        
        elif choose == "Dữ liệu thống kê":
            return render_template('chart.html',data1=x,max=y)
        else:
            cursor = database.cursor()
            #cursor.execute("use mysqldb1")
            cursor.execute("update key_login set val = 0")
            cursor.close()
            render_template('dangxuat.html')
            print(f'loading...')
            return render_template('trangchu.html')
    else:
        return render_template('trangchu.html')
    # elif request.method == 'GET':
    #     return render_template('index.html', form=form)
'''
@app.route('/')
def index():
    return render_template(
        'begin.html')
    return render_template(
        'index1.html')
'''
        # data=[{'name':'All office'},{'name':'BAN GIÁM HIỆU'}, {'name':'KHOA CÔNG NGHỆ NHIỆT - ĐIỆN LẠNH'}, {'name':'KHOA CƠ KHÍ'},{'name':'KHOA CƠ KHÍ GIAO THÔNG'},\
        # {'name':'KHOA CÔNG NGHỆ THÔNG TIN'},{'name':'KHOA ĐIỆN'},{'name':'KHOA ĐIỆN TỬ  - VIỄN THÔNG'},{'name':'KHOA HÓA'},{'name':'KHOA KIẾN TRÚC'}\
        # ,{'name':'KHOA MÔI TRƯỜNG'},{'name':'KHOA QUẢN LÝ DỰ ÁN'},{'name':'KHOA XÂY DỰNG CẦU ĐƯỜNG'},{'name':'KHOA XÂY DỰNG DÂN DỤNG VÀ CÔNG NGHIỆP'},\
        # {'name':'KHOA XÂY DỰNG THỦY LỢI - THỦY ĐIỆN'},{'name':'KHOA KHOA HỌC CÔNG NGHỆ TIÊN TiẾN'},{'name':'PHÒNG CƠ SỞ VẬT CHẤT'},\
        # {'name':'PHÒNG CÔNG TÁC SINH VIÊN'},{'name':'TRUNG TÂM HỖ TRỢ SINH VIÊN VÀ QUAN HỆ DOANH NGHIỆP'},{'name':'PHÒNG ĐÀO TẠO'},{'name':'PHÒNG KẾ HOẠCH - TÀI CHÍNH'},\
        # {'name':'PHÒNG KHẢO THÍ VÀ ĐẢM BẢO CHẤT LƯỢNG GIÁO DỤC'},{'name':'PHÒNG KHOA HỌC CÔNG NGHỆ VÀ HỢP TÁC QUỐC TẾ'},{'name':'PHÒNG THANH TRA - PHÁP CHẾ'},\
        # {'name':'PHÒNG TỔ CHỨC - HÀNH CHÍNH'},{'name':'TỔ CÔNG NGHỆ THÔNG TIN'},{'name':'VĂN PHÒNG ĐẢNG - CÔNG ĐOÀN - ĐOÀN TN'},\
        # {'name':'TRUNG TÂM HỌC LIỆU VÀ TRUYỀN THÔNG'},{'name':'VIỆN KHOA HỌC CÔNG NGHỆ BÁCH KHOA'}],\
        # data1=loop(),data2=loop1(),)
@app.route('/',methods=['GET','POST'])
def index_0():
    return render_template('trangchu.html')
@app.route('/login',methods=['GET','POST'])
def login():
    try:
        signal = request.form["login"]
        if signal == "LOGIN":
            return render_template('login_ok.html')
        else:
            return redirect(url_for('index_0'))
    except:
        return redirect(url_for('index_0'))
@app.route('/dangnhap',methods=['GET','POST'])
def dangnhap():
    try:
        global database
        user = request.form["username"]
        cursor = database.cursor()
        #cursor.execute("use mysqldb1")
        cursor.execute('select passwd,key_ from login where username="{}"'.format(user))
        password,key_ = cursor.fetchall()[0] # (('admin',28101997),)
        #key_ = password
        cursor.close()
        
        passwd = request.form["password"]
        if user=="admin":
            if passwd == password :
                #login successfull
                # user = request.form.get["username"]
                cursor = database.cursor()
                #cursor.execute("use mysqldb1")
                cursor.execute("update key_login set val = 1")
                cursor.close()
                cursor = database.cursor()
                #cursor.execute("use mysqldb1")
                cursor.execute("select * from key_login")
                key =  cursor.fetchone()[0]
                cursor.close()
                if str(key)=="1":
                    return render_template('begin.html')
                else:
                    return redirect(url_for('index_0'))
            else:
                return render_template('trangchu.html')
        else:
            return render_template('trangchu.html')
    except:
        return render_template('trangchu.html')
                      
            

'''
@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    select1 = request.form.get('comp_select1')
    select2 = request.form.get('comp_select2')
    return 11111
    if select =="of":
        # return render_template(
        #     'index.html',
        #     data=[{'name':'red'}, {'name':'green'}, {'name':'blue'},{'name':'yellow'}])
        return("Thong tin :\n"+str(loop2(select2))) # just to see what select is
'''
if __name__=='__main__':
    try:
        threading.Thread(target = name).start()
        threading.Thread(target = loop_realtime).start()
    except:
        pass
    try:
        app.run(host = "0.0.0.0",port = 5555,debug=1)
    except Exception as e:
        import logging
        logging.warning(e)
    database.close()