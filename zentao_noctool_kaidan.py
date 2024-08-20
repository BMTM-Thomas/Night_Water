from function import wait, find_element_nontext, find_element_ID, find_element_nontext, chrome
import time
import pyautogui
import pyperclip

night = " #晚班週期性業務"

# 开zentao和noctool工单
def kaidan(driver):
    try:
        # 拿SN码
        driver.get('https://ticket.big555.net/')
        time.sleep(1)
        pyautogui.click(134,129)
        time.sleep(1)
        pyautogui.click(124,258)
        time.sleep(1)
        SN = find_element_nontext(driver, '/html/body/div[2]')
        pyperclip.copy(SN + " 晚班週期性業務")


        # Zentao_开单
        driver.get('https://zr-zentao2023.cccqx.com/zentao/task-create-26-0-0-14936.html?')
        try:
            if find_element_ID(driver, 'loginPanel') is not None:
                time.sleep(1)
                pyautogui.click(804,558)          
        except:
            pass
        time.sleep(1)
        driver.switch_to.frame("appIframe-project")
        wait(driver, '/html/body/main/div/div/div/div/h2', '建任务') 
        time.sleep(1)
        pyautogui.moveTo(305,542)
        pyautogui.mouseDown()
        pyautogui.moveTo(585,542)
        pyautogui.mouseUp()
        time.sleep(1)
        pyautogui.hotkey("Command", "V")
        time.sleep(1)
        pyautogui.scroll(-30)
        time.sleep(1)
        pyautogui.click(758,694)
        time.sleep(2)
        
        # Noctool_开单
        driver.get('http://10.77.1.196/workorders/create/')
        time.sleep(1)

        # Check if is in 登入系统
        try:
            if find_element_nontext(driver, "/html/body/div[1]/div/article/h4") == "登入系統":
                wait(driver, "/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/h4", "最新通知")
                time.sleep(1)
                driver.get("http://10.77.1.196/workorders/create/")
                time.sleep(1)
        except:
            pass

        pyautogui.click(468,200)
        time.sleep(1)
        pyautogui.click(142,307)
        time.sleep(1)
        pyautogui.click(213,403)
        pyautogui.hotkey("Command", "V")
        time.sleep(1)
        pyautogui.click(357,529)
        time.sleep(1)
        pyperclip.copy("处理中")
        pyautogui.hotkey("Command", "V")
        time.sleep(1)
        pyautogui.click(35,695)
        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(111111)

driver = chrome()
kaidan(driver)
driver.close()