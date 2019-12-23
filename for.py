#!/usr/bin/python3

import os
#open the file where numbers are saved
f=open("file.txt","r")
sum =0
#summation of all the numbers in the file.txt
for i in f:
    sum= sum +int( i )

print("The total sum in the file is:-",sum)
