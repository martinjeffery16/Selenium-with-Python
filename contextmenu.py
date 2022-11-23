from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

#start the automation session
serv = Service("C:\Program Files\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=serv, options=op)
action = ActionChains(driver)
wait= WebDriverWait(driver,50)
alert = Alert(driver)

#navigate to the web page
driver.get("http://the-internet.herokuapp.com/context_menu")
driver.maximize_window()
#identify element
el = driver.find_element(By.XPATH,"//div[@id='hot-spot']")

#move the mouse over element

action.move_to_element(el).perform()

#perform right-click

action.context_click().perform()
time.sleep(3)



#swtich to alert
driver.switch_to.alert

#print alert text 

print(alert.text)

#Accept the popup alert(select ok)
alert.accept()
time.sleep(3)

#end the session
driver.close()


#