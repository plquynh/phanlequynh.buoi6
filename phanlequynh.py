# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:32:21 2024

@author: PhanLeQuynh
"""

chuoi="im a cat"

#Viết hoa chữ đầu

titlechuoi=chuoi.title()

print(titlechuoi)

#Viết hoa hết

upperchuoi=chuoi.upper()

print(upperchuoi)

#Viết thường

lowerchuoi=chuoi.lower()

print(lowerchuoi)

#Viết hoa chữ cuối

words=chuoi.split()

words=[word[:-1]+word[-1].upper() if len(word)>0 else word for word in words]

ketqua=" ".join(words)

print(f"{ketqua}")
