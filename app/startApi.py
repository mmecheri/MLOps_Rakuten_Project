# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:16:10 2022

@author: MME
"""
import uvicorn
from config.debug import log

module_name =  'StartApi'



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000 ,reload=True)
    