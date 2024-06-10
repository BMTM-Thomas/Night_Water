import time
import pyautogui
import sys
import cv2
import re
import numpy as np
import pymongo
import pyperclip
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from List_Zentao import ID, mongodb_id, tuple_id  
from PIL import ImageGrab, Image
from bson.objectid import ObjectId  

# Connect to the MongoDB server running on localhost at default port 27017
client = pymongo.MongoClient("mongodb://localhost:27017")
# Access Database
db = client["Thomas"]
# Access Collection
collection = db["Night_Database"]

def main():
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
    options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--hide-crash-restore-bubble")
    driver=webdriver.Chrome(options=options)
    gname(driver)
    jumingwang(driver)
    sms326(driver)
    ven196_7211(driver)
    ven295(driver)
    driver.quit()

def wait(driver, path, text):
    try:
        WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# Wait for a webpage fully load, then only continue steps
def wait_for_page_load(driver):
    return driver.execute_script("return document.readyState") == "complete"

# Gname
def gname(driver):
    
    id = tuple_id[11]
    
    try:
        # Go to Webpage
        driver.get('https://www.gname.com/login?refer=https%3A%2F%2Fwww.gname.com%2Fuser')
        with pyautogui.hold('command'):
            pyautogui.press('r')

            time.sleep(3)
            
        if pyautogui.locateOnScreen('./image/bestdomain.png') is not None:
            pyautogui.click(x=387, y=150)
            time.sleep(1)
            pyautogui.click(x=381, y=177)
            time.sleep(1)

        for i in range(2):
            wait(driver, '/html/body/div[2]/div/div[2]/p[2]', '欢迎来到GNAME，请登录！') 
            pyautogui.click(x=1416, y=62)
            time.sleep(1)  
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1202, y=180)
            time.sleep(1)
            
            if i == 0:
                wait(driver, '/html/body/div[1]/div/div[4]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/span', '基本信息') 
                wait(driver, '/html/body/div[1]/div/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/span', '资金信息') 
            elif i == 1:
                wait(driver, '/html/body/div[1]/div/div[4]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/span', 'Basic Information') 
                wait(driver, '/html/body/div[1]/div/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/span', 'Financial Information') 
                time.sleep(1)
                pyautogui.click(1002,324)

            time.sleep(1)
            
            # Extract Credit
            credit = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[3]/strong').get_attribute('textContent')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            collection.update_one(mangos_id, {"$set": {"Credit": credit}})
            print(f"{ID[id]}= {credit}")

            time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            time.sleep(1)
            pyautogui.moveTo(x=1540, y=142)
            time.sleep(1)
            pyautogui.click(x=1531, y=374)
            time.sleep(1)

            id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

# 聚名網
def jumingwang(driver):
    id = tuple_id[12]

    time.sleep(1)
    driver.get('https://www.juming.com/')
    time.sleep(1)

    try:
        for i in range (2):
            
            pyautogui.click(212, 138)
            time.sleep(1)
            pyautogui.click(1416, 62)
            time.sleep(1)
            pyperclip.copy(ID[id])
            pyautogui.hotkey("command", "v")
            time.sleep(1)
            pyautogui.click(1216, 175)
            time.sleep(1)
            pyautogui.moveTo(803, 489, 0.2)
            pyautogui.dragTo(1116, 489, button='left', duration=0.2)

            wait(driver, '/html/body/div[1]/div[1]/div/div/div/span[13]/a', '退出') 

            # Extract Credit
            credit = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div/div/div/span[7]/a').get_attribute('textContent')
            time.sleep(1)

            # Replace
            credit = credit.replace('￥', '')
            credit = credit.replace(',', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            collection.update_one(mangos_id, {"$set": {"Credit": credit}})
            print(f"{ID[id]}= {credit}")

            time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

            # Button Click Logout
            save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "退出")))
            save_button.click()
            time.sleep(3)

            wait(driver, '/html/body/div[1]/div[1]/div/div/span/a[2]', '新用户注册') 
            time.sleep(1)

            id+=1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

# sms326
def sms326(driver):
    id = tuple_id[13]

    driver.get('https://www.google.com')
    time.sleep(1)

    try:
            pyautogui.click(x=1416, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(1)
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1227, y=157)
            time.sleep(1)
            pyautogui.moveTo(1082,164)
            time.sleep(1)
            
            if pyautogui.locateOnScreen('./image/sms_login.png') is None:
                image_vault = None
                while image_vault is None:
                    image_vault = pyautogui.locateOnScreen('./image/newsms.png', grayscale = True)
                    time.sleep(2)
                pass
            elif pyautogui.locateOnScreen('./image/newsms.png') is None:
                time.sleep(4)
                pass
            
            # Zoom up
            for i in range(4):
                pyautogui.hotkey('command', '+')

            time.sleep(1)

            # Custom_Screenshot using cv2, due to imagegrab have some bug during screenshort
            # The first x,y use check_corrdinates tool to find the top-left coordinates
            # Weight & Height need to test and adjust by yourself
            x, y, width, height = 232,144,150,60
            custom_screenshot = cv2.cvtColor(np.array(pyautogui.screenshot(region=(x, y, width, height))), cv2.COLOR_RGB2BGR)
            cv2.imwrite(('./晚班水位/' + ID[id] + '.png'), custom_screenshot)

            # Tesseract Image Extract value
            # Load Image
            img = cv2.imread("./晚班水位/ven326.png")
            # Convert Image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Apply threshold to convert to binary image
            threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            # Pass the image through pytesseract
            # Extract the value from image
            credit = pytesseract.image_to_string(threshold_img)

            # Replace
            credit = credit.replace('$', '')
            credit = credit.replace('\n', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            collection.update_one(mangos_id, {"$set": {"Credit": credit}})
            print(f"{ID[id]}= {credit}")

            time.sleep(1)
            pyautogui.hotkey('command', '0')
            time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

            id+=1
            
            time.sleep(1)
            pyautogui.click(547,19)
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

# 7211.com ven196
def ven196_7211(driver):
    id = tuple_id[14]

    driver.get('https://www.7211.com/login.php')
    wait(driver, '/html/body/div[2]/div/div/div[1]/div[1]/div/h2', '请先登录再下单！') 
    time.sleep(1)
    pyautogui.click(387,641)
    time.sleep(1)
    wait(driver, '/html/body/div[2]/div/div[1]/div/div[1]/div[1]/h2', '购买一个') 
    time.sleep(1)

    try:
        pyautogui.moveTo(859,139)
        time.sleep(1)
        pyautogui.click(823,168)
        time.sleep(1)
        wait(driver, '/html/body/div[3]/table/tbody/tr/td[1]/div/div/div[1]/div[1]/strong', '快速链接') 
        time.sleep(1)
        pyautogui.click(65,383)
        time.sleep(1)

        # Extract Credit
        credit = driver.find_element(By.XPATH, value='/html/body/div[3]/table/tbody/tr[2]/td/font/b[2]/font').get_attribute('textContent')
        time.sleep(1)

        # Replace
        credit = credit.replace('CNY ', '')
        credit = credit.replace('\n', '')
        credit = credit.replace(' ', '')
        
        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        collection.update_one(mangos_id, {"$set": {"Credit": credit}})
        print(f"{ID[id]}= {credit}")

        time.sleep(1)
        
        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

        time.sleep(1)
        pyautogui.click(1554,226)
        time.sleep(1)
        pyautogui.click(1496,346)
        time.sleep(1)

        id+=1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

# ven295
def ven295(driver):
    
    id = tuple_id[15]

    try:
        driver.get('https://intl.cloud.tencent.com/zh/account/login?s_url=https%3A%2F%2Fconsole.intl.cloud.tencent.com%2Fexpense%2Frmc%2Faccountinfo')
        time.sleep(1)

        wait(driver, '/html/body/div/main/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]', '邮箱登录') 
        time.sleep(1)        
        pyautogui.click(x=1416, y=62) 

        # Wait for image Appear
        image_vault = None
        while image_vault is None:
            image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

        time.sleep(1)
        pyautogui.write(ID[id])
        time.sleep(1)
        pyautogui.click(x=1260, y=170)
        time.sleep(1)
        pyautogui.click(x=313, y=484)
        time.sleep(2)

        wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[1]/h3', '可用额度') 
        time.sleep(2)
        
        # Extract Credit                                            
        credit = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div').get_attribute('textContent') 
        print(f"{ID[id]}= {credit}")

        # Replace
        credit = credit.replace(',', '')
        credit = re.sub(r'USD.*', 'USD', credit)
        credit = credit.replace('USD', '')
        
        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        collection.update_one(mangos_id, {"$set": {"Credit": credit}})

        time.sleep(1)
        pyautogui.click(x= 1558, y=135)
        pyautogui.click(x= 1558, y=135)
        time.sleep(1)
        
        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        time.sleep(1)
        logout = pyautogui.locateOnScreen('./image/tencentlogout1.png')
        if logout is not None:
            time.sleep(1)
            pyautogui.click(logout)
        else:
            pyautogui.click(x=1458, y=506)
                
        time.sleep(2)
        
        id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
