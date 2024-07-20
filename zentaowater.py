import time
import pyautogui
import sys
import pyperclip
from AppKit import NSPasteboard, NSPasteboardTypePNG
from PIL import ImageGrab
from List_Zentao import ID, mongodb_id
from bson.objectid import ObjectId   
from function import chrome, find_element_ID, wait_buttonclick_XPATH, find_one

# zentao
def zentao(driver):
    
    try:
        # Go to Webpage
        driver.get('https://zr-zentao2023.cccqx.com/zentao/execution-task-26.html')
        try:
            if find_element_ID(driver, 'loginPanel') is not None:
                time.sleep(1)
                pyautogui.click(1420,62)

                # Wait for image Appear
                image_vault = None
                while image_vault is None:
                    image_vault = pyautogui.locateOnScreen('./image/vault.png', grayscale = True)
                print("Lastpass Image Vault Loaded") 

                time.sleep(1)
                pyautogui.click(1176,212)   
                time.sleep(1)
                pyautogui.click(805,577)    
                time.sleep(1)   
                pyautogui.click(805,577)   
        except:
            pass


        while True:
                mynoc = pyautogui.locateOnScreen('./image/mynoc.png')
                if mynoc is not None:
                    break
                else:
                    pass
                
        pyautogui.click(x=1509, y=315)

        while True: 
            remark = pyautogui.locateOnScreen('./image/remark.png')
            if remark is not None:
                break
            else:
                pass
        pyautogui.click(x=1468, y=722)
        time.sleep(1)
        pyautogui.click(x=729, y=737)
        time.sleep(1) 
        pyautogui.press('enter', presses = 8)
        time.sleep(1)
        pyautogui.click(x=600, y=644)

        id = 0
        for y in range(100): #100
            mangos_id = {'_id': ObjectId(mongodb_id[id])}
            documents = find_one(mangos_id)
            ven_machine_value = documents.get('Ven_Machine','N/A')
            credit_value = documents.get('Credit', 'N/A') 
            unit_value = documents.get('Unit', 'N/A')
            merge = ven_machine_value + " " + credit_value + " " + unit_value

            pyperclip.copy(merge)
            pyautogui.hotkey("command", "v")
    
            # Create an instance of the NSPasteboard class
            pasteboard = NSPasteboard.generalPasteboard()

            # Read image data from the file
            with open("./晚班水位/"+ID[id]+".png", 'rb') as file:
                image_data = file.read()

            # Copy the image data to the clipboard as a PNG
            if image_data:
                pasteboard.declareTypes_owner_([NSPasteboardTypePNG], None)
                pasteboard.setData_forType_(image_data, NSPasteboardTypePNG)
                print(ID[id]+" Image copied to clipboard.")
                
            else:
                print("Failed to read image data from the file.")

            # Paste Image
            pyautogui.keyDown('command')
            pyautogui.press('v')

            # Next Line
            pyautogui.press('enter', presses = 2)
            time.sleep(1)

            y+=1
            id+=1

        time.sleep(1)

        # Special Case for Button Click
        driver.switch_to.frame("appIframe-project")
        save_button = wait_buttonclick_XPATH(driver, "/html/body/main/div/div/form/div[2]/div[1]/div/div[5]/button")
        save_button.click()
        time.sleep(3)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

driver = chrome()
zentao(driver)
driver.close()
