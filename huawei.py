import time
import pyautogui
from List_Zentao import ID, Huawei_Webpage, mongodb_id, tuple_id
from PIL import ImageGrab
from bson.objectid import ObjectId   
from function import *

# 华为云【OPSADMIN】【IAM用户登录】
def huawei1(driver):

    id = tuple_id[8]
    id_Range = tuple_id[9] - tuple_id[8]
    
    try:
        for i in range(id_Range):
            # # Go to Webpage
            driver.get(Huawei_Webpage[i])
            wait(driver, '/html/body/div[3]/div/div[2]/div[2]/div[1]/span') 

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
            pyautogui.click(x=1193, y=581)
            time.sleep(1)
            
            # ven399 only
            try:
                time.sleep(1)
                if find_element_text(driver, '/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]'): #上次登录成功时间:
                    time.sleep(1)
                    pyautogui.click(x=937, y=485)
            except:
                pass
            
            time.sleep(1)

            # if 登入验证appear
            try:    
                if find_element_text(driver, '/html/body/div[3]/div/div[1]/div[1]/p'): #验证登入
                    time.sleep(1)
                    pyautogui.click(x= 533, y=498)
                    time.sleep(1)
                    pyautogui.click(x=651, y=605)
            except:
                pass


            wait(driver, '//span[contains(text(),"安全监控")]') # 安全监控
            time.sleep(1)

            driver.get('https://account-intl.huaweicloud.com/usercenter/?agencyId=0d7674b62e00f2a71f10c0148595ffbb&region=ap-southeast-1&locale=zh-cn#/userindex/allview')
            wait(driver, '//cbcsubexpense-partner-budget[@class="balance ng-star-inserted"]//div[@class="card-title"]') 

            time.sleep(2)
            
            # Extract Credit   
            credit = find_element_text(driver, '//span[@id="remainAmount_bindtype3"]') 
                                                
            # Replace
            credit = credit.replace(',', '')
            credit = credit.replace('$', '')
            credit = credit.replace(' USD', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            time.sleep(1)

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

            try:
                if find_element_text(driver, '/html/body/div[1]/div/div[1]/div/span[2]'):
                    pyautogui.click(1574, 108)
                    time.sleep(1)
                else:
                    pyautogui.moveTo(1530, 104)
            except:
                pyautogui.moveTo(1530, 104)

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
    id_Range = tuple_id[10] - tuple_id[9]
    
    try:
        # Go to Webpage
        driver.get('https://auth.huaweicloud.com/authui/login.html?service=https://account-intl.huaweicloud.com/usercenter/#/login')
        # with pyautogui.hold('command'):
        #     pyautogui.press('r')

        time.sleep(3)

        # If is English, Change to Chinese
        chinese = pyautogui.locateOnScreen('./image/chinese2.png')
        if chinese is None:
            pyautogui.moveTo(x= 1532, y=108)
            time.sleep(1)
            pyautogui.click(x= 1532, y=156)
            time.sleep(1)
            wait(driver, '/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/span/span') 
            time.sleep(1)
        else:
            pass
        
        for i in range(id_Range):
            
            wait(driver, '/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/span/span') 
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
            pyautogui.click(x= 1191, y=504)
            time.sleep(2)

            # # if 登入验证appear ven420, ven425
            # if i >= 6:
            #     wait(driver, '/html/body/div[3]/div/div[1]/div[1]/p') #登录验证
            #     time.sleep(1)
            #     pyautogui.click(x= 540, y=455)
            #     time.sleep(1)
            #     pyautogui.click(x=662, y=559)

            wait(driver, '/html/body/div[4]/cbcusercenterwebsite-master-root/cbcusercenterwebsite-layout-default/div/div[1]/div/cbcsubexpense-root/div/ti-app-layout-main-content/cbcsubexpense-allview-menu/cbcsubexpense-allview-hk/tp-layout-content/div/tp-layout-column[1]/tp-layout-content-body[1]/tp-layout-section/div[1]/cbcsubexpense-partner-budget/div[1]/span') 
            time.sleep(2)

            # Extract Credit
            credit = find_element_text(driver, '/html/body/div[4]/cbcusercenterwebsite-master-root/cbcusercenterwebsite-layout-default/div/div[1]/div/cbcsubexpense-root/div/ti-app-layout-main-content/cbcsubexpense-allview-menu/cbcsubexpense-allview-hk/tp-layout-content/div/tp-layout-column[1]/tp-layout-content-body[1]/tp-layout-section/div[1]/cbcsubexpense-partner-budget/div[2]/div[1]/span')
            
            # Replace
            credit = credit.replace(',', '')
            credit = credit.replace('$', '')
            credit = credit.replace(' USD', '')
   
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            time.sleep(1)

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            security = pyautogui.locateOnScreen('./image/huaweisecurity.png')
            if security is not None:
                pyautogui.moveTo(x= 1485, y=171)
            else:
                pyautogui.moveTo(x= 1530, y=109)
                
            time.sleep(1)

            logout2 = pyautogui.locateOnScreen('./image/huaweilogout2.png')
            if logout2 is not None:
                pyautogui.click(logout2)
            else:
                pyautogui.click(x= 1470, y=396)

            time.sleep(1)

            id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

driver = chrome()
driver = next(driver)
huawei1(driver)
huawei2(driver)