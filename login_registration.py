#Регистрация аккаунта
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://practice.automationtesting.in/')
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
email = driver.find_element_by_id('reg_email')
email.send_keys('email@mail.com')
password = driver.find_element_by_id('reg_password')
password.send_keys('password_strong')
register = driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]')
register.click()
driver.quit()

#Логин в систему
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://practice.automationtesting.in/')
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('email@mail.com')
password = driver.find_element_by_id('password')
password.send_keys('password_strong')
login = driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
login.click()
logout = driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a')
logout_text = logout.text
assert logout_text == "Logout"
driver.quit()
