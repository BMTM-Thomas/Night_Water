from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from List_Zentao import ID
from PIL import ImageGrab
import time
import sys

def main():
    options=Options()
    options.add_argument("--user-data-dir=\\Users\\Thomas\\Library\\Application Support\\Google\\Chrome\\")
    options.add_argument('profile-directory=Profile 3')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized") 
    options.add_argument("--remote-debugging-port=9222")
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

# Change Account
def kaidan(driver):
    try:
        # 拿SN码
        driver.get('http://10.77.1.196/accounts/login/')
        time.sleep(1111111)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
