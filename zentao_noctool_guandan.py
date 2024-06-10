from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from List_Zentao import ID
from zentao_noctool_kaidan import kaidan
from datetime import datetime
from PIL import ImageGrab
import time
import pyautogui
import pyperclip
import sys

night = " #晚班週期性業務"
def main():
    options=Options()
    options.add_argument('--user-data-dir=\\Users\\n02-19\\Library\\Application Support\\Google\\Chrome\\')
    options.add_argument('profile-directory=Default')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized') 
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    driver=webdriver.Chrome(options=options)
    guandan(driver)
    driver.quit()

def wait(driver, path, text):
    try:
        WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# 关zentao和noctool工单
def guandan(driver):
    try:
        # Zentao_关单
        driver.get('https://zr-zentao2023.cccqx.com/zentao/execution-task-26.html')
        try:
            if driver.find_element(By.ID, 'loginPanel') is not None:
                time.sleep(1)
                pyautogui.click(805,615)
                time.sleep(1)
                pyautogui.click(805,582)          
        except:
            pass
        time.sleep(1)
        pyautogui.click(557,319)
        time.sleep(1)
        driver.switch_to.frame("appIframe-project")
        wait(driver, '/html/body/main/div/div[2]/div[2]/a[6]/span', '目标变更')
        time.sleep(1)
        pyautogui.click(559,321)
        driver.switch_to.frame("iframe-triggerModal")
        wait(driver, '/html/body/main/div/div[2]/div[1]/div[1]/div/div[1]', '任务描述')
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
        time.sleep(1)
        
        # Noctool_关单
        with open('link_copy.txt', 'r') as file:
            file_contents = file.read()
        driver.get(file_contents)
        time.sleep(1)
        pyautogui.click(445,597)
        time.sleep(1)
        pyautogui.click(357,546)
        time.sleep(1)
        pyautogui.click(614,768)
        time.sleep(1)
        pyperclip.copy("检查完毕")
        pyautogui.hotkey("Command", "V")
        time.sleep(1)
        pyautogui.scroll(-30)
        time.sleep(1)
        pyautogui.click(287,732)
    

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# guandan_shortcut = main()

if __name__ == "__main__":
    main()
