#Добавление комментария
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
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element_by_css_selector('.post-160')
selenium_ruby.click()
reviews = driver.find_element_by_css_selector('.reviews_tab a')
reviews.click()
driver.execute_script("window.scrollBy(0, 600);")
star_5 =  driver.find_element_by_css_selector('.star-5')
star_5.click()
review = driver.find_element_by_id('comment')
review.send_keys('Nice book!')
name = driver.find_element_by_id('author')
name.send_keys('Jhon')
email = driver.find_element_by_id('email')
email.send_keys('email@mail.com')
submit = driver.find_element_by_id('submit')
submit.click()
driver.quit()