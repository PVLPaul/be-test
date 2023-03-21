#Отображение страницы товара
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
shop = driver.find_element_by_id('menu-item-40')
shop.click()
html_5 = driver.find_element_by_xpath('//*[@id="content"]/ul/li[3]/a[1]/img')
html_5.click()
html_5_forms = driver.find_element_by_css_selector('.summary.entry-summary h1')
html_5_forms_text = html_5_forms.text
assert html_5_forms_text == 'HTML5 Forms'
driver.quit()

#Количество товаров в категории
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
shop = driver.find_element_by_id('menu-item-40')
shop.click()
html = driver.find_element_by_css_selector('.cat-item.cat-item-19 a')
html.click()
html = driver.find_element_by_css_selector('.cat-item.cat-item-19.current-cat .count')
html_count = html.text
assert html_count == '(3)'
driver.quit()

#Сортировка товаров
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
shop = driver.find_element_by_id('menu-item-40')
shop.click()
default = driver.find_element_by_css_selector('[value = menu_order]')
default_select = default.get_attribute('selected')
print(default_select)
sort = driver.find_element_by_css_selector('.orderby')
select = Select(sort)
select.select_by_index(5)
price = driver.find_element_by_css_selector('[value = price-desc]')
price_select = price.get_attribute('selected')
print(price_select)
driver.quit()

#Отображение, скидка товара
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
shop = driver.find_element_by_id('menu-item-40')
shop.click()
android = driver.find_element_by_xpath('//*[@id="content"]/ul/li[1]/a[1]')
android.click()
book_old_price = driver.find_element_by_css_selector('.price>del>span')
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
book_new_price = driver.find_element_by_css_selector('.price>ins>span')
book_new_price_text = book_new_price.text
assert book_new_price_text == "₹450.00"
picture = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="product-169"]/div[1]/a/img')) )
picture.click()
close = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close')) )
close.click()
driver.quit()

#Проверка цены в корзине
#Все книги были out of stock, кроме Mastering JavaScript, поэтому работал с ней
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
shop = driver.find_element_by_id('menu-item-40')
shop.click()
book = driver.find_element_by_xpath('//*[@id="content"]/ul/li[6]/a[2]')
book.click()
time.sleep(3)
item = driver.find_element_by_css_selector('span.cartcontents')
item_text = item.text
assert item_text == '1 Item'
price = driver.find_element_by_css_selector('a>span.amount')
price_text = price.text
assert price_text == '₹350.00'
cart = driver.find_element_by_css_selector('.wpmenucart-icon-shopping-cart-0')
cart.click()
subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal>td>span"), "350.00"))
total = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td>strong>span"), "357.00"))
driver.quit()

#Работа в корзине
# Задание выполнить не представилось возможным, так как была доступна только 1 книга  - Mastering JavaScript,
# остальные книги были out of stock.

# Покупка товара (из всех книг была доступна только Mastering JavaScript, поэтому работал с ней)
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
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
book = driver.find_element_by_xpath('//*[@id="content"]/ul/li[6]/a[2]')
book.click()
time.sleep(3)
cart = driver.find_element_by_css_selector('.wpmenucart-icon-shopping-cart-0')
cart.click()
proceed = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout a")))
proceed.click()
first_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys('Jhon')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Smith')
email = driver.find_element_by_id('billing_email')
email.send_keys('email@mail.com')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('+1777222334455')
selector = driver.find_element_by_id('s2id_billing_country')
selector.click()
input = driver.find_element_by_id('s2id_autogen1_search')
input.send_keys('Malta')
country = driver.find_element_by_css_selector('.select2-result-label .select2-match')
country.click()
strit = driver.find_element_by_id('billing_address_1')
strit.send_keys('214, Merchant Street')
city = driver.find_element_by_id('billing_city')
city.send_keys('Valletta')
state = driver.find_element_by_id('billing_state')
state.send_keys('VAL')
postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('1170')
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payments = driver.find_element_by_id('payment_method_cheque')
payments.click()
order = driver.find_element_by_id('place_order')
order.click()
thank_you = WebDriverWait(driver, 5).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce>p.woocommerce-thankyou-order-received"),
      "Thank you. Your order has been received."))
method = WebDriverWait(driver, 5).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, "table>tfoot>tr:nth-child(3)>td"), "Check Payments"))
driver.quit()
