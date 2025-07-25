import time
import pyautogui
import sys
import cv2
import re
import numpy as np
import pyperclip
import pytesseract
from List_Zentao import ID, mongodb_id, tuple_id  
from PIL import ImageGrab, Image
from bson.objectid import ObjectId
from function import *

# Gname
def gname(driver):
    
    id = tuple_id[11]
    id_Range = tuple_id[12] - tuple_id[11]
    
    try:
        # Go to Webpage
        driver.get('https://www.gname.com/login?refer=https%3A%2F%2Fwww.gname.com%2Fuser')

        time.sleep(2)

        if pyautogui.locateOnScreen('./image/bestdomain.png') is not None:
            pyautogui.moveTo(x=382, y=122)
            time.sleep(1)
            pyautogui.click(x=379, y=146)
            time.sleep(1)

        for i in range(id_Range):
            wait(driver, '/html/body/div[2]/div/div[2]/p[2]') 
            pyautogui.click(x=1416, y=62)
            time.sleep(1)  
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1202, y=180)
            time.sleep(1)
            
            pyautogui.moveTo(858, 560, 0.4)
            pyautogui.dragTo(1280, 562, button='left', duration=0.4)

            if i == 0:
                wait(driver, ' /html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/span') 
                wait(driver, '/html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/span') 
            elif i == 1:
                wait(driver, '/html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/span') 
                wait(driver, '/html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/span') 
                time.sleep(1)
                pyautogui.click(1015,323)

            time.sleep(1)
            
            # Extract Credit
            credit = find_element_text(driver, '/html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[1]/strong')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            time.sleep(1)
            pyautogui.moveTo(x=1535, y=109)
            time.sleep(1)
            pyautogui.click(x=1531, y=338)
            time.sleep(1)

            id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

# 聚名網
def jumingwang(driver):

    id = tuple_id[12]
    id_Range = tuple_id[13] - tuple_id[12]

    time.sleep(1)
    driver.get('https://www.juming.com/')
    time.sleep(1)

    try:
        for i in range (id_Range):
            
            # Check if still login, if still login then logout, else button click login 
            try:
                if find_element_text(driver, "/html/body/div[1]/div[1]/div/div/div/span[13]/a") == "退出":
                    save_button = wait_buttonclick_LINK(driver, "退出")
                    save_button.click()
                    wait(driver, '/html/body/div[1]/div[1]/div/div/span/a[1]') 
                    time.sleep(1)
                    pyautogui.click(215,102)

            except Exception as e:
                time.sleep(1)
                pyautogui.click(215,102)

            # wait for 账号登入 image appear
            zhdl = None
            while zhdl is None:
                zhdl = pyautogui.locateOnScreen('./image/zhdl.png', grayscale = True)

            time.sleep(1)
            pyautogui.click(1416, 62)
            time.sleep(1)
            pyperclip.copy(ID[id])
            pyautogui.hotkey("command", "v")
            time.sleep(1)
            pyautogui.click(1216, 175)
            time.sleep(1)
            pyautogui.moveTo(803, 470, 0.2)
            pyautogui.dragTo(1116, 470, button='left', duration=0.2)

            wait(driver, '/html/body/div[1]/div[1]/div/div/div/span[13]/a') 

            # Extract Credit
            credit = find_element_text(driver, '/html/body/div[1]/div[1]/div/div/div/span[7]/a')
            time.sleep(1)

            # Replace
            credit = credit.replace('￥', '')
            credit = credit.replace(',', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

            # Button Click Logout
            save_button = wait_buttonclick_LINK(driver, "退出")
            save_button.click()
            time.sleep(3)

            wait(driver, '/html/body/div[1]/div[1]/div/div/span/a[2]') 
            time.sleep(1)

            id+=1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

# sms326
def sms326(driver):

    id = tuple_id[12]

    driver.get('https://www.google.com')
    time.sleep(1)

    try:
            pyautogui.click(x=1416, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(0.5)
            pyautogui.write(ID[id])
            time.sleep(0.5)
            pyautogui.click(x=1227, y=157)
            time.sleep(0.5)

            wait_for_page_load(driver)

            # Wait for 1. Select a service image appear
            select_Service_img = None
            while select_Service_img is None:
                select_Service_img = pyautogui.locateOnScreen('./image/select_service.png', grayscale = True)

            time.sleep(0.5)

            # Custom_Screenshot using cv2, due to imagegrab have some bug during screenshort
            # How to get x, y, width, height ?
            # First screenshot and save, and copy "wait for image Appear code" and then run code and find the coordinates
            x, y, width, height = 1203,123,80,24
            custom_screenshot = cv2.cvtColor(np.array(pyautogui.screenshot(region=(x, y, width, height))), cv2.COLOR_RGB2BGR)
            cv2.imwrite(('./晚班水位/ven326_tesseract.png'), custom_screenshot)

            time.sleep(1)
            # Tesseract Image Extract value
            # Load Image
            img = Image.open('./晚班水位/' + ID[id] + '_tesseract.png')
            credit = pytesseract.image_to_string(img)

            # Replace
            credit = credit.replace('$', '')
            credit = credit.replace('\n', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")
          
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

            id+=1
            time.sleep(0.5)
            pyautogui.click(547,19)
            time.sleep(0.5)

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

# 7211.com ven196
def ven196_7211(driver):
    
    id = tuple_id[13]

    driver.get('https://www.7211.com/login.php')
    wait(driver, '/html/body/div[2]/div/div/div[1]/div[1]/div/h2') 
    time.sleep(1)
    pyautogui.click(381,604)
    time.sleep(1)
    wait(driver, '/html/body/div[2]/div/div[1]/div/div[1]/div[1]/h2') 
    time.sleep(1)

    try:
        pyautogui.moveTo(852,102)
        time.sleep(1)
        pyautogui.click(820,133)
        time.sleep(1)
        wait(driver, '/html/body/div[3]/table/tbody/tr/td[1]/div/div/div[1]/div[1]/strong') 
        time.sleep(1)
        pyautogui.click(62,350)
        time.sleep(1)

        # Extract Credit
        credit = find_element_text(driver, '/html/body/div[3]/table/tbody/tr[2]/td/font/b[2]/font')
        time.sleep(1)

        # Replace
        credit = credit.replace('CNY ', '')
        credit = credit.replace('\n', '')
        credit = credit.replace(' ', '')
        
        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, credit)
        print(f"{ID[id]}= {credit}")

        time.sleep(1)
        
        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

        time.sleep(1)
        pyautogui.click(1554,190)
        time.sleep(1)
        pyautogui.click(1503,311)
        time.sleep(1)

        id+=1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

# ven295
def ven295(driver):
    
    id = tuple_id[14]

    try:
        driver.get('https://intl.cloud.tencent.com/zh/account/login?s_url=https%3A%2F%2Fconsole.intl.cloud.tencent.com%2Fexpense%2Frmc%2Faccountinfo')
        time.sleep(1)

        wait(driver, '/html/body/div/main/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]') 
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
        pyautogui.click(x=308, y=465)
        time.sleep(2)

        wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[1]/h3') 
        time.sleep(2)
        
        # Extract Credit                                            
        credit = find_element_text(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div')

        # Replace
        credit = credit.replace(',', '')
        credit = re.sub(r'USD.*', 'USD', credit)
        credit = credit.replace('USD', '')
        
        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, credit)
        print(f"{ID[id]}= {credit}")

        time.sleep(1)
        pyautogui.click(x= 1554, y=109)
        pyautogui.click(x= 1554, y=109)
        time.sleep(1)
        
        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        time.sleep(1)
        logout = pyautogui.locateOnScreen('./image/tencentlogout1.png')
        if logout is not None:
            time.sleep(1)
            pyautogui.click(logout)
        else:
            pyautogui.click(x=1470, y=484)
                
        time.sleep(2)
        
        id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# ven467 byteplus
def ven467(driver):
    
    id = tuple_id[15]
    
    try:
        driver.get("https://console.byteplus.com/auth/login/?redirectURI=https%3A%2F%2Fwww.byteplus.com&_gl=1*1ndxskn*_gcl_au*NTI5NTk5LjE3MjM0MzUyNzg.*_ga*NDc5ODkwMTM2LjE3MjM0MzUyNzg.*_ga_3H57BBC3B9*MTcyMzQzNTI3Ny4xLjAuMTcyMzQzNTI3Ny42MC4wLjA")
        time.sleep(2)

        waitID(driver, "volcfe-i18n-header")
        time.sleep(1) 
        driver.get('https://console.byteplus.com/finance/overview')
        time.sleep(1)
        wait(driver, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div[4]/div/p[1]/span') 
        time.sleep(1)

        # Extract Credit
        credit = find_element_text(driver, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[5]/div/p[2]/span[1]')
        credit = credit.replace('$', '')
        credit = credit.replace(',', '')

        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, credit)
        print(f"{ID[id]}= {credit}")

        pyautogui.click(x= 1563, y=149)
        time.sleep(1)
        
        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

driver = chrome()
driver = next(driver)
# gname(driver) 不要用先
sms326(driver)
ven196_7211(driver)
ven295(driver)
ven467(driver)