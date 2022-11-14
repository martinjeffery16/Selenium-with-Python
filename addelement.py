from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

#start the session and navitage to heroku web page
serv = Service("C:\Program Files\chromedriver_win32\chromedriver.exe ")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=serv, options=op)
wait = WebDriverWait(driver,60)
action = ActionChains(driver)
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()

#add new element
element = wait.until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/button[1]")))
action.move_to_element(element).click().perform()

#remove new element
l = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Delete')]")))
action.move_to_element(l).click().perform()



