# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:47:25 2020

@author: AE401
"""
name=[]
score=[]
total=0
avg=0
highest=0
lowest=100
n=int(input("how many people?"))
for e in range(n):
    s=int(input("輸入分數"))
    score.append(s)
for d in range(n):
    total=total+score[d]
print ('the total is ',total)
print ('the avg is ',total/n)  
 