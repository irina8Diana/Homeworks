#Completează user tomsmith ; Găsește elementul //h4; Ia textul de pe el și fă split după spațiu. Consideră fiecare
# cuvânt ca o potențială parolă. Folosește o structură iterativă prin care să introduci rând pe rând parolele și să apeși pe login.
#La final testul trebuie să îmi printeze fie ‘Nu am reușit să găsesc parola’ ; ‘Parola secretă este [parola]’
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
username = driver.find_element(By.ID,'username')
username.send_keys('tomsmith')
passw = driver.find_element(By.ID,'password')
login_button = driver.find_element(By.XPATH,'//*[@id="login"]/button/i')
element= driver.find_element(By.XPATH,"//h4")
msg_error = driver.find_element(By.ID, 'flash-messages')
list=[]
list = element.text.split()
print (list)
pass_value = 'tomsmith'
found = False

for psw in list:
    login_button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
    passw = driver.find_element(By.ID, 'password')
    print("parola este: ", psw)
    passw.send_keys(psw)
    login_button.click()
    if elementverde == True:
        found = True
if found ==True :
    print(parola buna)
else:










