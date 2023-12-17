import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service

# Import your Flask app and database initialization function
from app import app, initialize_testing_database

@pytest.fixture
def driver():
    service = Service(executable_path=r'C:\Users\Hubert\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe')
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Configure the Flask app to use the testing database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_greetings.db'

# Initialize the testing database before running the tests
app.testing = True
app_context = app.app_context()
app_context.push()
initialize_testing_database()

def test_home_page(driver):
    driver.get("http://localhost:5000")
    assert "Welcome" in driver.title

def test_greet_form(driver):
    driver.get("http://localhost:5000")
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'name'))
    )
    name_input.send_keys('Test')
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    assert "Hello, Test!" in driver.page_source

def test_greeting_function(driver):
    driver.get("http://localhost:5000")
    name_input = driver.find_element(By.NAME, 'name')
    name_input.send_keys('Test User')
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Hello, Test User!')]"))
    )
    assert "Hello, Test User!" in driver.page_source

def test_greetings_display(driver):
    driver.get("http://localhost:5000/greetings")
    assert "List of Greetings" in driver.page_source

def test_greeting_invalid_data(driver):
    driver.get("http://localhost:5000")
    name_input = driver.find_element(By.NAME, 'name')
    name_input.send_keys('')
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    assert "Hello, !" in driver.page_source
