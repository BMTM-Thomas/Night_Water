import time
import certifi
import pyautogui
import sys
import pymongo
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from AppKit import NSPasteboard, NSPasteboardTypePNG
from PIL import ImageGrab
from List_Zentao import ID, mongodb_id
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
    options.add_argument("--hide-crash-restore-bubble")
    options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    driver=webdriver.Chrome(options=options)
    zentao(driver)
    driver.quit()

def wait(driver, path, text):
    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# zentao
def zentao(driver):
    
    try:
        # Go to Webpage
        driver.get('https://zr-zentao2023.cccqx.com/zentao/execution-task-26.html')
        try:
            if driver.find_element(By.ID, 'loginPanel') is not None:
                time.sleep(1)
                pyautogui.click(1420,62)

                # Wait for image Appear
                image_vault = None
                while image_vault is None:
                    image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)
                print("Lastpass Image Vault Loaded") 

                time.sleep(1)
                pyautogui.click(1176,212)   
                time.sleep(1)
                pyautogui.click(805,577)    
                time.sleep(1)   
                pyautogui.click(805,577)   
        except:
            pass


        while True:
                mynoc = pyautogui.locateOnScreen('./image/mynoc.png')
                if mynoc is not None:
                    break
                else:
                    pass
                
        pyautogui.click(x=1509, y=315)

        while True: 
            remark = pyautogui.locateOnScreen('./image/remark.png')
            if remark is not None:
                break
            else:
                pass
        pyautogui.click(x=1468, y=722)
        time.sleep(1)
        pyautogui.click(x=729, y=737)
        time.sleep(1) 
        pyautogui.press('enter', presses = 8)
        time.sleep(1)
        pyautogui.click(x=600, y=644)

        id = 0
        for y in range(94): #94
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            documents = collection.find_one(mangos_id)
            ven_machine_value = documents.get('Ven_Machine','N/A')
    
            credit_value = documents.get('Credit', 'N/A') 
            unit_value = documents.get('Unit', 'N/A')
            merge = ven_machine_value + " " + credit_value + " " + unit_value

            pyperclip.copy(merge)
            pyautogui.hotkey("command", "v")
    
            # Create an instance of the NSPasteboard class
            pasteboard = NSPasteboard.generalPasteboard()

            # Read image data from the file
            with open("./晚班水位/"+ID[id]+".png", 'rb') as file:
                image_data = file.read()

            # Copy the image data to the clipboard as a PNG
            if image_data:
                pasteboard.declareTypes_owner_([NSPasteboardTypePNG], None)
                pasteboard.setData_forType_(image_data, NSPasteboardTypePNG)
                print(ID[id]+" Image copied to clipboard.")
                
            else:
                print("Failed to read image data from the file.")

            # Paste Image
            pyautogui.keyDown('command')
            pyautogui.press('v')

            # Next Line
            pyautogui.press('enter', presses = 2)
            time.sleep(1)

            y+=1
            id+=1

        time.sleep(1)
        pyautogui.click(1594,783)
        time.sleep(1)

        # Special Case for Button Click
        driver.switch_to.frame("appIframe-project")
        save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/div[2]/div[1]/div/div[5]/button")))
        save_button.click()
        time.sleep(3)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


