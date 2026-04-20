from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

try:
    # --- Тест 1: Авторизация ---
    driver.get("http://users.bugred.ru/user/login/index.html")
    
    driver.find_element(By.NAME, "login").send_keys("manager@mail.ru")
    driver.find_element(By.NAME, "password").send_keys("1")
    
    driver.find_element(By.XPATH, "//input[@value='Авторизоваться']").click()
    
    assert "Пользователи" in driver.page_source
    print("Тест №1 (Авторизация): Успешно")

    # --- Тест 2: Поиск ---
    search_input = driver.find_element(By.NAME, "q")
    search_input.clear()
    search_input.send_keys("manager@mail.ru")
    
    search_input.send_keys(Keys.RETURN)
    
    time.sleep(3)
    
    results = driver.find_elements(By.XPATH, "//td[contains(text(), 'manager@mail.ru')]")
    
    assert len(results) > 0, "Email не найден в результатах поиска!"
    print("Тест №2 (Поиск): Успешно")

finally:
    driver.quit()
