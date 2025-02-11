import time                                                                                            
import pyautogui                                                                                                                                                                                                                                                                                                            
from List_Zentao import ID, mongodb_id,tuple_id                                                       
from List_Aliyun_DDCaptcha import m_X1,m_Y2,d_X1,d_Y2          
from PIL import ImageGrab  
from bson.objectid import ObjectId                                               
from DrissionPage import ChromiumOptions, ChromiumPage            
from DrissionPage.common import Settings
from function import update_one
from function import find_element_nontext, wait

co = ChromiumOptions()
co.set_argument('--user-data-dir=\\Users\\n02-19\\Library\\Application Support\\Google\\Chrome\\')
co.set_argument('--disable-blink-features=AutomationControlled')
co.set_argument('--no-sandbox')
co.set_argument('--start-maximized')
co.set_argument('--disable-gpu')
co.set_argument('--disable-dev-shm-usage')
co.set_argument('--remote-debugging-port=9222')
co.set_argument('--no-default-browser-check')
co.set_argument('--no-first-run')
co.set_argument('--hide-crash-restore-bubble')
co.set_argument("--disable-blink-features=AutomationControlled")

driver = ChromiumPage(co)

# 阿里云【国际站】
def aliyun2(driver):
    
    id = tuple_id[2]
    X = 0
    Y = 0

    try:
        driver.get('https://account.alibabacloud.com/login/login.htm?oauth_callback=https://usercenter2-intl.aliyun.com/billing/#/account/overview')
        time.sleep(1)
        pyautogui.click(x=1576, y=115)
        time.sleep(1)

        if pyautogui.locateOnScreen('./image/ali_Eng.png') is not None:
            pyautogui.click(x=1246, y=118)
            time.sleep(1)
            pyautogui.click(x=1235, y=186)
            time.sleep(1)
        else:
            pass

        for i in range(31):

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
            pyautogui.click(x=1361, y=62)

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
            
            driver.wait.doc_loaded()
            time.sleep(2)
            
            # Extract Credit
            while True:
                credit = driver('x:/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/span', timeout=200).text
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
                    if driver('x:/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]', timeout=2).text == '基本资料':
                        break
                except:
                    pyautogui.moveTo(x= 1183, y=162)
                    time.sleep(2)
                    pyautogui.moveTo(x= 1505, y=104)
                    time.sleep(2)
                

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

            # Element Button Click
            time.sleep(1)
            driver('x:/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/header[2]/div[1]/div[1]/a[1]').click()

            time.sleep(1)
            
            id += 1
            if X >= 8:
                X = 0
                Y = 0
    
            driver.wait.doc_loaded()

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
        pyautogui.click(x=1576, y=115)
        time.sleep(1)

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
            pyautogui.click(x=1361, y=62)

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

            driver.wait.doc_loaded()
            wait(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/span', '本月消费概览')
            time.sleep(2)

            # Check if overdue payment
            try:
                if pyautogui.locateOnScreen('./image/overdue.png') is not None:
                    overdue = find_element_nontext(driver, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/p/span')
                    print(f"{ID[id]}= ", overdue)
            except:
                pass

            pyautogui.click(x= 1505, y=104)
            time.sleep(1)

            while True:
                try:
                    if driver('x:/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]', timeout=2).text == '基本资料':
                        break
                except:
                    pyautogui.moveTo(x= 1183, y=162)
                    time.sleep(2)
                    pyautogui.moveTo(x= 1505, y=104)
                    time.sleep(2)
                

            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')

            # Element Button Click
            time.sleep(1)
            driver('x:/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/div[10]/div[1]/header[2]/div[1]/div[1]/a[1]').click()

            time.sleep(1)
            
            id += 1
            if X >= 8:
                X = 0
                Y = 0
    
            driver.wait.doc_loaded()

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(11111)

aliyun2(driver)
watermelon_2(driver)
driver.quit()
