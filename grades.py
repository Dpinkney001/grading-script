# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:11:17 2021

@author: thees
"""



def grades():
    finalgrade = 0
    
    homework = 49
    test1 = 80
    test2 = 75
    midtermproject  = 85
    finalproject = 85
    print("homework grade:", homework)
    
    print("test1 grade:",test1)
    
    print("test2 grade:", test2)
    
    print("midtermptoject grade:", midtermproject)
    
    print("finalproject grade:",finalproject)
    
    finalgrade = (0.20 * homework) + (0.10 * test1) + (0.10 * test2) + (0.30 * midtermproject) + (0.30 * finalproject)

    print(finalgrade)

def main():
    grades()
    
    
main()    
    