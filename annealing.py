#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 20:25:58 2018

@author: demilangston
"""

import random
import numpy
import math

new_state = float
bef_state = float
fin_state = float
count = 0
T = 10
Coolrate = 0.01

x1=-10
x2=-10

curr_state = ((-1) * (abs(math.sin(x1) * math.cos(x2) * math.exp(abs(1 - math.sqrt(math.pow(x1, 2) 
                                      + math.pow(x2, 2)) / math.pi)))))
  
#init_state = fin_state

while x1 <= 10:
    x2 = -10
    while x2 <= 10:
        new_state = ((-1) * (abs(math.sin(x1) * math.cos(x2) * 
                         math.exp(abs(1 - math.sqrt(math.pow(x1, 2) 
                         + math.pow(x2, 2)) / math.pi)))))
        if new_state < curr_state :
             bef_state = curr_state
             curr_state = new_state
             fin_state = new_state
        x2 = x2 + 1
    x1 = x1 + 1
print("nilai x1 = " ,x1)
print("nilai x2 = " ,x2)        
print("hasil SA = " ,curr_state)
                    
                    
            
    