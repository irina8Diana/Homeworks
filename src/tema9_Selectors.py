import time
import unittest
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
form_auth = (By.LINK_TEXT, 'Form Authentication')
driver.find_element(*form_auth).click()
time.sleep(3)
actual = driver.current_url
expected = 'https://the-internet.herokuapp.com/login'
# Verifică dacă noul url e corect
assert actual == expected, f'Invalid URL {expected} but found {actual}'
print('Test passed')

# Verifică textul de pe elementul xpath=//h2 e corect
elH2 = driver.find_element(By.XPATH, '//*[@id="content"]/div/h2')
assert elH2.text == "Login Page"

# Verifică dacă butonul de login este displayed
login_button = driver.find_element(By.CSS_SELECTOR, '#login > button > i')
login_button.is_displayed()

# Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
elemental_link = driver.find_element(By.LINK_TEXT, 'Elemental Selenium')
attrib = elemental_link.get_attribute("href")
assert attrib == "http://elementalselenium.com/"

#  Lasă goale user și pass; Click login ; Apasă x la eroare ; Verifică dacă eroarea a dispărut
login_button.click()
close_error = driver.find_element(By.CLASS_NAME, 'close')
close_error.click()
time.sleep(2)
error_msg = driver.find_element(By.ID, 'flash-messages')
if error_msg:
    print("Message was close")
else:
    print("Close the message")

# 7  Completează cu user și pass invalide; Click login ;Verifică dacă mesajul de pe eroare e corect
# Este și un x pus acolo extra așa că vom folosi soluția de mai jos
username = driver.find_element(By.ID, 'username')
username.send_keys('tomsmithh')
passw = driver.find_element(By.ID, 'password')
passw.send_keys('ceva')
login_button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
text = driver.find_element(By.ID, 'flash').text
expected = 'Your username is invalid'
if expected in text:
    print('Message is correct')
else:
    print('Message is not correct')

#def test(self):
 #   self.assertTrue(expected in text, 'Error message text is incorrect')


# 9. Ia ca o listă toate //label Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
# Aici e ok să avem 2 asserturi
label_list = []
label_list = driver.find_elements(By.XPATH, '//*[@id="login"]')
for elem in label_list:
    print(elem.text)
# assert elem.text == "Username"

# Completează cu user și pass valide; Click login ; Verifică ca noul url CONTINE /secure
# Folosește un explicit wait pentru elementul cu clasa ’flash succes’; Verifică dacă elementul cu clasa=’flash succes’ este displayed
# Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

user = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
user.send_keys('tomsmith')
password.send_keys('SuperSecretPassword!')
lg_button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
lg_button.click()
new_url = driver.current_url
if "secure" in new_url:
    print('Url contains secure text')
else:
    print('Url doesn\'t contain secure text')
# flash = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'flash success')))
flash = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'flash')))
if flash.is_displayed():
    print("Is displayed")
else:
    print('Is not displayed')
text = flash.text
if "secure area" in text:
    print('Message contains text')
else:
    print('Text is not in the message')

# Completează cu user și pass valide. Click login. Click logout
# Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
logout = driver.find_element(By.XPATH, '//*[@id="content"]/div/a')
logout.click()
new_page = driver.current_url
assert (new_page == 'https://the-internet.herokuapp.com/login')


