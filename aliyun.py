import time                                                                                            
import pyautogui                                                                                                                                                                                  
import sys                                                                                                                                      
from List_Zentao import ID, mongodb_id,tuple_id                                                       
from List_Aliyun_DDCaptcha import m_X1,m_Y2,d_X1,d_Y2,ram_d_X1,ram_d_Y2,ram_m_X1,ram_m_Y2              
from PIL import ImageGrab  
from bson.objectid import ObjectId                                                                  
from function import chrome, update_one, wait, find_element_XPATH, find_element_nontext, wait_buttonclick_XPATH

# 阿里云【中国站】
def aliyun1(driver):  
    
    id = tuple_id[0]
    
    try:
        driver.get('https://account.aliyun.com/login/login.htm?oauth_callback=https://usercenter2.aliyun.com/home')
        time.sleep(1)

        try:
            if find_element_nontext(driver, "/html/body/div[2]/div[1]/div[2]/div/div/div[1]/div/div/h3") == "RAM 用户登录": 
                    pyautogui.click(798, 632)
                    wait(driver, '/html/body/div[1]/div/div[1]/nav/div/div/div/span', 'International - 简体中文') 
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
                pyautogui.moveTo(1058, 460, 0.2)
                pyautogui.dragTo(1453, 545, button='left', duration=0.2)
            else:
                pass
            
            time.sleep(2)
            
            # Drag and Drop Failed
            if pyautogui.locateOnScreen('./image/alidndfailed.png') is not None:
                pyautogui.click(x=1197, y=457)
                time.sleep(1)
                pyautogui.moveTo(1058, 457, 0.25)
                pyautogui.dragTo(1363, 545, button='left', duration=0.25)
            else:
                pass

            # detected unusual traffic from your network (Drag n Drop)
            if pyautogui.locateOnScreen('./image/unusual_traffic.png') is not None:
                pyautogui.moveTo(669, 526, 0.2)
                pyautogui.dragTo(956, 526, button='left', duration=0.2)
            else:
                pass


            # Extract credit
            # This is due to VEN407 aliyun China UI CHANGE
            if i == 1:
                # Waiting for a Text to be appear
                wait(driver, '/html/body/div[2]/div[1]/div[3]/div/ali-alfa-cloudservice-xusercenter-widget-home/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[3]/button[1]/span', '充值') 

                time.sleep(1)

                while True:
                    try:
                        credit = find_element_nontext(driver, '/html/body/div[2]/div[1]/div[3]/div/ali-alfa-cloudservice-xusercenter-widget-home/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/span')
                    except:
                        driver.refresh()
                        time.sleep(5)
                        continue
                    break
            
            # VEN338 Aliyun China remain same no change
            else:
                # Waiting for a Text to be appear
                wait(driver, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/button[1]/span', '充值') 
                
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

            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_XPATH(driver, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[11]/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]', "安全管控"):
                        break
                except:
                    pyautogui.click(x= 1183, y=192)
                    time.sleep(2)
                    pyautogui.click(x= 1505, y=104)
                    time.sleep(2)

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            logout_button = wait_buttonclick_XPATH(driver, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[11]/div[1]/header[2]/div[1]/div[1]/a[1]")
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
        wait(driver, '/html/body/div[2]/div[1]/div[3]/div/ali-alfa-cloudservice-xusercenter-widget-home/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[3]/button[1]/span', '充值') 
        
        time.sleep(1)

        while True:
                    try:
                        credit = find_element_nontext(driver, '/html/body/div[2]/div[1]/div[3]/div/ali-alfa-cloudservice-xusercenter-widget-home/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/span')
                    except:
                        driver.refresh()
                        time.sleep(5)
                        continue
                    break
        
        # Replace
        credit = credit.replace('¥ ', '')
        credit = credit.replace(',', '')
       
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, credit)
        print(f"{ID[id]}= {credit}")

        while True:
                try:
                    if find_element_XPATH(driver, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[11]/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]', "安全管控"):
                        break
                except:
                    pyautogui.click(x= 1183, y=192)
                    time.sleep(2)
                    pyautogui.click(x= 1505, y=104)
                    time.sleep(2)
        
        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        time.sleep(1)

        id += 1

        #IP 纯真社区版IP库离线下载
        driver.get('https://market.console.aliyun.com/?spm=a2c81.42099b4.products-recent.dmarket.75381127UzpKUg#/?_k=koc938')
        wait(driver, '/html/body/div[2]/div/div[3]/div/div/div[1]/div[4]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table[2]/tbody/tr/td[1]/p[1]', 'AppKey：') 
        wait(driver, '/html/body/div[2]/div/div[3]/div/div/div[1]/div[4]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table[2]/tbody/tr/td[1]/p[2]/a', '复制') 
        time.sleep(2)

        # Extract credit
        credit = find_element_nontext(driver, '/html/body/div[2]/div/div[3]/div/div/div[1]/div[4]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table[2]/tbody/tr/td[2]/span/span') 
                                                
        # MongoDB update Data 
        mangos_id = {'_id': ObjectId(mongodb_id[id])}
        update_one(mangos_id, str(credit))
        print(f"{ID[id]}= {credit}")

        pyautogui.moveTo(x= 1536, y=131)

        time.sleep(1)

        # Screenshot
        ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
        logout_button = wait_buttonclick_XPATH(driver, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[11]/div[1]/header[2]/div[1]/div[1]/a[1]")
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
        time.sleep(2)

        if pyautogui.locateOnScreen('./image/ram.png') is not None:
            pyautogui.click(x=796, y=634)
            time.sleep(1)
        else:
            pass

        for i in range(35):
            
            # Refresh
            with pyautogui.hold('command'):
                pyautogui.press('r')

            time.sleep(2)

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
            pyautogui.click(x=913, y=525)
            time.sleep(4)
            
            # Drag and Drop Appear?
            if pyautogui.locateOnScreen('./image/alidnd.png') is not None:
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
                    pyautogui.click(x=1111, y=511)
                    time.sleep(1)
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
                    break

            # detected unusual traffic from your network (Drag n Drop)
            if pyautogui.locateOnScreen('./image/unusual_traffic.png') is not None:
                pyautogui.moveTo(660, 507, 0.15)
                pyautogui.dragTo(970, 507, button='left', duration=0.20)
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

            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_XPATH(driver, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]', '基本资料'):
                        break
                except:
                        pyautogui.moveTo(x= 1183, y=162)
                        time.sleep(2)
                        pyautogui.moveTo(x= 1505, y=104)
                        time.sleep(2)

            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            logout_button = wait_buttonclick_XPATH(driver, "//html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/header[2]/div[1]/div[1]/a[1]")
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
            
            # Refresh
            with pyautogui.hold('command'):
                pyautogui.press('r')
            
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
            pyautogui.click(x=792, y=507)
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

            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_XPATH(driver, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/div[1]/div[2]/a[1]/span[1]/span[2]', "安全管控") :
                        break
                except:
                    pyautogui.click(x= 1183, y=104)
                    time.sleep(1)
                    pyautogui.click(x= 1505, y=104)
                    time.sleep(1)
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            
            #Click Logout
            logout_button = wait_buttonclick_XPATH(driver, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/header[2]/div[1]/div[2]/a[1]")
            logout_button.click()
            time.sleep(2)
            
            id += 1
      
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(111111)

# watermelon【国际站】【RAM】
def watermelon_1(driver):

    id = tuple_id[16]
    X = 0
    Y = 0
    
    try:
        driver.get('https://signin.alibabacloud.com/5099316222832876.onaliyun.com/login.htm?callback=https://usercenter2-intl.aliyun.com/billing/#/account/overview#/main')
        time.sleep(2)
        pyautogui.click(x=1280, y=433)
        
        for i in range(9):
            
            # Refresh
            with pyautogui.hold('command'):
                pyautogui.press('r')
            
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
            pyautogui.click(x=792, y=507)
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
            
            time.sleep(1)

            # 启用 MFA 设备
            try:
                if find_element_nontext(driver, "/html/body/div[2]/div[1]/div[2]/div/div/div/h3") == "启用 MFA 设备":
                        wait(driver, '/html/body/div[2]/div[1]/div[2]/div/div/div/form/div[3]/div/div/div', '您当前的登录存在安全风险，请绑定 MFA 设备。')
                        pyautogui.click(918,612)
            except:
                pass

            wait(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/span', '本月消费概览')
            time.sleep(1)

            # Check if overdue payment
            if pyautogui.locateOnScreen('./image/overdue.png') is not None:
                print(f"{ID[id]}= !!!!! OVERDUE !!!")
            else:
                pass

            # Screenshot
            ImageGrab.grab().save('./watermelon/' + ID[id] + '.png')

            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_XPATH(driver, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/div[1]/div[2]/a[1]/span[1]/span[2]', "安全管控") :
                        break
                except:
                    pyautogui.click(x= 1183, y=104)
                    time.sleep(1)
                    pyautogui.click(x= 1505, y=104)
                    time.sleep(1)
            
            # Click Logout
            logout_button = wait_buttonclick_XPATH(driver, "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/header[2]/div[1]/div[2]/a[1]")
            logout_button.click()
            time.sleep(2)
            
            id += 1
      
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(111111)

# watermelon 【国际站】
def watermelon_2(driver):

    id = tuple_id[17]
    X = 0
    Y = 0

    try:
        driver.get('https://account.alibabacloud.com/login/login.htm?oauth_callback=https://usercenter2-intl.aliyun.com/billing/#/account/overview')
        time.sleep(2)

        if pyautogui.locateOnScreen('./image/ram.png') is not None:
            pyautogui.click(x=796, y=634)
            time.sleep(1)
        else:
            pass

        for i in range(3):

            # Refresh
            with pyautogui.hold('command'):
                pyautogui.press('r')

            time.sleep(2)

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
            pyautogui.click(x=913, y=525)
            time.sleep(4)
            
            # Drag and Drop Appear?
            if pyautogui.locateOnScreen('./image/alidnd.png') is not None:
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
                    pyautogui.click(x=1111, y=511)
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
                pyautogui.moveTo(671, 506, 0.15)
                pyautogui.dragTo(981, 506, button='left', duration=0.15)
            else:
                pass
            
            wait(driver, '//html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/span', '本月消费概览')
            time.sleep(1)

            # Check if overdue payment
            if pyautogui.locateOnScreen('./image/overdue.png') is not None:
                print(f"{ID[id]}= !!!!! OVERDUE !!!")
            else:
                pass

            # Screenshot
            ImageGrab.grab().save('./watermelon/' + ID[id] + '.png')

            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if find_element_XPATH(driver, '/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]', '基本资料'):
                        break
                except:
                        pyautogui.moveTo(x= 1183, y=162)
                        time.sleep(2)
                        pyautogui.moveTo(x= 1505, y=104)
                        time.sleep(2)

            # Logout
            logout_button = wait_buttonclick_XPATH(driver, "//html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/header[2]/div[1]/div[1]/a[1]")
            logout_button.click()

            time.sleep(1)
            
            id += 1
            if X >= 8:
                X = 0
                Y = 0
            
    
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

driver = chrome()
aliyun1(driver)
ven387(driver)
aliyun2(driver)
aliyun3(driver)
watermelon_1(driver)
watermelon_2(driver)
driver.close()
