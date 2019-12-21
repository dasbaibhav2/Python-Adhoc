#!/usr/bin/python3

import os
import webbrowser
import  subprocess
options="""
Press  1  to  start your default web browser :- 
Press  2  to  check your internet connection speed :- 
Press  3  to check your internet status  :- 
Press  4  to check current date and  time:- 
Press  5   to check current temperature in your city :- 
Press  6   to check current public IP :- 
Press  7   to create  a directory in your OS :- 
Press  8   to reboot your system :- 
Press  9   to play song in you tube  :- 
Press  10   to search something in google search engine  :- 
"""
print(options)
#  to accept input from user
choice=input()
#  input  function will accept in string form only
print("you have entered  "+choice)
#  conditional statements
if choice == '1' :
	#open default webbrowser
    webbrowser.open_new_tab('https://www.google.com')
elif choice == '2':
	os.system("ping -c 5 google.com")
elif choice == '3' :
    output=subprocess.getstatusoutput('ping -c 2 google.com')
    if output[0] == 0:
        print("Your Internet is working fine")
    else:
        print("Your internet is not working")
elif  choice  ==  '4'  :
	print("current time is ",subprocess.getoutput("date +%T"))
elif choice == '7':
    dir_name=input("Enter name of the directory")
    dir_output=subprocess.getstatusoutput("mkdir "+dir_name)
    if dir_output[0] == 0:
        print("Your directory "+dir_name+"successfully created")
    else:
        print("Change your directory name")
elif choice == '10':
    msg=input("Please enter your message:-")
    webbrowser.open_new_tab('https://www.google.com/search?q='+msg)
