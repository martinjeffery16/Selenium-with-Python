from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


#start the session and navitage to heroku web page
serv = Service("C:\Program Files\chromedriver_win32\chromedriver.exe ")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=serv, options=op)
wait = WebDriverWait(driver,20)
action = ActionChains(driver)
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()


#select option1
dropselect = Select(wait.until(EC.element_to_be_clickable((By.TAG_NAME,"select"))))
dropselect.select_by_value('1')

#Sleep for 3 secs
time.sleep(5)

#select option 2
dselect2 = Select(wait.until(EC.element_to_be_clickable((By.TAG_NAME,"select"))))
dselect2.select_by_value('2')




