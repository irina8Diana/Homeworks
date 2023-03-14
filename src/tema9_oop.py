import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class login(unittest.TestCase):
    username = (By.ID, 'username')
    passw = (By.ID, 'password')
    login_button = (By.XPATH, '//*[@id="login"]/button/i')
    form_auth = (By.LINK_TEXT, 'Form Authentication')
    page_title = (By.XPATH, '//*[@id="content"]/div/h2')
    text_elh2 = (By.XPATH, '//*[@id="content"]/div/h2')
    login_button = (By.CSS_SELECTOR, '#login > button > i')
    href_selenium = (By.LINK_TEXT, 'Elemental Selenium')
    close_error = (By.CLASS_NAME, 'close')
    error_msg = (By.ID, 'flash-messages')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.driver.maximize_window()

    def test1(self):
        self.driver.find_element(*self.form_auth).click()
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # Verifică dacă noul url e corect
        self.assertEqual(actual == expected, f'Invalid URL {expected} but found {actual}')
        print('Test passed')

    def test2(self):
        self.assertEqual(self.driver.find_element(*self.page_title), 'Login Page')

    def test3(self):
        self.assertEqual(self.driver.find_element(*self.text_elh2).text, 'Login Page')

    def test4(self):
        self.driver.find_element(*self.login_button).is_displayed()

    def test5(self):
        self.assertEqual(self.driver.find_element(*self.href_selenium).get_attribute('href'),
                         'http://elementalselenium.com/')

    def test6(self):
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.error_msg).is_displayed()

    def test7(self):
        self.driver.find_element(*self.username).send_keys('tomsmithh')
        self.driver.find_element(*self.passw).send_keys('ceva')
        self.driver.find_element(*self.login_button).click()
        expected = 'Your username is invalid!'
        self.assertTrue(expected in self.driver.find_element(*self.error_msg).text)

    def test8(self):
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.close_error).click()
        if self.driver.find_element(*self.error_msg).is_displayed():
            print('Message is still displayed')
        else:
            print('Message is not displayed')

    def tearDown(self) -> None:
        self.driver.quit()
