# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:21:31 2020

@author: prati
"""

s = "12:06:30AM"

s = s.split(":")

if s[2][-2:] == "AM" and s[0] == '12':
    s[0] = 0
if int(s[0]) < 12 and int(s[0]) > 0 and s[2][-2:] == "PM":
    s[0] = int(s[0]) +12
if s[2][-2:] == "AM" and int(s[0]) < 10:
    s[0] = s[0]

s[0] = str(s[0]).zfill(2)
k = []
for i in s:
    k.append(i[:2])

p = ":".join(k)
print(p)