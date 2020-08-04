# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:22:49 2020

@author: AE401
"""

import random
A=random.randint(1,20)
while True :
    
    number=int(input("輸入1~20的數字"))
    if number<=0 or number>20:
        print("wrong")
    else:
        if A>number:
            print("大一點")
        elif A<number:
            print("小一點")
        else:
            print("correct") 
            break