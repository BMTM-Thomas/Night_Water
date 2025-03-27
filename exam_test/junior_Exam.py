import pyautogui       
import time                                                                                                                                                                                                                                                                             
import sys     
import cv2
import re                                                                                                                                                     
from selenium import webdriver     
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.keys import Keys                                       
from selenium.webdriver.common.by import By                                                            
from selenium.webdriver.support.wait import WebDriverWait                                              
from selenium.webdriver.support import expected_conditions as EC  
from webdriver_manager.chrome import ChromeDriverManager     
from PIL import ImageGrab  
from bson.objectid import ObjectId       
                                                                                                                                                   

# Selenium Chrome   
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument("--user-data-dir=\\Users\\Thomas\\Library\\Application Support\\Google\\Chrome\\")
options.add_argument('profile-directory=Profile 4')
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

# go to a website
driver.get("https://www.saucedemo.com/")

# Username
username_field = driver.find_element(By.XPATH, "//input[@id='user-name']") 
username_field.send_keys("standard_user")

time.sleep(1)

# Password
password_field = driver.find_element(By.XPATH, "//input[@id='password']")  
password_field.send_keys("secret_sauce", Keys.RETURN) 

try: 
    invalid_login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
    if invalid_login.text == "Epic sadface: Username and password do not match any user in this service":
    
        # Capture
        ImageGrab.grab().save('./exam_test/invalid_login.png')
        
        print(invalid_login.text)
        print(f"invalid_user")
        print(f"invalid_password")
except:
    pass

    
print("hahaa")
WebDriverWait(driver, 1000).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/div"), "Swag Labs"))

time.sleep(1)

x=1
for item in range(6):
    
    product_Name = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div/div/div/div[{x}]/div[2]/div[1]/a/div")
    product_Description = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div/div/div/div[{x}]/div[2]/div[1]/div")
    product_Price = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div/div/div/div[{x}]/div[2]/div[2]/div")

    
    print(product_Name.text + "\n" + product_Description.text + "\n" + product_Price.text +"\n\n")
    
    x+=1

time.sleep(1)
three_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")))
three_menu.click()

time.sleep(1)
logout= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]")))
logout.click()

time.sleep(2)
driver.close()


