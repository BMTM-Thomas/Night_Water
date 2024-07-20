import time                                                                                            
import pyautogui                                                                                       
import re                                                                                              
import sys                                                                                                                                      
from List_Zentao import ID, mongodb_id,tuple_id                                                       
from List_Aliyun_DDCaptcha import m_X1,m_Y2,d_X1,d_Y2,ram_d_X1,ram_d_Y2,ram_m_X1,ram_m_Y2              
from PIL import ImageGrab, Image    
from bson.objectid import ObjectId                                                                  
from function import chrome, update_one, wait, find_element_XPATH, find_element_nontext, wait_buttonclick_XPATH

# 阿里云【中国站】
def aliyun1(driver):  
    
    id = tuple_id[0]
    
    try:
        driver.get('https://account.aliyun.com/login/login.htm?oauth_callback=https://usercenter2.aliyun.com/home')
        time.sleep(1)
        if pyautogui.locateOnScreen('./image/ram.png') is not None: 
                pyautogui.click(798, 651)
                wait(driver, '/html/body/div[1]/div/div[1]/nav/div/div/div/span', 'International - 简体中文') 
                time.sleep(1)  
        else:
            pass

        if pyautogui.locateOnScreen('./image/alilogin_text1.png') is not None:
                if pyautogui.locateOnScreen('./image/international.png') is not None:
                    time.sleep(1)
                    pyautogui.moveTo(1288, 144)
                    time.sleep(1)
                    pyautogui.click(1253, 420)
                    time.sleep(1)
                    driver.get('https://account.aliyun.com/login/login.htm?oauth_callback=https://usercenter2.aliyun.com/home')
        else:
            pass


        for i in range (2) : 
            wait(driver, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div', '账号密码登录')
            wait(driver, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div', '手机号登录')
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
                pyautogui.moveTo(1058, 481, 0.2)
                pyautogui.dragTo(1453, 558, button='left', duration=0.2)
            else:
                pass
            
            time.sleep(2)
            
            # Drag and Drop Failed
            if pyautogui.locateOnScreen('./image/alidndfailed.png') is not None:
                pyautogui.click(x=1197, y=470)
                time.sleep(1)
                pyautogui.moveTo(1058, 470, 0.25)
                pyautogui.dragTo(1363, 558, button='left', duration=0.25)
            else:
                pass

            # detected unusual traffic from your network (Drag n Drop)
            if pyautogui.locateOnScreen('./image/unusual_traffic.png') is not None:
                pyautogui.moveTo(671, 526, 0.2)
                pyautogui.dragTo(971, 528, button='left', duration=0.2)
            else:
                pass

            # Waiting for a Text to be appear
            wait(driver, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/button[1]/span', '充值') 

            time.sleep(1)
            
            # Extract credit
            while True:
                try:
                    credit = find_element_nontext(driver, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span')
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

            pyautogui.click(x= 1505, y=137)
            time.sleep(1)

            while True:
                try:
                    if find_element_XPATH(driver, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[8]/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]', "安全管控"):
                        break
                except:
                    pyautogui.click(x= 1183, y=192)
                    time.sleep(2)
                    pyautogui.click(x= 1505, y=137)
                    time.sleep(2)

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            logout_button = wait_buttonclick_XPATH(driver, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[8]/div[1]/header[2]/div[1]/div[1]/a[1]")
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
        
        if pyautogui.locateOnScreen('./image/ram.png') is not None:
                pyautogui.click(798, 651)
                wait(driver, '/html/body/div[1]/div/div[1]/nav/div/div/div/span', 'International - 简体中文') 
        else:
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
        
        wait(driver, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div', '账号密码登录')
        wait(driver, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div', '手机号登录')
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
        wait(driver, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/button[1]/span', '充值') 
        
        # Extract credit
        credit = find_element_nontext(driver, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span')
        
        # Replace
        credit = credit.replace('¥ ', '')
        credit = credit.replace(',', '')
       
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, credit)
        print(f"{ID[id]}= {credit}")
        
        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

        time.sleep(1)

        id += 1

        #IP 纯真社区版IP库离线下载
        driver.get('https://market.console.aliyun.com/?spm=a2c81.42099b4.products-recent.dmarket.75381127UzpKUg#/?_k=koc938')
        time.sleep(1)
        wait(driver, '/html/body/div[2]/div/div[3]/div/div/div[1]/div[4]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table[2]/tbody/tr/td[1]/p[1]', 'AppKey：') 
        time.sleep(1)
        wait(driver, '/html/body/div[2]/div/div[3]/div/div/div[1]/div[4]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table[2]/tbody/tr/td[1]/p[2]/a', '复制') 
        time.sleep(2)

        # Extract credit
        credit = find_element_nontext(driver, '/html/body/div[2]/div/div[3]/div/div/div[1]/div[4]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table[2]/tbody/tr/td[2]/span') 
                                                   
        A = re.findall(r'/(\d+)',credit)
        B = re.findall(r'(\d+)/',credit)

        A = [int(item) for item in A]
        B = [int(item) for item in B]
        
        credit = A[0] - B[0]

        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, str(credit))
        print(f"{ID[id]}= {credit}")

        pyautogui.moveTo(x= 1536, y=131)

        time.sleep(1)

        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        logout_button = wait_buttonclick_XPATH(driver, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[8]/div[1]/header[2]/div[1]/div[1]/a[1]")
        logout_button.click()
        
        id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)
        sys.exit(1)

# 阿里云【国际站】
def aliyun2(driver):

    id = tuple_id[2]
    X = 0
    Y = 0

    try:
        driver.get('https://account.alibabacloud.com/login/login.htm?oauth_callback=https://usercenter2-intl.aliyun.com/billing/#/account/overview')
        time.sleep(1)
        alilogin2 = pyautogui.locateOnScreen('./image/alilogin_text1.png')
        if alilogin2 is not None:
            pyautogui.click(alilogin2)
        else:
            pass

        time.sleep(2)

        if pyautogui.locateOnScreen('./image/ram.png') is not None:
            pyautogui.click(x=796, y=656)
            time.sleep(1)
        else:
            pass

        for i in range(34):
            while True:
                if pyautogui.locateOnScreen('./image/alilogin_text1.png') is not None:
                    if pyautogui.locateOnScreen('./image/alilogin_text2.png') is not None:
                        time.sleep(1)
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
            pyautogui.click(x=1216, y=175)
            time.sleep(1)
            pyautogui.click(x=913, y=542)
            time.sleep(4)
            
            # Drag and Drop Appear?
            if pyautogui.locateOnScreen('./image/alidnd.png') is not None:
                pyautogui.click(989,544)
                pyautogui.moveTo(m_X1[X], m_Y2[Y], 0.15)
                pyautogui.dragTo(d_X1[X], d_Y2[Y], button='left', duration=0.15)
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
                alidndfailed4 = pyautogui.locateOnScreen('./image/alidndfailed5.png')
                if alidndfailed4 is not None:
                    pyautogui.click(x=1111, y=543)
                    time.sleep(1)
                    pyautogui.click(989,544)
                    pyautogui.moveTo(m_X1[X], m_Y2[Y], 0.2)
                    pyautogui.dragTo(d_X1[X], d_Y2[Y], button='left', duration=0.2)
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
                pyautogui.moveTo(671, 526, 0.15)
                pyautogui.dragTo(981, 526, button='left', duration=0.15)
            else:
                pass
            
            wait(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[1]/span', '信用额度')
            wait(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/span', '状态')

            # Extract Credit
            while True:
                credit = find_element_nontext(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/span')
                if credit == "":
                    continue
                else:
                    break

            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            pyautogui.click(x= 1505, y=137)
            time.sleep(1)

            while True:
                try:
                    if find_element_XPATH(driver, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[8]/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]', '基本资料'):
                        break
                except:
                        pyautogui.moveTo(x= 1183, y=192)
                        time.sleep(2)
                        pyautogui.moveTo(x= 1505, y=137)
                        time.sleep(2)

            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            logout_button = wait_buttonclick_XPATH(driver, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[8]/div[1]/header[2]/div[1]/div[1]/a[1]")
            logout_button.click()

            time.sleep(1)
            
            id += 1
            if X >= 8:
                X = 0
                Y = 0
            
    
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)
        
# 阿里云【国际站】【RAM】
def aliyun3(driver):
    
    id = tuple_id[3]
    X = 0
    Y = 0
    
    try:
        driver.get('https://signin.alibabacloud.com/5256975880117898.onaliyun.com/login.htm?callback=https://usercenter2-intl.aliyun.com/billing/#/account/overview#/main')
        time.sleep(2)
        pyautogui.click(x=1280, y=433)
        
        for i in range(12):

            while True:
                if pyautogui.locateOnScreen('./image/next1.png') is not None:
                    break
                else:
                    time.sleep(1)
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
            pyautogui.click(x=798, y=529)
            time.sleep(3)

            # Drag and Drop Appear? #### Username Login
            alidnd3 = pyautogui.locateOnScreen('./image/alidnd.png')
            if alidnd3 is not None:
                pyautogui.moveTo(ram_m_X1[X], ram_m_Y2[Y], 0.2)
                pyautogui.dragTo(ram_d_X1[X], ram_d_Y2[Y], button='left', duration=0.2)
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
                    pyautogui.moveTo(ram_m_X1[X], ram_m_Y2[Y], 0.2)
                    pyautogui.dragTo(ram_d_X1[X], ram_d_Y2[Y], button='left', duration=0.2)
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
            wait(driver, '/html/body/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/form/div[5]/button/span', '登录')
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
            
            wait(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[1]/span', '信用额度')
            wait(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/span', '正常')

            # Extract Credit
            credit = find_element_nontext(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/span')
        
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")

            pyautogui.moveTo(x= 1521, y=143)
            time.sleep(1)

            while True:
                try:
                    if find_element_XPATH(driver, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[8]/div[1]/div[1]/div[2]/a[1]/span[1]/span[2]', "安全管控") :
                        break
                except:
                    pyautogui.click(x= 1183, y=192)
                    time.sleep(1)
                    pyautogui.moveTo(x= 1521, y=143)
                    time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            
            #Click Logout
            logout_button = wait_buttonclick_XPATH(driver, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[8]/div[1]/header[2]/div[1]/div[2]/a[1]")
            logout_button.click()
            time.sleep(2)
            
            id += 1
      
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(111111)

driver = chrome()
aliyun1(driver)
ven387(driver)
aliyun2(driver)
aliyun3(driver)
driver.close()
