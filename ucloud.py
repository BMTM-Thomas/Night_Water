import time
import pyautogui
import sys
import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from List_Zentao import ID, mongodb_id, tuple_id 
from PIL import ImageGrab
from bson.objectid import ObjectId  

# # Connect to the MongoDB Local server running on localhost at default port 27017
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
    options.add_argument("--hide-crash-restore-bubble")
    options.add_argument("--no-first-run")
    options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    driver=webdriver.Chrome(options=options)
    ucloud(driver)
    driver.quit()

def wait(driver, path, text):
    try:
        WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# Ucloud
def ucloud(driver):

    id = tuple_id[10]
    
    try:
        # Go to Webpage
        driver.get('https://passport.ucloud.cn/#login')
        with pyautogui.hold('command'):
            pyautogui.press('r')
            time.sleep(1)

        for i in range(3):
            wait(driver, '/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/span', '账号登录') 
            time.sleep(1)
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
            pyautogui.click(x=639, y=599)
            time.sleep(1)

            while True:
                ucloudhelp = pyautogui.locateOnScreen('./image/ucloudhelp.png')
                if ucloudhelp is not None:
                    break
                else:
                    time.sleep(2)
                
            pyautogui.click(x=1558, y=130)
            time.sleep(2)
            
            # Extract Credit
            try:
                credit = driver.find_element(By.XPATH, value='/html/body/div[8]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/span[1]').get_attribute('textContent')
            except:
                credit = driver.find_element(By.XPATH, value='/html/body/div[11]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/span[1]').get_attribute('textContent')
            credit = credit.replace(',', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            collection.update_one(mangos_id, {"$set": {"Credit": credit}})
            print(f"{ID[id]}= {credit}")
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            time.sleep(1)
            ucloudlogout = pyautogui.locateOnScreen('./image/ucloudlogout.png')
            if ucloudlogout is not None:
                pyautogui.click(ucloudlogout)
                time.sleep(2)
            else:
                pass

            id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
