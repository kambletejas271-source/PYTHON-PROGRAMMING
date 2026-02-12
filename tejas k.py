# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 10:37:22 2026

@author: User
"""

n = int(input("enter number:"))
fact = 1
for i in range (1 , n+1):
    fact = fact*i
    print("factorial:", fact)