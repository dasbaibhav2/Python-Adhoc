#!/usr/bin/python3

import time,subprocess,webbrowser,os,sys

l1=[2,7,99,23]

sum=0
for i in l1:
    sum=sum+i
    time.sleep(1)
    print("element ",i," is added")

print(sum)
