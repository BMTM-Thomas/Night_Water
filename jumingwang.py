import time
import pyautogui
import sys
import pymongo
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from List_Zentao import ID, mongodb_id  
from PIL import ImageGrab
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
    jumingwang(driver)
    driver.quit()

def wait(driver, path, text):
    try:
        WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# 聚名網
def jumingwang(driver):
    id = 107

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
            # Logout
            logout = pyautogui.locateOnScreen('./image/juminglogout.png')
            logout2 = pyautogui.locateOnScreen('./image/juminglogout2.png')
            if logout is not None:
                pyautogui.click(logout)
                time.sleep(2)
            else:
                pyautogui.click(logout2)
                time.sleep(2)

            id+=1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

if __name__ == "__main__":
    main()
