import time
import certifi
import pyautogui
import sys
import pymongo 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from List_Zentao import ID, Huawei_Webpage, mongodb_id, tuple_id
from PIL import ImageGrab
from bson.objectid import ObjectId   
from pymongo import MongoClient  
  
# Local Server
# # Connect to the MongoDB Local server running on localhost at default port 27017
# client = pymongo.MongoClient("mongodb://localhost:27017")
# # Access Database
# db = client["Thomas"]
# # Access Collection
# collection = db["Night_Database"]

# MongoDB Atlas (Server)
client = MongoClient("mongodb+srv://thomasleong:8zvnWrT3sf8N2u7x@cluster0.ef0wowh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",tlsCAFile=certifi.where())
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
    options.add_argument("--hide-crash-restore-bubble")
    options.add_experimental_option('useAutomationExtension', False)
    driver=webdriver.Chrome(options=options)
    huawei1(driver)
    huawei2(driver)
    driver.quit()

def wait(driver, path, text):
    try:
        WebDriverWait(driver, 1000).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

def wait2(driver, path, text):
    try:
        WebDriverWait(driver, 1).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# 华为云【OPSADMIN】【IAM用户登录】
def huawei1(driver):

    id = tuple_id[8]
    i = 0
    
    try:
        for i in range(14):
            # # Go to Webpage
            driver.get(Huawei_Webpage[i])
            with pyautogui.hold('command'):
                pyautogui.press('r')
                time.sleep(1)

            wait(driver, '/html/body/div[3]/div/div[2]/div[2]/div[1]/span', 'IAM用户登录') 
            time.sleep(1)
            pyautogui.click(x=1416, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(1)
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x= 1241, y=169)
            time.sleep(1)
            pyautogui.click(x= 1186, y=604)
            time.sleep(1)

            # for ven399 purpose
            if i == 7:
                wait(driver, '/html/body/div[3]/div/div[1]/div[1]/p', '登录验证') 
                time.sleep(3)
                pyautogui.click(x= 932, y=512)
                time.sleep(1)

            wait(driver, '/html/body/div[1]/div/div[2]/div/div[2]/div[5]/a/span[2]', 'Intl-简体')
            time.sleep(2)
            driver.get('https://account-intl.huaweicloud.com/usercenter/#/userindex/allview')
            wait(driver, '/html/body/div[3]/cbcusercenterwebsite-master-root/cbcusercenterwebsite-layout-default/div/div[1]/div/cbcsubexpense-root/cbcsubexpense-allview-menu/cbcsubexpense-allview-hk/tp-layout-content/div/tp-layout-column[1]/tp-layout-content-body[1]/tp-layout-section/div/cbcsubexpense-partner-budget/div[1]/span', '本月剩余预算') 
            if i <= 8:
                wait(driver, '/html/body/div[3]/cbcusercenterwebsite-master-root/cbcusercenterwebsite-layout-default/div/div[1]/div/cbcsubexpense-root/div/cbcsubexpense-allview-menu/cbcsubexpense-allview-hk/tp-layout-content/div/tp-layout-column[1]/tp-layout-content-body[1]/tp-layout-section/div[1]/cbcsubexpense-partner-budget/div[2]/div[2]/span[1]', '合作伙伴为您设置的月度预算是:') 
            else:
                wait(driver, '/html/body/div[3]/cbcusercenterwebsite-master-root/cbcusercenterwebsite-layout-default/div/div[1]/div/cbcsubexpense-root/div/cbcsubexpense-allview-menu/cbcsubexpense-allview-hk/tp-layout-content/div/tp-layout-column[1]/tp-layout-content-body[1]/tp-layout-section/div[1]/cbcsubexpense-partner-budget/div[2]/div[2]/span[1]', '合作伙伴为您设置的一次性预算是:')
                
            # Extract Credit   
            credit = driver.find_element(By.XPATH, value='/html/body/div[3]/cbcusercenterwebsite-master-root/cbcusercenterwebsite-layout-default/div/div[1]/div/cbcsubexpense-root/cbcsubexpense-allview-menu/cbcsubexpense-allview-hk/tp-layout-content/div/tp-layout-column[1]/tp-layout-content-body[1]/tp-layout-section/div/cbcsubexpense-partner-budget/div[2]/div[1]/span').get_attribute('textContent') 

            # Replace
            credit = credit.replace(',', '')
            credit = credit.replace(' $', '')
            credit = credit.replace(' USD ', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            collection.update_one(mangos_id, {"$set": {"Credit": credit}})
            print(f"{ID[id]}= {credit}")

            time.sleep(1)

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            try:
                if driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/span[2]').get_attribute('textContent') == "您尚未开启敏感操作保护，存在安全风险，请您前往 安全设置>敏感操作>操作保护 开启敏感操作保护。":
                    pyautogui.click(1574, 142)
                else:
                    pyautogui.moveTo(1540, 138)
            except:
                pyautogui.moveTo(1540, 138)

            time.sleep(1)
            
            # Logout
            logout4 = pyautogui.locateOnScreen('./image/huaweilogout4.png')
            if logout4 is not None:
                pyautogui.click(logout4)
            else:
                pyautogui.click(x= 1486, y=398)

            id += 1
            i += 1
        
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(111111)

# 华为云 【华为帐号登录】
def huawei2(driver):
    
    id = tuple_id[9]
    
    try:
        # Go to Webpage
        driver.get('https://auth.huaweicloud.com/authui/login.html?service=https://account-intl.huaweicloud.com/usercenter/#/login')
        with pyautogui.hold('command'):
            pyautogui.press('r')

        time.sleep(3)

        # If is English, Change to Chinese
        chinese = pyautogui.locateOnScreen('./image/chinese2.png')
        if chinese is None:
            pyautogui.moveTo(x= 1515, y=133)
            time.sleep(1)
            pyautogui.click(x= 1517, y=181)
            time.sleep(1)
            wait(driver, '/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/span/span', '华为帐号登录') 
            time.sleep(1)
        else:
            pass
        
        for i in range(6):
            
            wait(driver, '/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/span/span', '华为帐号登录') 
            time.sleep(1)
            pyautogui.click(x=1416, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(1)
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x= 1226, y=170)
            time.sleep(1)
            pyautogui.click(x= 1189, y=527)
            time.sleep(1)
            if i >= 4:
                wait(driver, '/html/body/div[3]/cbcusercenterwebsite-master-root/cbcusercenterwebsite-layout-default/div/div[1]/div/cbcsubexpense-root/cbcsubexpense-allview-menu/cbcsubexpense-allview-hk/tp-layout-content/div/tp-layout-column[1]/tp-layout-content-body[1]/tp-layout-section/div/cbcsubexpense-partner-budget/div[2]/div[2]/span[1]', '合作伙伴为您设置的一次性预算是:') 
            else:
                wait(driver, '/html/body/div[3]/cbcusercenterwebsite-master-root/cbcusercenterwebsite-layout-default/div/div[1]/div/cbcsubexpense-root/cbcsubexpense-allview-menu/cbcsubexpense-allview-hk/tp-layout-content/div/tp-layout-column[1]/tp-layout-content-body[1]/tp-layout-section/div/cbcsubexpense-partner-budget/div[2]/div[2]/span[1]', '合作伙伴为您设置的月度预算是:') 
            time.sleep(1)

            # Extract Credit
            credit = driver.find_element(By.XPATH, value='/html/body/div[3]/cbcusercenterwebsite-master-root/cbcusercenterwebsite-layout-default/div/div[1]/div/cbcsubexpense-root/cbcsubexpense-allview-menu/cbcsubexpense-allview-hk/tp-layout-content/div/tp-layout-column[1]/tp-layout-content-body[1]/tp-layout-section/div/cbcsubexpense-partner-budget/div[2]/div[1]/span').get_attribute('textContent')

            # Replace
            credit = credit.replace(',', '')
            credit = credit.replace(' $', '')
            credit = credit.replace(' USD ', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            collection.update_one(mangos_id, {"$set": {"Credit": credit}})
            print(f"{ID[id]}= {credit}")

            time.sleep(1)

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            security = pyautogui.locateOnScreen('./image/huaweisecurity.png')
            if security is not None:
                pyautogui.moveTo(x= 1485, y=171)
            else:
                pyautogui.moveTo(x= 1540, y=140)
                
            time.sleep(1)

            logout2 = pyautogui.locateOnScreen('./image/huaweilogout2.png')
            if logout2 is not None:
                pyautogui.click(logout2)
            else:
                pyautogui.click(x= 1484, y=400)

            time.sleep(1)

            id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

if __name__ == "__main__":
    main()