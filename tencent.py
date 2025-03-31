import time
import pyautogui
import sys
import re  
from List_Zentao import ID, mongodb_id, tuple_id, Tencent_Webpage
from PIL import ImageGrab
from bson import ObjectId 
from function import chrome, update_one, wait, find_element_nontext, wait_buttonclick_XPATH

# 腾讯云【中国站】
def tencent1(driver):
    
    id = tuple_id[4]

    try:
        # Go to Webpage
        driver.get('https://cloud.tencent.com/login?s_url=https://console.cloud.tencent.com/expense/overview')
        time.sleep(1)

        # detect 切换其他账号button
        try:
            if find_element_nontext(driver, "/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/h3"):
                time.sleep(2)
                pyautogui.click(x=450, y=202)
        except:
            pass
        
        wait(driver, '/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/ul/li[1]/div/div/div')
        pyautogui.click(x=608, y=209)
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
        pyautogui.click(x=554, y=455)
        time.sleep(1)
            
        while True:
            if pyautogui.locateOnScreen('./image/keyong.png') is not None:
                time.sleep(2)
                break
            else:
                time.sleep(1)

        time.sleep(5)

        while True:
            credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]')
            time.sleep(1)
            if credit == "--":
                pass
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
        # Logout
        logout_button = wait_buttonclick_XPATH(driver, "//button[contains(text(),'退出')]")
        logout_button.click()
               
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# 腾讯云【国际站】
def tencent2(driver):
    
    id = tuple_id[5]
    id_Range = tuple_id[6] - tuple_id[5]

    try:

        for i in range(id_Range): #14

            driver.get('https://www.tencentcloud.com/zh/account/login?s_url=https://console.tencentcloud.com/expense/rmc/accountinfo')
            time.sleep(1)

            try:
                if find_element_nontext(driver, "/html/body/div[1]/main/div/div/div/div/div/div/div[1]/div/div/div/div[1]") == "CAM用户登录":
                    pyautogui.click(x=318, y=623)
            except:
                pass
            
            wait(driver, '/html/body/div/main/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]')    
            time.sleep(1)    
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
            
            # Accountinfo
            # Wait Condition   
            wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[1]/h3')

            time.sleep(1)

            while True:
                try:
                    credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div')
                except:
                    pass           
                
                if credit == "0.00USD（冻结额度 0.00 USD）":
                    time.sleep(2)
                else:
                    break
                    
            # Extract Credit 
            credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div')

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

# 腾讯云 CAM用户登录   
def tencent3(driver):

    id = tuple_id[6]
    id_Range = tuple_id[7] - tuple_id[6]

    for i in range (id_Range):
        try:
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
            wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[1]/h3') 
            time.sleep(3)
            
            # Extract Credit  
            while True:
                credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section[1]/main/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div')
                if credit == "--":
                    continue
                else:
                    break

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
            time.sleep(111111)

# 腾讯云 子用户登录 
def tencent4(driver):

    id = tuple_id[7]

    try:

        # Go to Webpage
        driver.get('https://cloud.tencent.com/login/subAccount?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fexpense%2Foverview')
        time.sleep(2)
        
        wait(driver, '/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/h3') 

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
        pyautogui.click(x=552, y=507)
        time.sleep(1)

        # Wait Condition
        wait(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[2]/div/div/div[1]/div/div[1]/h3') 
        time.sleep(15)

        # Extract Credit  
        while True:
            credit = find_element_nontext(driver, '/html/body/div[1]/div[2]/div[2]/div/section/main/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]')
            time.sleep(1)
            if credit == "--":
                pass
            else:
                break

        # Replace
        credit = credit.replace(',', '')
        credit = credit.replace('元', '')
        
        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, credit)
        print(f"{ID[id]}= {credit}")

        time.sleep(1)

        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        pyautogui.moveTo(x=1507, y=106)
        time.sleep(3)
        pyautogui.click(1426, 558)
        time.sleep(3)

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(111111)

driver = chrome()
tencent1(driver)
tencent2(driver) 
tencent3(driver)
tencent4(driver) 
driver.close()

