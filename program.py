#!/usr/bin/python3

import time,subprocess,webbrowser,os,sys

#Static value
l1=[2,7,99,23]

#dynamic input 
dynamic_input=sys.argv[1:]
#all data except file name
sum=0
for i in dynamic_input:
    sum=sum+int(i)
    time.sleep(1)
    print("element ",i," is added")

print(sum)
