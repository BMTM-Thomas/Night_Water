import time
import pyautogui
import sys
import re  
from List_Zentao import ID, mongodb_id, tuple_id, Tencent_Webpage
from PIL import ImageGrab
from bson import ObjectId 
from function import chrome, update_one, wait, find_element_XPATH, find_element_nontext

# 腾讯云【中国站】
def tencent1(driver):
    
    id = tuple_id[4]
 
    try:
        # Go to Webpage
        driver.get('https://cloud.tencent.com/login?s_url=https://console.cloud.tencent.com/expense/overview')
        time.sleep(2)

        # detect 切换其他账号button
        if pyautogui.locateOnScreen('./image/tencent1.png') is not None:
            time.sleep(2)
            pyautogui.click(x=448, y=223)
        elif pyautogui.locateOnScreen('./image/tencentint.png') is not None:
            time.sleep(3)
            pyautogui.moveTo(x=1460, y=139)
            time.sleep(1)
            pyautogui.click(x=1422, y=336)
            time.sleep(1)
        
        for i in range(5):
            wait(driver, '/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/ul/li[1]/div/div/div', '扫码登录')
            pyautogui.click(x=604, y=232)
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
            pyautogui.click(x=532, y=482)
            time.sleep(1)
              
            while True:
                if pyautogui.locateOnScreen('./image/keyong.png') is not None:
                    time.sleep(2)
                    break
                else:
                    time.sleep(1)

            time.sleep(1)

            while True:
                credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]')
                if credit == "--":
                    continue
                else:
                    break

            # Replace
            credit = credit.replace(',', '')
            credit = credit.replace('元', '')

            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")
    
            pyautogui.click(x= 1558, y=135)
            pyautogui.click(x= 1558, y=135)
            time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            logout1 = pyautogui.locateOnScreen('./image/tencentlogout1.png')
            logout2 = pyautogui.locateOnScreen('./image/tencentlogout2.png')
            if logout1 is not None:
                pyautogui.click(logout1)
            else:
                if logout2 is not None:
                    pyautogui.click(logout2)
                else:
                    pyautogui.click(x= 1425, y=524)

            id += 1
               
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# 腾讯云【国际站】
def tencent2(driver):
    
    id = tuple_id[5]

    try:
        driver.get('https://www.tencentcloud.com/zh/account/login?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2Fexpense%2Frmc%2Faccountinfo')
        time.sleep(2)

        for i in range(12):

            if pyautogui.locateOnScreen('./image/cam.png') is not None:
                pyautogui.click(x=318, y=642)
                
            wait(driver, '/html/body/div/main/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]', '邮箱登录')    
            time.sleep(3)        
            pyautogui.click(x=1416, y=62)
            time.sleep(1)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1260, y=170)
            time.sleep(1)
            pyautogui.click(x=313, y=484)
            time.sleep(2)

            # Wait Image Appear 
            if pyautogui.locateOnScreen('./image/chinese.png') is not None:
                time.sleep(1)
            else:
                pass
            
            # Accountinfo
            if i <= 9:
            
                # Wait Condition   
                wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[1]/h3', '可用额度')

                time.sleep(1)

                while True:
                    credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div')
                    if credit == "0.00USD（冻结额度 0.00 USD）":
                        pass
                    else:
                        break

            # Expenses
            else:
                driver.get('https://console.tencentcloud.com/expense')

                # Wait Condition   
                wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/h3', '已出账的未还账单总金额') 
                
                time.sleep(3)
                
                # Open 可用额度
                if i == 6 and pyautogui.locateOnScreen('./image/buttonoff.png') is not None:
                    pyautogui.click(x=1562, y=183)
                    time.sleep(1)

                # Extract Credit 
                try:
                    credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div/div/div/em')
                except:                                            
                    credit = find_element_nontext(driver, '//*[@id="expense-index"]/section/main/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div/em')

            # Replace
            credit = credit.replace(',', '')
            credit = re.sub(r'USD.*', 'USD', credit)
            credit = credit.replace('USD', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

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

# 腾讯云【中国站】【子用户】   
def tencent3(driver):

    id = tuple_id[6]

    try:
        driver.get('https://cloud.tencent.com/login/subAccount/100015429463?s_url=https://console.cloud.tencent.com/expense/overview')

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
        pyautogui.click(x=514, y=545)
        time.sleep(1)

        # Wait Condition   
        while True:
            if pyautogui.locateOnScreen('./image/keyong.png') is not None:
                time.sleep(3)
                break
            else:
                pass
            
         # Extract Credit
        try:
            credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]')                                                  
        except:
            credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]')
                                                    
        # Replace
        credit = credit.replace(',', '')
        credit = credit.replace('元', '')
        
        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, credit)
        print(f"{ID[id]}= {credit}")

        time.sleep(1)
        pyautogui.click(x= 1558, y=135)
        pyautogui.click(x= 1558, y=135)
        time.sleep(3)

        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        logout = pyautogui.locateOnScreen('./image/tencentlogout1.png')
        if logout is not None:
            time.sleep(1)
            pyautogui.click(logout)
        else:
            pyautogui.click(x=1475, y=581)

        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# 腾讯云 CAM用户登录   
def tencent4(driver):

    id = tuple_id[7]

    try:
        for i in range(2):
            driver.get(Tencent_Webpage[i])

            time.sleep(3)
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
            pyautogui.click(x=314, y=570)
            time.sleep(1)

            # Wait Condition   
            wait(driver, '/html/body/div/main/div/div/div/div/div[2]/div[1]/div', '完善关联手机信息') 
            time.sleep(1)
            pyautogui.click(x=1118, y=679)

            # Wait Condition
            if i == 0:   
                wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/h3', '已出账的未还账单总金额') 
                time.sleep(3)
            else:
                wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[1]/h3', '可用额度') 
                time.sleep(3)

            # Open 可用额度
            if pyautogui.locateOnScreen('./image/buttonoff.png') is not None:
                pyautogui.click(x=1562, y=183)
                time.sleep(1)

            try:
            # Extract Credit (ven327, 328)   
                credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div/em')
            except:
                credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div')
            
            # Replace
            credit = re.sub(r'USD.*', 'USD', credit)
            credit = credit.replace(',', '')
            credit = credit.replace('USD', '')
            
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            time.sleep(1)

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            pyautogui.moveTo(x=1555, y=136)
            time.sleep(2)
            logout = pyautogui.locateOnScreen('./image/tencentlogout1.png')
            if logout is not None:
                time.sleep(1)
                pyautogui.click(logout)

            time.sleep(2)
            id+=1

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

driver = chrome()
tencent1(driver)
tencent2(driver)
tencent3(driver)
tencent4(driver)
driver.close()

