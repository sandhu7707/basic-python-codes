# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:25:47 2018
this is demo program to find combination of objects amounting to given sum
@author: Sandhu
"""
import random as r
x={"p1":4,"p2":1,"p3":7,"p4":6,"p5":9,"p6":3,"p7":2,"p8":8,"p9":5,"p10":2}

s=3 #s is no. of objects in combo
reqsum=10


noi=int(input("no. of iterations: "))
for j in range(0,noi):    
    y=r.sample(x.keys(),s)
    z=0
    for i in range(0,s):
        z=x[y[i]]+z
    if z==reqsum:
        print(y)
