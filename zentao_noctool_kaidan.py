from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from List_Zentao import ID
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
    options.add_argument("--hide-crash-restore-bubble")
    options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    driver=webdriver.Chrome(options=options)
    kaidan(driver)
    driver.quit()

def wait(driver, path, text):
    try:
        WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.XPATH, path), text))
    except:
        pass

# 开zentao和noctool工单
def kaidan(driver):
    try:
        # 拿SN码
        driver.get('https://ad.bgvip88.com/ticket.html')
        time.sleep(1)
        pyautogui.click(139,163)
        time.sleep(1)
        pyautogui.click(74,292)
        time.sleep(1)
        SN = driver.find_element(By.XPATH, value='/html/body/div[2]').get_attribute('textContent')  
        pyperclip.copy(SN + " 晚班週期性業務")


        # Zentao_开单
        driver.get('https://zr-zentao2023.cccqx.com/zentao/task-create-26-0-0-14936.html?')
        try:
            if driver.find_element(By.ID, 'loginPanel') is not None:
                time.sleep(1)
                pyautogui.click(805,582)          
        except:
            pass
        time.sleep(1)
        driver.switch_to.frame("appIframe-project")
        wait(driver, '/html/body/main/div/div/div/div/h2', '建任务') 
        time.sleep(1)
        pyautogui.moveTo(305,574)
        pyautogui.mouseDown()
        pyautogui.moveTo(585,574)
        pyautogui.mouseUp()
        time.sleep(1)
        pyautogui.hotkey("Command", "V")
        time.sleep(1)
        pyautogui.scroll(-30)
        time.sleep(1)
        pyautogui.click(757,703)
        time.sleep(1)
        
        # Noctool_开单
        with open('link_copy.txt', 'w') as file:
            pass

        driver.get('http://10.77.1.196/workorders/create/')
        time.sleep(1)
        pyautogui.click(447,235)
        time.sleep(1)
        pyautogui.click(140,340)
        time.sleep(1)
        pyautogui.click(370,436)
        pyautogui.hotkey("Command", "V")
        time.sleep(1)
        pyautogui.click(248,529)
        time.sleep(1)
        pyperclip.copy("处理中")
        pyautogui.hotkey("Command", "V")
        time.sleep(1)
        pyautogui.click(37,730)
        time.sleep(1)
        pyautogui.hotkey('command', 'l')
        time.sleep(1)
        pyautogui.hotkey('command', 'c')
        time.sleep(1)
        copy_link = pyperclip.paste()
        with open('link_copy.txt', 'a') as file:
            file.write(copy_link)


    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(111111)

# kaidan_shortcut = main()

if __name__ == "__main__":
    main()
