# module
try:
  import os,sys,time,requests,bs4
  from bs4 import Beautifulsoup
  from time import sleep
  from os import system
except:
      system("pip install requests bs4")
 # tampilan
def jalan():
   tampil = """
==================================
Author : MR.CyberHack
Team  : IndonesiaCyberXploid 
=================================="""
    system("clear")
    sleep(1)
    system("figlet GOOGLE")
    sleep(1)
    print(tampil)
    # isi data
    file = imput("Masuk Pencarian: ")
    ulr = f"https://www.google.com/search?&q=(file)"
    r  = requests.get(url)
    cari = BeautifulSoup(r.text. "html parser")
    a  = cari.find("div",class_="BNeawe").text
    # hasil pencarian
    print("Hasil => ",a)

jalan()
 