import time
import pyautogui
import sys
from List_Zentao import ID, mongodb_id, tuple_id 
from PIL import ImageGrab
from bson.objectid import ObjectId  
from function import chrome, update_one, wait, find_element_XPATH, find_element_nontext

# Ucloud
def ucloud(driver):

    id = tuple_id[10]
    id_Range = tuple_id[11] - tuple_id[10]
    
    try:
        # Go to Webpage
        driver.get('https://passport.ucloud.cn/#login')

        time.sleep(1)

        for i in range(id_Range):
            wait(driver, '/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]', '账号登录') 
            time.sleep(1)
            pyautogui.click(x=1416, y=62)

            # Wait for image Appear
            image_vault = None
            while image_vault is None:
                image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)

            time.sleep(1)
            pyautogui.write(ID[id])
            time.sleep(1)
            pyautogui.click(x=1227, y=157)
            time.sleep(1)
            pyautogui.click(x=634, y=578)
            time.sleep(1)

            while True:
                ucloudhelp = pyautogui.locateOnScreen('./image/ucloudhelp.png')
                if ucloudhelp is not None:
                    break
                else:
                    time.sleep(2)
                
            pyautogui.click(x=1558, y=107)
            time.sleep(1)
            
            while True:
                if pyautogui.locateOnScreen('./image/ucloudlogout_detect.png') is not None:
                    break
                else:
                    time.sleep(2)


            # Extract Credit
            try:
                credit = find_element_nontext(driver, '/html/body/div[13]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/span[1]')
            except:
                credit = find_element_nontext(driver, '/html/body/div[11]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/span[1]')
            credit = credit.replace(',', '')
            
            # MongoDB update Data 
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            update_one(mangos_id, credit)
            print(f"{ID[id]}= {credit}")
            
            # Screenshot
            ImageGrab.grab().save('./晚班水位/' + ID[id] + '.png')
            time.sleep(1)
            ucloudlogout = pyautogui.locateOnScreen('./image/ucloudlogout.png')
            if ucloudlogout is not None:
                pyautogui.click(ucloudlogout)
                time.sleep(2)
            else:
                pass

            id += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

driver = chrome()
ucloud(driver)
driver.close()