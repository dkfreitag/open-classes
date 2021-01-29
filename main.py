#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:04:23 2020

@author: davidfreitag
"""

import open_classes
import time
from datetime import datetime  
from datetime import timedelta  

def find_open_classes(c_num, c_sub):
    browser_instance = open_classes.initiate_browser()
    open_classes.login_to_CUNYfirst(browser_instance)
    open_classes.navigate_to_class(c_num, c_sub, browser_instance)
    open_classes.check_for_open_sections(c_num, c_sub, browser_instance)
    

while 1:
#    find_open_classes('9490', 'CIS - Computer Information Sys')
    find_open_classes('9708', 'STA - Statistics')
    print('\nCurrent time is: ' + str(datetime.now()))
    print('Checking for classes again at: ' + str(datetime.now() + timedelta(seconds=300)) + '\n')
    time.sleep(300)
