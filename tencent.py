import time
import pyautogui
import sys
import re  
from List_Zentao import ID, mongodb_id, tuple_id, Tencent_Webpage
from PIL import ImageGrab
from bson import ObjectId 
from function import chrome, update_one, wait, find_element_nontext

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
            pyautogui.click(x=402, y=202)
        
        for i in range(5):
            wait(driver, '/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/ul/li[1]/div/div/div', '扫码登录')
            pyautogui.click(x=579, y=209)
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
    
            pyautogui.click(x= 1496, y=107)
            pyautogui.click(x= 1496, y=107)
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
                    pyautogui.click(x= 1415, y=539)

            id += 1
               
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# 腾讯云【国际站】
def tencent2(driver):
    
    id = tuple_id[5]

    try:
        driver.get('https://www.tencentcloud.com/zh/account/login?s_url=https://console.tencentcloud.com/expense/rmc/accountinfo')
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
            pyautogui.click(x=313, y=474)
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
                    pyautogui.click(x=1562, y=160)
                    time.sleep(1)

                # Extract Credit 
                credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div/em')


            # Replace
            credit = credit.replace(',', '')
            credit = re.sub(r'USD.*', 'USD', credit)
            credit = credit.replace('USD', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            time.sleep(1)
            pyautogui.click(x= 1552, y=110)
            pyautogui.click(x= 1552, y=110)
            time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            time.sleep(1)
            logout = pyautogui.locateOnScreen('./image/tencentlogout1.png')
            if logout is not None:
                time.sleep(1)
                pyautogui.click(logout)
            else:
                pyautogui.click(x=1473, y=485)
                    
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
        pyautogui.click(x=505, y=534)
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
        pyautogui.click(x= 1552, y=110)
        pyautogui.click(x= 1552, y=110)
        time.sleep(3)

        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        logout = pyautogui.locateOnScreen('./image/tencentlogout1.png')
        if logout is not None:
            time.sleep(1)
            pyautogui.click(logout)
        else:
            pyautogui.click(x=1404, y=609)

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
            pyautogui.click(x=310, y=554)
            time.sleep(1)

            # Wait Condition
            wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[1]/h3', '可用额度') 
            time.sleep(2)

            # Extract Credit  
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
            pyautogui.moveTo(x=1558, y=110)
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

