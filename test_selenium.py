import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time

URL = "C:\\Users\\Aluno\\Downloads\\ExerciciosSelenium-master\\index.html"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()

def test_login_valido(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("1234")
    time.sleep(1)
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    message = driver.find_element(By.ID, "message").text
    assert message == "Login bem-sucedido!" 

def test_checkboxes(driver):
    cb1 = driver.find_element(By.ID, "cb1")
    cb2 = driver.find_element(By.ID, "cb2")
    cb3 = driver.find_element(By.ID, "cb3")

    cb1.click()
    time.sleep(1)
    cb2.click()
    time.sleep(1)
    cb3.click()
    time.sleep(1)

    assert cb1.is_selected()
    assert cb2.is_selected()
    assert cb3.is_selected()

    cb2.click()
    time.sleep(1)
    assert not cb2.is_selected()

def test_dropdown(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)

    select = Select(driver.find_element(By.ID, "country"))
    time.sleep(2)
    select.select_by_visible_text("Brasil")
    time.sleep(1)
    assert select.first_selected_option.text == "Brasil"

    select.select_by_visible_text("Canadá")
    time.sleep(1)
    assert select.first_selected_option.text == "Canadá"