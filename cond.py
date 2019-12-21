#!/usr/bin/python3

import os
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
	os.system("google-chrome")
if choice == '2':
	os.system("ping google.com")
if  choice  ==  '4'  :
	print("current time is ",subprocess.getoutput("date +%T"))
else :
	print("wrong option")
