import certifi               
import pytest                                                                                                                                                          
from selenium import webdriver     
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager                                                                   
from selenium.webdriver.common.by import By                                                            
from selenium.webdriver.support.wait import WebDriverWait                                              
from selenium.webdriver.support import expected_conditions as EC                                                                                                                                                          
from pymongo import MongoClient                                                                  

# Serverless
def mongodb_atlas():
    # MongoDB Atlas (Server)
    client = MongoClient("mongodb+srv://thomasleong:8zvnWrT3sf8N2u7x@cluster0.ef0wowh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",tlsCAFile=certifi.where())
    # Access Database
    db = client["Thomas"]
    # Access Collection
    collection = db["Night_Database"]
    return collection

# Selenium Chrome   
def chrome():

    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=\\Users\\Thomas\\Library\\Application Support\\Google\\Chrome\\")
    options.add_argument('profile-directory=Profile 3')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized') 
    options.add_argument('--no-default-browser-check')
    options.add_argument('--no-first-run')
    options.add_argument('--hide-crash-restore-bubble')
    options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    # return vs yield, why use yield?
    # return ❌ Stops execution completely! `driver.quit()` will never run.
    # yield ✅ Execution pauses here; `driver` is provided to the test.
    # yield, use send() and next() to continue the execution
    yield driver  

    driver.quit()

# MongoDB Update one Document / Credit
def update_one(filter, update):
    # update one data
    collection = mongodb_atlas()
    collection.update_one(filter, {"$set": {"Credit": update}})
    
# MongoDB Find One Document
def find_one(find):
    # Find one data 
    collection = mongodb_atlas()
    document = collection.find_one(find)
    return document

# Extract data / driver get_element by xpath
# Text
def find_element_text(driver, path):
    return driver.find_element(By.XPATH, path).text

# Without Text
def find_element_nontext2(driver, path):
    return driver.find_element(By.XPATH, path)

# driver find element by ID
def find_element_ID(driver, path):
    return driver.find_element(By.ID, path).text

# wait (wait for element appear)
def wait(driver, path):
    try:
        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, path)))
    except:
        pass

# wait2 (wait for text appear)
def wait2(driver, path, text):
    try:
        WebDriverWait(driver, 1000).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# wait for button click by LINK
def wait_buttonclick_LINK(driver, text): 
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, text)))
    return driver.find_element(By.LINK_TEXT, text)

# wait by ID
def waitID(driver, waitid):
    try:
        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, waitid)))
    except:
        pass

# wait for button click by XPATH
def wait_buttonclick_XPATH(driver, text): 
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, text)))
    return driver.find_element(By.XPATH, text)

# Wait for a webpage fully load, then only continue steps
def wait_for_page_load(driver):
    return driver.execute_script("return document.readyState") == "complete"

