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

# Setups Selenium WebDriver
def driver_setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome(options = options)
    return driver

# function to log into Central Square & Oracle and search permits
def login(url, driver, usr, pwd):
    driver.get(url)
    driver.maximize_window()
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='txtAdminUserName']"))
            ).send_keys(usr)
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='txtAdminPassword']"))
            ).send_keys(pwd)
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='btnAdminLogin']"))
            ).click()
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'General')]"))
            ).click()
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, "//td[@id='UltraWebTab1td4']"))
            ).click()
    WebDriverWait(driver, '45').until(
            EC.presence_of_element_located((By.XPATH, "(//a[contains(text(),'View List')])[2]"))
            ).click()
    df = pd.DataFrame(columns=["Username", "Name", "Company", "Email"])
    pagecounter = 1
    run = True
    while run:
        try:
            for i in range(20):
                try:
                    username = ""
                    if i == 0:
                        username = WebDriverWait(driver, '10').until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, "#gvETRAKITUsers tr:nth-child(" + str(i + 2) + ") > td:nth-child(1)"))
                                ).text
                    else:
                        username = WebDriverWait(driver, '10').until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, "tr:nth-child(" + str(i + 2) + ") > td:nth-child(1)"))
                                ).text
                    name = WebDriverWait(driver, '10').until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "tr:nth-child(" + str(i + 2) + ") > td:nth-child(2)"))
                            ).text
                    company = WebDriverWait(driver, '10').until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "tr:nth-child(" + str(i + 2) + ") > td:nth-child(3)"))
                            ).text
                    email = WebDriverWait(driver, '10').until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "tr:nth-child(" + str(i + 2) + ") > td:nth-child(4)"))
                            ).text
                    df2 = pd.DataFrame([[username, name, company, email]],columns=["Username", "Name", "Company", "Email"])
                    df = df.append(df2,ignore_index=True)
                except TimeoutException:
                    run = False
                    df.to_csv("C:/Users/amadeo.rosario/Downloads/Contractor_Users.csv", index=False, header=True)
            nextpage = driver.find_element(By.XPATH, "//a[contains(text(),'" + str(pagecounter + 1) + "')]")
            nextpage.click()
            pagecounter += 1
        except NoSuchElementException:
            threedots = driver.find_elements(By.XPATH, "//a[contains(text(),'...')]")
            threedots[-1].click()
            pagecounter +=1
            
