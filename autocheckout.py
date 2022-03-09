from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\WebDriver\\chromedriver.exe")
driver.get("https://www.nike.com/checkout")

first_name = "Rogelio"
last_name = "Rodriguez"
address = "Place Holder"
email = "Place Holder"
phone_number = "Place Holder"

#finds name textboxes by ID
first_name_textbox = driver.find_element(By.ID, "firstName")
first_name_textbox = driver.send_keys(first_name)

last_name_textbox = driver.find_element(By.ID, "lastName")
last_name_textbox = driver.send_keys(last_name)

#finds address text box and sends information to it
address_textbox = driver.find_element(By.ID, "search-address-input")
address_textbox = driver.send_keys(address)

email_textbox = driver.find_element(By.ID, "email")
email_textbox = driver.send_keys(email)

phone_textbox = driver.find_element(By.ID, "phoneNumber")
phone_textbox = driver.send_keys(phone_number)

#looks for button by class and presses
cont_btn = driver.find_element(By.Class, "css-1q9tr6m ex41m6f0 btn-primary-dark  btn-responsive")
cont_btn.submit()

