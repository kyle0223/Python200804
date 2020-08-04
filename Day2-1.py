# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:09:20 2020

@author: AE401
"""

import random
A=random.randint(1,10)
number=int(input("輸入1~10的數字"))
if number<1 or number>10:
    print("重打!!!!!!!")
if A==number:
    print('答對')
else:
    print("錯")
