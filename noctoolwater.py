import time
import pyautogui
from List_Zentao import ID, mongodb_id
from List_Noctool import n_webpage
from bson.objectid import ObjectId  
from function import chrome, update_one, wait, find_element_XPATH, find_element_nontext, wait_buttonclick, find_one, update_one2

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
            documents = find_one(mangos_id)
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
        documents = find_one(mangos_id)
        ven = documents['Ven_Machine']
        credit = documents['Credit']
        unit = documents['Unit']
        secure_credit = documents['Secure_Credit']
        report = documents['Report']

        if float(credit) < float(secure_credit):
            print(f"【{report}】 {ven}已低于安全流量 (当前存量：{credit} {unit} 安全存量：{secure_credit} {unit})")
            report_status = "Reported" 
            update_one2(mangos_id, report_status)
        else:
            report_status2 = "Not Yet" 
            update_one2(mangos_id, report_status2)
        i+=1      
        id+=1
    print("\n\n")

driver = chrome()
noctool(driver)
low_water()