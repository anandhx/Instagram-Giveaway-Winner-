import os
import sys
import time
from itertools import count
from time import sleep
from random import randint
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def delay_counter(delay_time):
    while delay_time:
        mins, secs = divmod(delay_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\u001b[31;1m   ",timer, end="\r\u001b[0m")
        time.sleep(1)
        delay_time -= 1
 







      
def cron():
  counter = 0
  abc = 0
  slp = 0
  while True:
      #replace your username and password 
      #os.system("python (how much mention).py -u (enter username) -p (enter password) ") 
      #example 
      #os.system("python 5mentions.py -u the__hell__gurl -p shazzam@12")
      #replace the__hell__gurl = your username 
      #replace shazzam@12 = your password
      os.system("python 5mentions.py -u the__hell__gurl -p shazzam@12")
      counter += 1
      abc += 1
      slp += 1
      print("\u001b[32mTotal comments : \u001b[0m",counter)
      print('')
      delay_counter(randint(1750,2000))
      #delay_counter(randint(1,5))
      sleep(randint(5,9))
      if slp>= 48:
        print("\u001b[34;1m-- JUST TAKE A LONG BREAK --\u001b[0m")
        delay_counter(5500)
        slp = 0
      if abc>=29:
        print("\u001b[34;1m-- JUST TAKE A short BREAK --\u001b[0m")
        delay_counter(1600)
        abc = 0
       
        
cron()