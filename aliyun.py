import time                                                                                            
import pyautogui                                                                                                                                                                                  
import sys                                                                                                                                  
from List_Zentao import ID, mongodb_id,tuple_id                                                       
from List_Aliyun_DDCaptcha import m_X1,m_Y2,d_X1,d_Y2,ram_d_X1,ram_d_Y2,ram_m_X1,ram_m_Y2              
from PIL import ImageGrab  
from bson.objectid import ObjectId                                                                  
from function import *

# 阿里云【中国站】
def aliyun1(driver):  
    
    id = tuple_id[0]
    id_Range = tuple_id[1] - tuple_id[0]
    
    try:
        driver.get('https://account.aliyun.com/login/login.htm?oauth_callback=https://usercenter2.aliyun.com/home')
        time.sleep(2)

        try:
            if find_element_nontext(driver, "//h3[contains(text(),'RAM 用户登录')]"):
                    pyautogui.click(798, 632)
                    wait(driver, "//span[contains(text(),'International - 简体中文')]")
                    time.sleep(1)  
            else:
                pass
        except Exception as e:
            pass


        if pyautogui.locateOnScreen('./image/alilogin_text1.png') is not None:
            if pyautogui.locateOnScreen('./image/international.png') is not None:
                time.sleep(1)
                pyautogui.moveTo(1245, 114)
                time.sleep(1)
                pyautogui.click(1253, 386)
                time.sleep(1)
                driver.get('https://account.aliyun.com/login/login.htm?oauth_callback=https://usercenter2.aliyun.com/home')
        else:
            pass


        for i in range (id_Range) : 
            wait(driver, "/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[3]/div[1]/div/div[1]/div[1]/div")
            wait(driver, "/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[3]/div[1]/div/div[1]/div[2]/div")
            if pyautogui.locateOnScreen('./image/cross.png') is not None: 
                pyautogui.click(85, 62)
            time.sleep(1)
            pyautogui.click(x=1416, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(1)
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1216, y=175)
            time.sleep(1)
      
            # Click Login
            alilogin = pyautogui.locateOnScreen('./image/alilogin.png')
            if alilogin:
                pyautogui.click(pyautogui.center(alilogin))
            else:
                pass
            
            time.sleep(2) 
            
            # Drag and Drop Appear?
            if pyautogui.locateOnScreen('./image/alidnd.png') is not None:
                pyautogui.moveTo(858, 469, 0.24)
                pyautogui.dragTo(1150, 469, button='left', duration=0.24)
            else:
                pass
            
            time.sleep(2)
            
            # Drag and Drop Failed
            if pyautogui.locateOnScreen('./image/alidndfailed7.png') is not None:
                pyautogui.click(x=978, y=469)
                time.sleep(1)
                pyautogui.moveTo(835, 476, 0.2)
                pyautogui.dragTo(1150, 476, button='left', duration=0.2)
            else:
                pass

            # detected unusual traffic from your network (Drag n Drop)
            if pyautogui.locateOnScreen('./image/unusual_traffic.png') is not None:
                pyautogui.moveTo(669, 526, 0.2)
                pyautogui.dragTo(956, 526, button='left', duration=0.2)
            else:
                pass


            # Extract credit
            # This is due to VEN407 change UI
            if i == 1:
                # Waiting for a Text to be appear
                wait(driver, "//div[@class='label'][contains(text(),'账户可用额度')]") 

                time.sleep(2)

                while True:
                    try:
                        credit = find_element_nontext(driver, "/html/body/div[2]/div[1]/div[3]/div/ali-alfa-cloudservice-xusercenter-widget-home/div/div[1]/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/span")
                    except:
                        driver.refresh()
                        time.sleep(5)
                        continue
                    break
            
            # VEN338 Aliyun China remain same no change
            else:
                # Waiting for a Text to be appear
                wait(driver, "//span[contains(text(),'充值汇款')]") 
                
                while True:
                    try:
                        credit = find_element_nontext(driver, "//span[@class='amount']//span[1]")
                    except:
                        driver.refresh()
                        time.sleep(5)
                        continue
                    break

            # Replace
            credit = credit.replace('¥ ', '')
            credit = credit.replace(',', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            time.sleep(1)
            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_nontext(driver, "//span[contains(text(),'安全管控')]"):
                        break
                except:
                    time.sleep(1)
                    pyautogui.click(x= 1183, y=192)
                    time.sleep(2)
                    pyautogui.click(x= 1505, y=104)
                    time.sleep(1)

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            
            # Logout Button
            logout_button = wait_buttonclick_XPATH(driver, "//a[contains(text(),'退出登录')]")
            logout_button.click()
            
            id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)
         
# ven387 费用 + IP 纯真社区版IP库离线下载
def ven387(driver):  
    
    id = tuple_id[1]
    
    try:
        time.sleep(1)
        driver.get('https://account.aliyun.com/login/login.htm?oauth_callback=https://usercenter2.aliyun.com/home')
        time.sleep(1)
        
        try:
            if find_element_nontext(driver, "//h3[contains(text(),'RAM 用户登录')]"):
                    pyautogui.click(798, 632)
                    wait(driver, "//span[contains(text(),'International - 简体中文')]")
                    time.sleep(1)  
            else:
                pass
        except Exception as e:
            pass

        if pyautogui.locateOnScreen('./image/alilogin_text1.png') is not None:
            if pyautogui.locateOnScreen('./image/international.png') is not None:
                time.sleep(1)
                pyautogui.moveTo(1288, 144, 0.2)
                time.sleep(1)
                pyautogui.click(1253, 420)
                time.sleep(1)
                driver.get('https://account.aliyun.com/login/login.htm?oauth_callback=https://usercenter2.aliyun.com/home')
        else:
            pass
        
        wait(driver, '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[3]/div[1]/div/div[1]/div[1]/div')
        wait(driver, '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[3]/div[1]/div/div[1]/div[2]/div')

        pyautogui.click(x=1416, y=62)

        # Wait for image Appear
        image_vault = None
        while image_vault is None:
            image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)
        
        time.sleep(1)
        pyautogui.write(ID[id])
        time.sleep(1)
        pyautogui.click(x=1216, y=175)
        time.sleep(1)
        
        # Click Login
        alilogin = pyautogui.locateOnScreen('./image/alilogin.png')
        if alilogin:
            pyautogui.click(pyautogui.center(alilogin))
        else:
            pass
        
        time.sleep(3) 
        
        # Drag and Drop Appear?
        if pyautogui.locateOnScreen('./image/alidnd.png') is not None:
            pyautogui.moveTo(1058, 481, 0.2)
            pyautogui.dragTo(1453, 558, button='left', duration=0.2)
        else:
            pass
        
        time.sleep(2)
        
        # Drag and Drop Failed
        if pyautogui.locateOnScreen('./image/alidndfailed.png') is not None:
            pyautogui.click(x=1113, y=546)
            time.sleep(1)
            pyautogui.moveTo(1068, 470, 0.2)
            pyautogui.dragTo(1353, 470, button='left', duration=0.2)
        else:
            pass
        
        # Waiting for a Text to be appear
        wait(driver, '/html/body/div[2]/div[1]/div[3]/div/ali-alfa-cloudservice-xusercenter-widget-home/div/div[1]/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[3]/button[1]/span') 
        
        time.sleep(1)

        while True:
            try:
                credit = find_element_nontext(driver, '/html/body/div[2]/div[1]/div[3]/div/ali-alfa-cloudservice-xusercenter-widget-home/div/div[1]/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/span')
            except:
                driver.refresh()
                time.sleep(5)
                continue
            break
        
        # Replace
        credit = credit.replace('¥ ', '')
        credit = credit.replace(',', '')

        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, credit)
        print(f"{ID[id]}= {credit}")

        time.sleep(1)
        pyautogui.click(x= 1505, y=104)
        time.sleep(1)

        while True:
            try:
                if find_element_nontext(driver, "//span[contains(text(),'安全管控')]"):
                    break
            except:
                time.sleep(1)
                pyautogui.click(x= 1183, y=192)
                time.sleep(2)
                pyautogui.click(x= 1505, y=104)
                time.sleep(1)
        
        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        time.sleep(1)

        while True:
            try:
                if find_element_nontext(driver, "/html[1]/body[1]/div[12]/div[1]/div[1]/a[1]/span[1]/span[2]"):
                    break
            except:
                pyautogui.click(x= 1183, y=192)
                time.sleep(2)
                pyautogui.click(x= 1505, y=104)
                time.sleep(2)

        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        
        # Logout Button
        logout_button = wait_buttonclick_XPATH(driver, "//a[contains(text(),'退出登录')]")
        logout_button.click()
        
        id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)
        sys.exit(1)
      
# 阿里云【国际站】【RAM】
def aliyun3(driver):

    id = tuple_id[3]
    id_Range = tuple_id[4] - tuple_id[3]
    X = 0
    Y = 0
    
    try:
        driver.get('https://signin.alibabacloud.com/5256975880117898.onaliyun.com/login.htm?callback=https%3A%2F%2Fusercenter2-intl.aliyun.com%2Fbilling%2F%23%2Faccount%2Foverview#/main')
        time.sleep(2)
        
        for i in range(id_Range):
    
            time.sleep(1)

            while True:
                if pyautogui.locateOnScreen('./image/next1.png') is not None:
                    break
                else:
                    time.sleep(1)
            pyautogui.click(x=1416, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(1)
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1257, y=171)
            time.sleep(1)

            # Login Button(id)
            logout_button = wait_buttonclick_XPATH(driver, "//span[contains(text(),'下一步')]")
            logout_button.click()
            time.sleep(3)

            # Drag and Drop Appear? #### Username Login
            alidnd3 = pyautogui.locateOnScreen('./image/alidnd.png')
            if alidnd3 is not None:
                pyautogui.moveTo(ram_m_X1[X], ram_m_Y2[Y], 0.13)
                pyautogui.dragTo(ram_d_X1[X], ram_d_Y2[Y], button='left', duration=0.13)
                X += 1
                Y += 1

                if X >= 8:
                    X = 0
                    Y = 0
                time.sleep(2)
            else:
                pass
            
            # Drag and Drop Failed
            while True:
                if pyautogui.locateOnScreen('./image/alidndfailed3.png') is not None:
                    pyautogui.click(x=795, y=462)
                    time.sleep(1)
                    pyautogui.moveTo(ram_m_X1[X], ram_m_Y2[Y], 0.13)
                    pyautogui.dragTo(ram_d_X1[X], ram_d_Y2[Y], button='left', duration=0.13)
                    time.sleep(3)
                    X += 1
                    Y += 1

                    if X >= 8:
                        X = 0
                        Y = 0
                    time.sleep(1)
                else:
                    break
                
            # Click Login
            wait(driver, '/html/body/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/form/div[5]/button/span')
            time.sleep(1)
            login = pyautogui.locateOnScreen('./image/aliram_login.png')

            if login is not None:
                image_center = pyautogui.center(login)
                pyautogui.click(image_center)
            else:
                pass

            time.sleep(3)

            # Drag and Drop Appear? ### Password Login
            alidnd4 = pyautogui.locateOnScreen('./image/alidnd6.png')
            if alidnd4 is not None:
                pyautogui.moveTo(ram_m_X1[X], ram_m_Y2[Y], 0.2)
                pyautogui.dragTo(ram_d_X1[X], ram_d_Y2[Y], button='left', duration=0.2)
                time.sleep(2)
            else:
                pass
            
            time.sleep(1)

            # MFA Appear
            try:
                if find_element_nontext(driver, '/html/body/div/div/div/div[1]/div[1]/div[2]/button/span'):
                    pyautogui.click(1206,242)
                else:
                    wait(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[1]/span')
            except:
                pass

            wait(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[1]/span')
            wait(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/span')
            
            time.sleep(1)

            # Extract Credit
            credit = find_element_nontext(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/span')
        
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            time.sleep(1)
            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_nontext(driver, "//span[contains(text(),'安全信息')]") :
                        break
                except:
                    time.sleep(1)
                    pyautogui.click(x= 1183, y=104)
                    time.sleep(2)
                    pyautogui.click(x= 1505, y=104)
                    time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            
            #Click Logout
            logout_button = wait_buttonclick_XPATH(driver, "//a[contains(text(),'退出登录')]")
            logout_button.click()
            time.sleep(2)
            
            id += 1
      
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(111111)

# watermelon【国际站】【RAM】
def watermelon_1(driver):

    id = tuple_id[17]
    id_Range = tuple_id[18] - tuple_id[17]
    X = 0
    Y = 0

    try:
        driver.get('https://signin.alibabacloud.com/5256975880117898.onaliyun.com/login.htm?callback=https%3A%2F%2Fusercenter2-intl.aliyun.com%2Fbilling%2F%23%2Faccount%2Foverview#/main')
        time.sleep(2)
        
        for i in range(id_Range):

            print(ID[id])
            time.sleep(1)

            while True:
                if pyautogui.locateOnScreen('./image/next1.png') is not None:
                    break
                else:
                    time.sleep(1)
            pyautogui.click(x=1416, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(1)
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1257, y=171)
            time.sleep(1)

            # Login Button(id)
            logout_button = wait_buttonclick_XPATH(driver, "//span[contains(text(),'下一步')]")
            logout_button.click()
            time.sleep(3)

            # Drag and Drop Appear? #### Username Login
            alidnd3 = pyautogui.locateOnScreen('./image/alidnd.png')
            if alidnd3 is not None:
                pyautogui.moveTo(ram_m_X1[X], ram_m_Y2[Y], 0.13)
                pyautogui.dragTo(ram_d_X1[X], ram_d_Y2[Y], button='left', duration=0.13)
                X += 1
                Y += 1

                if X >= 8:
                    X = 0
                    Y = 0
                time.sleep(2)
            else:
                pass
            
            # Drag and Drop Failed
            while True:
                if pyautogui.locateOnScreen('./image/alidndfailed3.png') is not None:
                    pyautogui.click(x=795, y=462)
                    time.sleep(1)
                    pyautogui.moveTo(ram_m_X1[X], ram_m_Y2[Y], 0.13)
                    pyautogui.dragTo(ram_d_X1[X], ram_d_Y2[Y], button='left', duration=0.13)
                    time.sleep(3)
                    X += 1
                    Y += 1

                    if X >= 8:
                        X = 0
                        Y = 0
                    time.sleep(1)
                else:
                    break
                
            # Click Login
            wait(driver, '/html/body/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/form/div[5]/button/span')
            time.sleep(1)
            login = pyautogui.locateOnScreen('./image/aliram_login.png')

            if login is not None:
                image_center = pyautogui.center(login)
                pyautogui.click(image_center)
            else:
                pass

            time.sleep(3)

            # Drag and Drop Appear? ### Password Login
            alidnd4 = pyautogui.locateOnScreen('./image/alidnd6.png')
            if alidnd4 is not None:
                pyautogui.moveTo(ram_m_X1[X], ram_m_Y2[Y], 0.2)
                pyautogui.dragTo(ram_d_X1[X], ram_d_Y2[Y], button='left', duration=0.2)
                time.sleep(2)
            else:
                pass
            
            time.sleep(1)
    
            # MFA Appear
            try:
                if find_element_nontext(driver, '/html/body/div/div/div/div[1]/div[1]/div[2]/button/span'):
                    pyautogui.click(1206,242)
            except:
                pass
            
            # wait for 本月消费概览 appear
            while True:
                if pyautogui.locateOnScreen('./image/aliyun_account_overview.png') is None:
                    continue
                else:
                    break

            time.sleep(2)

            # Check if overdue payment
            try:
                if pyautogui.locateOnScreen('./image/overdue.png') is not None:
                    overdue = find_element_nontext(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/p/span')
                    print(f"{ID[id]}= ", overdue)   
            except:
                pass

            # Screenshot
            ImageGrab.grab().save('./watermelon/' + ID[id] + '.png')

            time.sleep(1)
            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_nontext(driver, "//span[contains(text(),'安全信息')]") :
                        break
                except:
                    time.sleep(1)
                    pyautogui.click(x= 1183, y=104)
                    time.sleep(2)
                    pyautogui.click(x= 1505, y=104)
                    time.sleep(1)
            
            #Click Logout
            logout_button = wait_buttonclick_XPATH(driver, "//a[contains(text(),'退出登录')]")
            logout_button.click()
            time.sleep(2)
            
            id += 1
      
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(111111)

driver = chrome()
aliyun1(driver)
ven387(driver)
aliyun3(driver)
watermelon_1(driver)
driver.close()
