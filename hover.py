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
from webdriver_manager.drivers.chrome import ChromeDriver

#start the session and initialize the objects
ser = Service("C:\Program Files\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser,options=op)
wait = WebDriverWait(driver,60)
action = ActionChains(driver)

#navigate to a webpage
driver.get("http://the-internet.herokuapp.com/hovers")
driver.maximize_window()

#find the element to hover over the image 
elementslist = driver.find_elements(By.XPATH,"//body/div[2]/div[1]/div[1]/*")
time.sleep(5)

for element in elementslist: 
        action.move_to_element(element).perform()
        time.sleep(1)
        
#close browser
driver.close()