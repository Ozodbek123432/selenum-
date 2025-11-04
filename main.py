# auto_login_phone.py
import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

load_dotenv()
LOGIN_URL = os.getenv("LOGIN_URL")
PHONE = os.getenv("LOGIN_PHONE")
PASSWORD = os.getenv("LOGIN_PASSWORD")
if not (LOGIN_URL and PHONE):
    raise SystemExit("LOGIN_URL va LOGIN_PHONE .env ga qo'shing")
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 15)
try:
    driver.get(LOGIN_URL)
    phone_locator = (By.ID,  'phone')
    password_locator = (By.ID, "password")
    submit_locator = (By.CSS_SELECTOR, "button[type='submit']")
    phone_el = wait.until(EC.presence_of_element_located(phone_locator))
    phone_el.clear()
    phone_el.send_keys(PHONE)
    if os.getenv("LOGIN_PASSWORD"):
        pwd_el = wait.until(EC.presence_of_element_located(password_locator))
        pwd_el.clear()
        pwd_el.send_keys(os.getenv("LOGIN_PASSWORD"))
    submit_el = wait.until(EC.element_to_be_clickable(submit_locator))
    submit_el.click()
    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    button.click()
    sleep(1000)
finally:
    driver.quit()