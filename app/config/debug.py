# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:27:07 2022

@author: MME
"""

DEBUG = True


def log(module, func,  message, variable=None ):
    
    if DEBUG:
        print ('\n***************************************************************************************************************')
        print ('[DEBUG]==>', 'Module :','[', module,'],', 'Function :', '[', func, '],',  'message :', '[', message ,']' )
        if variable is not None:
         print ('[DEBUG]==> variable :', '[', variable ,']' )     
        print ('***************************************************************************************************************\n')
            
