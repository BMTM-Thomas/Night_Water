import time                                                                                            
import pyautogui                                                                                                                                                                                  
import sys                                                                                                                                  
from List_Zentao import ID, mongodb_id,tuple_id                                                       
from List_Aliyun_DDCaptcha import m_X1,m_Y2,d_X1,d_Y2,ram_d_X1,ram_d_Y2,ram_m_X1,ram_m_Y2              
from PIL import ImageGrab  
from bson.objectid import ObjectId                                                                  
from function import *

# 阿里云【国际站】
def aliyun2(driver):
    
    id = tuple_id[2]
    id_Range = tuple_id[3] - tuple_id[2]
    X = 0
    Y = 0

    try:
        driver.get('https://account.alibabacloud.com/login/login.htm?oauth_callback=https://usercenter2-intl.aliyun.com/billing/#/account/overview')
        time.sleep(1)

        try:
            if find_element_nontext(driver,"//h3[contains(text(),'RAM 用户登录')]"):
                pyautogui.click(x=798, y=638)
                time.sleep(1)
                pyautogui.click(x=861, y=333)
        except:
            pass

        if pyautogui.locateOnScreen('./image/ali_Eng.png') is not None:
            pyautogui.click(x=1246, y=118)
            time.sleep(1)
            pyautogui.click(x=1235, y=186)
            time.sleep(1)
        else:
            pass

        for i in range(id_Range):

            if pyautogui.locateOnScreen('./image/logout_Bug.png') is not None:
                pyautogui.click(x=1102, y=445)
            else:
                pass

            time.sleep(1)

            while True:
                    if pyautogui.locateOnScreen('./image/alilogin_text1.png') is not None:
                        if pyautogui.locateOnScreen('./image/alilogin_text2.png') is not None:
                            time.sleep(1)
                            break
                            
            # click lastpass extension       
            pyautogui.click(x=1415, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(1)
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1216, y=175)
            time.sleep(1)
            pyautogui.click(x=913, y=525)
            time.sleep(3)

            # Drag and Drop Appear?
            if pyautogui.locateOnScreen('./image/alidnd.png') is not None:
                pyautogui.moveTo(m_X1[X], m_Y2[Y], 0.13)
                pyautogui.dragTo(d_X1[X], d_Y2[Y], button='left', duration=0.13)
                X += 1
                Y += 1
                
                if X >= 8:
                    X = 0
                    Y = 0
                time.sleep(2)
            else:
                pass
            
            time.sleep(2)
            
            # # Drag and Drop Failed
            while True:
                if pyautogui.locateOnScreen('./image/alidndfailed5.png') is not None:
                    pyautogui.click(x=1111, y=511)
                    time.sleep(1)
                    pyautogui.moveTo(m_X1[X], m_Y2[Y], 0.16)
                    pyautogui.dragTo(d_X1[X], d_Y2[Y], button='left', duration=0.16)
                    X += 1
                    Y += 1

                    if X >= 8:
                        X = 0
                        Y = 0
                    time.sleep(2)
                else:
                    break

            # detected unusual traffic from your network (Drag n Drop)
            if pyautogui.locateOnScreen('./image/unusual_traffic.png') is not None:
                pyautogui.moveTo(660, 507, 0.12)
                pyautogui.dragTo(970, 507, button='left', duration=0.12)
            else:
                pass
            
            # wait for '正常' appear
            wait(driver, "//span[contains(text(),'正常')]") 

            # Extract Credit
            while True:
                credit = find_element_nontext(driver, "//span[@class='price-wrap ng-binding']")
                if credit == "":
                    continue
                else:
                    break

            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            time.sleep(1)
            pyautogui.click(x= 1183, y=162)
            time.sleep(1)
            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_nontext(driver,"//span[contains(text(),'基本资料')]"):
                        break
                except:
                    time.sleep(1)
                    pyautogui.moveTo(x= 1183, y=162)
                    time.sleep(2)
                    pyautogui.moveTo(x= 1505, y=104)
                    time.sleep(1)

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            
            # Logout Button
            logout_button = wait_buttonclick_XPATH(driver, "//a[contains(text(),'退出登录')]")
            logout_button.click()
            
            id += 1
            if X >= 8:
                X = 0
                Y = 0

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

# watermelon 【国际站】
def watermelon_2(driver):

    id = tuple_id[18]
    X = 0
    Y = 0

    try:
        driver.get('https://account.alibabacloud.com/login/login.htm?oauth_callback=https://usercenter2-intl.aliyun.com/billing/#/account/overview')
        time.sleep(1)
        
        # if in RAM Page, then button click back to 国际站
        try:
            if find_element_nontext(driver,"//h3[contains(text(),'RAM 用户登录')]"):
                pyautogui.click(x=798, y=638)
                time.sleep(1)
                pyautogui.click(x=861, y=333)
        except:
            pass
        
        # if 国际站 is in english, switch to chinese
        if pyautogui.locateOnScreen('./image/ali_Eng.png') is not None:
            pyautogui.click(x=1246, y=118)
            time.sleep(1)
            pyautogui.click(x=1235, y=186)
            time.sleep(1)
        else:
            pass

        for i in range(3):
            print(ID[id])

            driver.get('https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A%2F%2Fusercenter2-intl.aliyun.com%2Fbilling%2F#/account/overview')

            time.sleep(1)

            if pyautogui.locateOnScreen('./image/logout_Bug.png') is not None:
                pyautogui.click(x=1102, y=445)
            else:
                pass

            time.sleep(1)

            while True:
                    if pyautogui.locateOnScreen('./image/alilogin_text1.png') is not None:
                        if pyautogui.locateOnScreen('./image/alilogin_text2.png') is not None:
                            time.sleep(1)
                            break
        
            # click lastpass extension       
            pyautogui.click(x=1415, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(1)
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1216, y=175)
            time.sleep(1)
            pyautogui.click(x=913, y=525)
            time.sleep(3)

            # Drag and Drop Appear?
            if pyautogui.locateOnScreen('./image/alidnd.png') is not None:
                pyautogui.moveTo(m_X1[X], m_Y2[Y], 0.13)
                pyautogui.dragTo(d_X1[X], d_Y2[Y], button='left', duration=0.13)
                X += 1
                Y += 1
                
                if X >= 8:
                    X = 0
                    Y = 0
                time.sleep(2)
            else:
                pass
            
            time.sleep(2)
            
            # # Drag and Drop Failed
            while True:
                if pyautogui.locateOnScreen('./image/alidndfailed5.png') is not None:
                    pyautogui.click(x=1111, y=511)
                    time.sleep(1)
                    pyautogui.moveTo(m_X1[X], m_Y2[Y], 0.16)
                    pyautogui.dragTo(d_X1[X], d_Y2[Y], button='left', duration=0.16)
                    X += 1
                    Y += 1

                    if X >= 8:
                        X = 0
                        Y = 0
                    time.sleep(2)
                else:
                    break

            # detected unusual traffic from your network (Drag n Drop)
            if pyautogui.locateOnScreen('./image/unusual_traffic.png') is not None:
                pyautogui.moveTo(660, 507, 0.12)
                pyautogui.dragTo(970, 507, button='left', duration=0.12)
            else:
                pass

            # wait for '正常' appear
            wait(driver, "//span[contains(text(),'支付信息')]") 
            time.sleep(2)

            # Check if overdue payment
            try:
                if pyautogui.locateOnScreen('./image/overdue.png') is not None:
                    overdue = find_element_nontext(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/p/span')
                    print(f"{ID[id]}= ", overdue)
            except:
                pass

            time.sleep(1)
            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_nontext(driver,"//span[contains(text(),'基本资料')]"):
                        break
                except:
                    time.sleep(1)
                    pyautogui.moveTo(x= 1183, y=162)
                    time.sleep(2)
                    pyautogui.moveTo(x= 1505, y=104)
                    time.sleep(1)

            # Screenshot
            ImageGrab.grab().save('./watermelon' + ID[id] + '.png')

            # Logout Button
            logout_button = wait_buttonclick_XPATH(driver, "//a[contains(text(),'退出登录')]")
            logout_button.click()

            id += 1
            if X >= 8:
                X = 0
                Y = 0
    

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

driver = chrome()
aliyun2(driver)
watermelon_2(driver)
driver.quit()
