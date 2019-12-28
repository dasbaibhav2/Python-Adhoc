#!/usr/bin/python3

# Import the required module for text 
# to speech conversion 
# install gTTS using pip3 install gTTS
from gtts import gTTS 
import os 

f=open("file.txt","r")
sum =0
#summation of all the numbers in the file.txt
for i in f:
    sum= sum +int( i )

a=str(sum)

language = 'en'

myobj = gTTS(text=a, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named welcome 
myobj.save("result.mp3") 

# Playing the converted file 
#install mpg321 using sudo apt install mpg321
os.system("mpg321 result.mp3") 
