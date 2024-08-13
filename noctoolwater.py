import time
import pyautogui
from List_Zentao import ID, mongodb_id
from List_Noctool import n_webpage
from bson.objectid import ObjectId  
from function import chrome, wait, find_one, find_element_nontext, mongodb_atlas

# noctool
def noctool(driver):
    driver.get('http://10.77.1.196/stocks/')
    wait(driver, '/html/body/div/div/main/div/h3', '記錄列表') 
    driver.get('http://10.77.1.196/stocks/')
    time.sleep(1)

    try:
        for i in range(99): # 99
 
            driver.get(n_webpage[i])
            wait(driver, '/html/body/div/div/main/div/div[3]/div[2]/div/div[1]/h5', '記錄量趨勢圖')       
            time.sleep(1)
            if i == 0:       
                pyautogui.click(x=879, y=346)
                time.sleep(1)
            pyautogui.scroll(-30)
            time.sleep(1)
            pyautogui.click(x=180, y=668)

            # Previous Credit / Data
            pre_credit = find_element_nontext(driver, "/html/body/div/div/main/div/div[3]/div[1]/div/div[2]/div/table/tbody/tr[1]/td[2]")

            # Search for Database
            mangos_id = {'_id': ObjectId(mongodb_id[i])}
            documents = find_one(mangos_id)
            credit_value = documents.get('Credit', 'N/A') 

            # Print out Previous and Actual Data
            print(f"{ID[i]}= Pre: {pre_credit}, Act: {credit_value} \n")
            
            # Write Credit Value
            pyautogui.write(credit_value)

            # button click (新增记录)
            pyautogui.hotkey("Enter")

    except:
        while True:
            time.sleep(1)

def low_water ():
    print("\n【低于安全水位】\n")
    collection = mongodb_atlas()
    documents = collection.find()

    for doc in documents:
        if float(doc.get("Credit", 0)) < float(doc.get("Secure_Credit", 0)):
            print(f"{doc.get('Ven_Machine')} 已低于安全流量 (当前存量：{doc.get('Credit')} {doc.get('Unit')}, 安全存量：{doc.get('Secure_Credit')} {doc.get('Unit')})")
        
    print("\n\n")

driver = chrome()
noctool(driver)
driver.close()
low_water()