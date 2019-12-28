#!/usr/bin/python3

import time

def clear():
    print("\n"*50)


def sum(*x):
    a=0
    for i in x:
        a=a+i

    print("SUM:-",a)


def current():
    print("Current time is:-",time.ctime())



