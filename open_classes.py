#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:05:54 2020

@author: davidfreitag
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

# Make this a headless browser instance
options = Options()
options.headless = True

def initiate_browser():
    # Initiate the browser
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
    # Open the Website
    browser.get('https://home.cunyfirst.cuny.edu/')
    print('Running...')
    return browser

def login_to_CUNYfirst(browser):
    print ('Logging in...')

    # Type in the username and password
    elem = browser.find_element_by_id('CUNYfirstUsernameH') #identify the element
    elem.clear() #clear any text in the field
    elem.send_keys('') #type the username

    elem = browser.find_element_by_id('CUNYfirstPassword')
    elem.clear()
    elem.send_keys('')

    # Submit username and password
    elem = browser.find_element_by_id('submit')
    elem.click()
    print ('Logged in.')

def navigate_to_class(course_number, subject, browser):
    print('Navigating...')
    print('Searching for open sections of ' + subject + ' ' + course_number + '.')
    
    # Click on "Student Center"
    elem = browser.find_element_by_id('crefli_HC_SSS_STUDENT_CENTER')
    elem.click()

    # Wait to ensure the page has loaded
    time.sleep(5)

    # Switch to the iframe
    frame = browser.find_element_by_id('ptifrmtgtframe')
    browser.switch_to.frame(frame)

    # Click on Search
    elem = browser.find_element_by_id('DERIVED_SSS_SCR_SSS_LINK_ANCHOR1')
    elem.click()

    # Wait to ensure the page has loaded
    time.sleep(5)

    # Select the Institution
    elem = Select(browser.find_element_by_id('CLASS_SRCH_WRK2_INSTITUTION$31$'))
    elem.select_by_visible_text('Baruch College')

    # Wait to ensure the choice is populated
    time.sleep(5)

    # Select CIS
    elem = Select(browser.find_element_by_id('SSR_CLSRCH_WRK_SUBJECT_SRCH$0'))
    elem.select_by_visible_text(subject)

    # Input the course number
    elem = browser.find_element_by_id('SSR_CLSRCH_WRK_CATALOG_NBR$1')
    elem.send_keys(course_number)

    # Click Search
    elem = browser.find_element_by_id('CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH')
    elem.click()

    # Wait to ensure the page has loaded
    time.sleep(5)

def check_for_open_sections(course_number, subject, browser):
    # Are there any open sections?
    try:
        elem = browser.find_element_by_id('win0divDERIVED_CLSMSG_ERROR_TEXT')
        print('No open class sections of ' + subject + ' ' + course_number + '.')
        browser.quit()
    except:
        print('Open section of ' + subject + ' ' + course_number + ' found!')
        browser.quit()
        send_text_message(course_number, subject)
        
def send_text_message(course_number, subject):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body='There\'s a section of ' + subject + ' ' + course_number + ' open!',
                     from_='',
                     to=''
                 )
    print('Text message sent.')

""" 
    browser2 = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser2.get('https://www.opentextingonline.com/')
    
    # Type in the phone number
    elem = browser2.find_element_by_id('phone') #identify the element
    elem.clear() #clear any text in the field
    elem.send_keys('') #type the username
    
    # Type in the message
    elem = browser2.find_element_by_id('tmessage') #identify the element
    elem.clear() #clear any text in the field
    elem.send_keys('There\'s a section of ' + subject + ' ' + course_number + ' open!') 
    
    # Click the Send Message button
    elem = browser2.find_element_by_id('btsend')
    elem.click()
    print('Text message sent.')

    # Quit the program
    time.sleep(5)
    browser2.quit()
"""
