import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from keys import linkedin_email, linkedin_password

url="https://www.linkedin.com/jobs/search/?currentJobId=3100050203&f_E=2%2C3%2C4&f_JT=F&f_WT=2&geoId=103644278&keywords=data%20engineer%20advertising&location=United%20States"

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(url)

sign_in1 = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]")
sign_in1.click()
email_input=driver.find_element(By.NAME, "session_key")
password_input=driver.find_element(By.NAME, "session_password")
sign_in2 = driver.find_element(By.CSS_SELECTOR,"#organic-div > form > div.login__form_action_container > button")
email_input.send_keys(linkedin_email)
password_input.send_keys(linkedin_password)
time.sleep(2)
sign_in2.click()




time.sleep(5)

driver.quit()