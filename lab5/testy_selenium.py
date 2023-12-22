import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def browser():
    service = Service(executable_path=r'C:\Users\Hubert\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe')
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    driver.set_window_size(1280, 720)
    yield driver
    driver.quit()

def test_fill_form(browser):
    browser.get("https://demoqa.com/automation-practice-form")

    browser.find_element(By.ID, "firstName").send_keys("Jan")
    browser.find_element(By.ID, "lastName").send_keys("Kowalski")
    browser.find_element(By.ID, "userEmail").send_keys("jan.kowalski@example.com")

    gender_radio = browser.find_element(By.CSS_SELECTOR, "input[name='gender'][value='Male']")
    ActionChains(browser).move_to_element(gender_radio).click().perform()

    browser.find_element(By.ID, "userNumber").send_keys("1234567890")

    date_of_birth_input = browser.find_element(By.ID, "dateOfBirthInput")
    browser.execute_script("arguments[0].scrollIntoView(true);", date_of_birth_input)
    date_of_birth_input.click()

    month_selector = Select(browser.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    month_selector.select_by_value("3")
    year_selector = Select(browser.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    year_selector.select_by_value("1995")
    browser.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()

    subjects_input = browser.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("Maths")
    subjects_input.send_keys(Keys.RETURN)

    sports_checkbox = browser.find_element(By.CSS_SELECTOR, "input[id='hobbies-checkbox-1']")
    ActionChains(browser).move_to_element(sports_checkbox).click().perform()

    browser.find_element(By.ID, "currentAddress").send_keys("ul. Przykładowa 1, 00-000 Miasto")

    state_input = browser.find_element(By.ID, "react-select-3-input")
    browser.execute_script("arguments[0].scrollIntoView(true);", state_input)
    browser.execute_script("arguments[0].click();", state_input)
    state_input.send_keys("NCR")
    state_input.send_keys(Keys.RETURN)

    city_input = browser.find_element(By.ID, "react-select-4-input")
    browser.execute_script("arguments[0].scrollIntoView(true);", city_input)
    browser.execute_script("arguments[0].click();", city_input)
    city_input.send_keys("Delhi")
    city_input.send_keys(Keys.RETURN)

    submit_button = browser.find_element(By.ID, "submit")
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    browser.execute_script("arguments[0].click();", submit_button)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-body")))
    assert "Thanks for submitting the form" in browser.page_source
