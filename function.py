import certifi                                                                                  
import time                                                                                            
import pyautogui                                                                                       
import re                                                                                              
import sys                                                                                            
from selenium import webdriver                                                                        
from selenium.webdriver.common.by import By                                                            
from selenium.webdriver.support.wait import WebDriverWait                                              
from selenium.webdriver.support import expected_conditions as EC                                       
from selenium.webdriver.chrome.options import Options                                                  
from List_Zentao import ID, mongodb_id,tuple_id                                                       
from List_Aliyun_DDCaptcha import m_X1,m_Y2,d_X1,d_Y2,ram_d_X1,ram_d_Y2,ram_m_X1,ram_m_Y2              
from PIL import ImageGrab, Image    
from bson.objectid import ObjectId   
from pymongo import MongoClient                                                                  

def mongodb_atlas():
    # MongoDB Atlas (Server)
    client = MongoClient("mongodb+srv://thomasleong:8zvnWrT3sf8N2u7x@cluster0.ef0wowh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",tlsCAFile=certifi.where())
    # Access Database
    db = client["Thomas"]
    # Access Collection
    collection = db["Night_Database"]
    return collection

# MongoDB Update Documnent
def update_one(filter, update):
    # update one data
    collection = mongodb_atlas()
    collection.update_one(filter, {"$set": {"Credit": update}})

# Selenium Chrome
def chrome():
    options=Options()
    options.add_argument('--user-data-dir=\\Users\\n02-19\\Library\\Application Support\\Google\\Chrome\\')
    options.add_argument('profile-directory=Default')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized') 
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--hide-crash-restore-bubble")
    options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    driver=webdriver.Chrome(options=options)
    return driver

# wait
def wait(driver, path, text):
    try:
        WebDriverWait(driver, 1000).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# Extract data / driver get_element by xpath
# With Text
def find_element_text(driver, path, text):
    mongodb_atlas()
    element = driver.find_element(By.XPATH, path)
    element_text = element.get_attribute('textContent')
    return element_text == text

# Extract data / driver get_element by xpath
# Without-Text
def find_element_nontext(driver, path):
    element = driver.find_element(By.XPATH, path)
    return element.get_attribute('textContent')