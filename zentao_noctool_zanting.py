from datetime import datetime
from function import wait, find_element_ID, find_element_nontext, wait_buttonclick_XPATH, chrome
import time
import pyautogui
import pyperclip
import sys

# 关zentao和 暂停noctool工单
def zanting(driver):
    try:
        # Zentao_关单
        driver.get('https://zr-zentao2023.cccqx.com/zentao/execution-task-26.html')
        try:
            if find_element_ID(driver, 'loginPanel') is not None:
                time.sleep(1)
                pyautogui.click(805,615)
                time.sleep(1)
                pyautogui.click(805,582)          
        except:
            pass
        time.sleep(1)
        pyautogui.click(546,326)
        time.sleep(1)
        driver.switch_to.frame("appIframe-project")
        wait(driver, '/html/body/main/div/div[2]/div[2]/a[6]/span', '目标变更')
        time.sleep(1)
        pyautogui.click(559,321)
        driver.switch_to.frame("iframe-triggerModal")
        wait(driver, '/html/body/main/div/div[2]/div[1]/div[1]/div/div[1]', '任务描述')

        # Extract Gongdan Number
        gongdan_number = find_element_nontext(driver, "/html/body/main/div/div[1]/div/div/span[2]")
        
        pyautogui.click(681,690)
        time.sleep(1)
        pyautogui.click(602,294)
        pyautogui.write("1")
        time.sleep(1)
        pyautogui.click(641,383)
        pyautogui.write(str(datetime.today().date())+ " ")
        pyautogui.write(str(datetime.now().strftime("%H:%M")))    
        time.sleep(1)
        pyautogui.click(835,723)
        time.sleep(2)
        
        # Noctool_关单
        driver.get("http://10.77.1.196/workorders/list/default/")
        wait(driver, '/html/body/div/div/main/div/h3', '案件列表')
        time.sleep(1)
        pyautogui.click(1476,256)
        time.sleep(1)
        pyperclip.copy(gongdan_number)
        pyautogui.hotkey("Command", "V")
        wait(driver, '/html/body/div/div/main/div/div/div[2]/div/table/tbody/tr/td[4]', '內部專案')
        time.sleep(1)
        pyautogui.click(569,385)
        time.sleep(1)
        pyautogui.scroll(-30)
        time.sleep(1)
        pyautogui.click(362,328)
        time.sleep(1)
        zan_ting_zhong = pyautogui.locateOnScreen('./image/pause.png')
        pyautogui.click(zan_ting_zhong)
        time.sleep(1)
        pyautogui.click(632,500)
        time.sleep(1)
        pyperclip.copy("暂停中")
        pyautogui.hotkey("Command", "V")
        time.sleep(1)
        # Special Case for Button Click
        button_click = wait_buttonclick_XPATH(driver, "/html/body/div[1]/div/main/div/div[4]/form/button[1]")
        button_click.click()
        time.sleep(2)
    

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

driver = chrome()
zanting(driver)
driver.close()