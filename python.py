#!/usr/bin/python3
import os
print ("Press 1 to show date\nPress 2 to show calender\nPress 3 to shutdown Pc\nPress 4 to show IP\nPress 5 to show all IP connect to Pc\n")
var=int(input("ENTER A CHOICE\n"))
if var==1:
	print("DATE IS:-\n")
	os.system("date")
elif var==2:
	print("CALENDER:-\n")
	os.system("cal")
elif var==3:
	print("SYSTEM WILL SHUTDOWN IN 5 SEC")
	os.system("sleep 5s; shutdown -h now")
elif var==4:
	print("IP OF THIS MACHINE:\n")
	os.system("ifconfig")
elif var==5:
	print("IP all")
	os.system("ip a s")
elif var==6:
	print("Enter a Keyword:\n")
