import email
import imaplib
import ctypes
import getpass
import credentials
import threading
mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
unm = "nhatpropct98@gmail.com"
pwd = credentials.passwd
mail.login(unm,pwd)
mail.select("INBOX")
subject = "testid"
a=0
#import queue
import yagmail
#que = queue.Queue(maxsize = 1)

def send():
    receiver = "nhatpropct98@gmail.com"
    body = "WARNING WARNING"
    yag = yagmail.SMTP("ltn281097@gmail.com")


    yag.send(to=receiver,subject = "WARNING",contents = body,)

def loop():
    global a
    #global que
    while 1:
        mail.select("INBOX")
        n = 0
        (retcode, messages) = mail.search(None,'(UNSEEN SUBJECT "%s")' % subject)
        #print(messages)
        if retcode == 'OK':
            for num in messages[0].split():
                n = n+1
                #print(n)
                typ, data = mail.fetch(num,'(RFC822)')
                #print(data)
                body = data[0][1]
                body = body.decode("utf-8")
                #print(type(body.decode("utf-8")))
                print(body)
                if "quoted-printable" in body:

                    content = body.split("quoted-printable")[1][4:10]
                else:
                    content = body.split('charset="UTF-8"')[1][4:10]
                save = open('id.txt','w+')
                save.write(str(content))
                save.close()
threading.Thread(target = loop).start()
'''

def main():

    threading.Thread(target = loop).start()
main()
'''
'''
if __name__ == '__main__':
    while 1:
        for i in range(10000):
            a=i
'''
