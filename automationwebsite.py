from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser

ser = Service("C:\Program Files\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)
action = ActionChains(s)
wait = WebDriverWait(s,60)
s.get("http://www.automationpractice.com/index.php")
s.maximize_window()

#identify the xpath of signin,username in webpage
wait.until(EC.presence_of_element_located((By.XPATH,"//a[contains(text(),'Sign in')]"))).click()
username = "martinjefferyaus@gmail.com"
password = "Tcei@n59"

ulocator = (By.XPATH,"//input[@id='email']")
element_username = wait.until(EC.presence_of_element_located(ulocator))
element_username.send_keys(username)

#identify the xpath of password in webpage
plocator = (By.XPATH,"//input[@id='passwd']")
element_password = wait.until(EC.presence_of_element_located(plocator))
element_password.send_keys(password)
element_password.send_keys(Keys.RETURN)

#Use searchbox to find the product you want to order
ecomm_searchbox = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='search_query_top']")))
action.move_to_element(ecomm_searchbox).click().perform()
ecomm_searchbox.send_keys("Faded Short Sleeve T-shirts")
ecomm_searchbox.send_keys(Keys.ENTER)

#Add the product to cart

ecomm_pic = wait.until(EC.element_to_be_clickable((By.XPATH,"//body/div[@id='page']/div[2]/div[1]/div[3]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[1]/a[1]/img[1]")))
action.move_to_element(ecomm_pic).click().perform()
ecomm_addtocart = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Add to cart')]")))
action.move_to_element(ecomm_addtocart).click().perform()

#Proceed to checkout 

ecomm_checkout = wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/div[4]/a[1]/span[1]")))
action.move_to_element(ecomm_checkout).click().perform()


#Shopping cart summary: Checkout 
frame = s.find_element(By.XPATH, "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/p[2]/a[1]/span[1]")
action.scroll_to_element(frame).perform()
ecomm_summary = wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/p[2]/a[1]/span[1]")))
action.move_to_element(ecomm_summary).click().perform()

#Shopping cart summary: Address

aframe = s.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/p[1]/button[1]/span[1]")
action.scroll_to_element(aframe).perform()
ecomm_address = wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/p[1]/button[1]/span[1]")))
action.move_to_element(ecomm_address).click().perform()

#Shopping cart summary: shipping
sframe = s.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/p[1]/button[1]/span[1]")
action.scroll_to_element(sframe).perform()
s.find_element(By.ID,'cgv').click()
ecomm_shipping = wait.until(EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/p[1]/button[1]/span[1]")))
action.move_to_element(ecomm_shipping).click().perform()           
                            
#Shopping cart summary: payment 

pframe = s.find_element(By.XPATH,"//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/p[1]/a[1]")
action.scroll_to_element(pframe).perform()
ecomm_payment = wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/p[1]/a[1]")))
action.move_to_element(ecomm_payment).click().perform()
   
#Shopping cart summary: orderconfirmation

oframe =  s.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/p[1]/button[1]/span[1]")
action.scroll_to_element(oframe).perform()
ecomm_orderconfirmation = wait.until(EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/p[1]/button[1]/span[1]")))
action.move_to_element(ecomm_orderconfirmation).click().perform()                             
                                    
               
                
                                                              