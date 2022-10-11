from gettext import find
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException, ElementNotInteractableException
from datetime import datetime as dt
import zipfile
import shutil
import re
import math
import os
import time
import pandas as pd
import csv
from threading import Thread
import pyautogui as pg

def driver_setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome(options = options)
    return driver

def login(url, driver, trakit_user, trakit_pass):
    print("logging in to Trakit....")
    driver.get(url)
    driver.maximize_window()
    

    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='txtAdminUserName']"))
            ).send_keys(trakit_user)
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='txtAdminPassword']"))
            ).send_keys(trakit_pass)
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='btnAdminLogin']"))
            ).click()

    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ucSideBar_HlGeneralPrefs"]'))
            ).click()
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="UltraWebTab1td3"]'))
            ).click()
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="UltraWebTab1__ctl3_HlViewUserList"]'))
            ).click()


    
    
    


