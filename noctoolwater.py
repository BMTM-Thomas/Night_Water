import time
import certifi
import pyautogui
import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from List_Zentao import ID, mongodb_id
from List_Noctool import n_webpage
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
    noctool(driver)
    low_water()
    time.sleep(1)
    driver.quit()

def wait(driver, path, text):
    try:
        WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# noctool
def noctool(driver):
    web = 0 
    id = 0
    driver.get('http://10.77.1.196/stocks/')
    wait(driver, '/html/body/div/div/main/div/h3', '記錄列表') 
    driver.get('http://10.77.1.196/stocks/')
    time.sleep(1)
    try:
        for i in range(99): # 99
 
            driver.get(n_webpage[web])
            wait(driver, '/html/body/div/div/main/div/div[3]/div[2]/div/div[1]/h5', '記錄量趨勢圖') 
             
            time.sleep(1)
            if i == 0:       
                pyautogui.click(x=879, y=346)
                time.sleep(1)
            pyautogui.scroll(-30)
            time.sleep(1)
            pyautogui.click(x=187, y=675)
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            documents = collection.find_one(mangos_id)
            credit_value = documents.get('Credit', 'N/A') 
            print(f"{ID[id]}= {credit_value}")
            pyautogui.write(credit_value)
            pyautogui.click(x=67, y=729)

            id+=1
            web +=1
    except:
        while True:
            time.sleep(1)

def low_water ():

    id = 0

    print("\n\n")
    print("【低于安全水位】\n")
    for i in range (99): #99
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        documents = collection.find_one(mangos_id)
        ven = documents['Ven_Machine']
        credit = documents['Credit']
        unit = documents['Unit']
        secure_credit = documents['Secure_Credit']
        report = documents['Report']

        if float(credit) < float(secure_credit):
            print(f"【{report}】 {ven}已低于安全流量 (当前存量：{credit} {unit} 安全存量：{secure_credit} {unit})")
            collection.update_one(mangos_id, {"$set": {"Report": "Reported"}})
        else:
            collection.update_one(mangos_id, {"$set": {"Report": "Not Yet"}})
  
        i+=1      
        id+=1
    print("\n\n")

if __name__ == "__main__":
    main()