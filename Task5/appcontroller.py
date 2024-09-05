import time
from appium import webdriver
from typing import Any,Dict
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions

options = UiAutomator2Options()
options.set_capability('platformName', 'Android')
options.set_capability('platformVersion', '14')
options.set_capability('deviceName', 'Redmi Note 12S')
options.set_capability('appPackage', 'com.openai.chatgpt')
options.set_capability('appActivity', '.MainActivity')
options.set_capability('automationName', 'UiAutomator2')

driver = webdriver.Remote('http://localhost:4723', options=options)

def login(username, password):
    continue_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[1]"))
    )
    continue_button1.click()

    signup_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//s1.e0/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Button[1]"))
    )
    signup_button1.click()

    signup_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//s1.e0/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.widget.Button.Button[1]"))
    )
    signup_button2.click()

    username_field = driver.find_element((AppiumBy.XPATH,"//s1.e0/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.widget.Button[0]"))
    username_field.send_keys(username)

    continue_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[2]"))
    )
    continue_button2.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[1]')))

    password_field = driver.find_element((AppiumBy.XPATH,"//android.widget.EditText[1]"))
    password_field.send_keys(password)

    continue_button3 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[3]"))
    )
    continue_button3.click()

def handle_screen_orientation():
    driver.rotate('LANDSCAPE')
    time.sleep(2)
    
    driver.rotate('PORTRAIT')
    time.sleep(2)
    
def main():
    try:
        login('sithu.ko.ko@outlook.com', 'cw#yb6m2lg52')
        time.sleep(5)
        handle_screen_orientation()
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
