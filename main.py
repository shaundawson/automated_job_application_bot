import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from keys import CHROME_BINARY_LOC, CHROME_DRIVER_PATH, CHROME_PROFILE_PATH, EMAIL, PASSWORD
from selenium.common.exceptions import NoSuchElementException
import random

def pause():
    time_break = random.randint(4,9)
    return time.sleep(time_break)

url="https://www.linkedin.com/jobs/search/?distance=25.0&f_AL=true&f_F=eng&f_I=80%2C28%2C36&f_JT=F&f_TPR=r604800&f_WT=2&geoId=103644278&keywords=data%20engineer%20ad&location=United%20States&sortBy=R"

s=Service(executable_path=CHROME_DRIVER_PATH)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
chrome_options.binary_location=(CHROME_BINARY_LOC)
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
driver.get(url)
pause()

def sign_in():
    try:
        sign_in = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]")
        sign_in.click()
        pause()
        member_profile = driver.find_element(By.CLASS_NAME,"member-profile-block")
        member_profile.click()
        pause()
    except:
       pass
          
sign_in()
all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    pause()

#Try to locate the apply button, if can't locate then skip the job.
    try:
        easy_apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        easy_apply_btn.click()
        pause()
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        
        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.text != "Submit application":
            close_button=driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()
            save_button = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div[3]/button[2]")
            save_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
            print("Submitted the application")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
        #Once application completed, close the pop-up window.
        pause()
        close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
        close_button.click()
        (pause)
    
    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        pass

pause()
driver.quit()
