from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import env


def find(xpath):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, xpath)))


def findMultiples(xpath):
    return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
        (By.XPATH, xpath)))


def click(xpath):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, xpath))).click()


def login():
    login_button = find(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
    login_button.click()
    username_text_field = find(
        '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username_text_field.send_keys(env.username)
    username_text_field.send_keys(Keys.ENTER)
    password_text_field = find(
        '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_text_field.send_keys(env.password)
    password_text_field.send_keys(Keys.ENTER)


chrome_options = Options()
chrome_options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)
driver.get(f'https://www.twitter.com/')
login()
