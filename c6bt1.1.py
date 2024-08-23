# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:40:03 2024

@author: Phan Le Quynh 23720041
"""

s = "Dai hoc quoc gia, Khu pho 6, P.Linh Trung, Q. Thu Duc, Tp. HCM"
s1=s.split(",")
for i in s1:
    print(i)
s2=s.replace('P.','').replace('Q.','').replace('Tp.','').split(",")
for u in s2:
    print(u)