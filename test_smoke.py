import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


USER = {
    'login': 'yana.yanchevska@wesoftyou.com',
    'password': 'energy12ENERGY12=-=',
    'invalid_password': 'energy12ENERGY11=-----'
}


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def login_as_registered_user(driver, USER):

    driver.get("https://ca.wsu.retinatest.net/retailers/154035")
    time.sleep(2)
    accept_button = driver.find_element_by_css_selector(".sc-fznJRM.iPmIHw").click()
    time.sleep(1)

    username_field = driver.find_element_by_css_selector("#emailInput").send_keys(USER['login'])
    password_field = driver.find_element_by_css_selector("#password").send_keys(USER['password'])
    login_button = driver.find_element_by_css_selector(".sc-fznJRM.jZXONG").click()
    time.sleep(1)

    # def test_login_with_empty_fieds_flow(driver):
    # driver.get("https://ca.wsu.retinatest.net/#/login")

    # Click on [Accept] button in PII module
    # accept_button =  driver.find_element_by_css_selector(".sc-fznJRM.iPmIHw").click()
    # accept_button.click()
    # time.sleep(1)

    # # Log in with empty fields
    # login_button =  driver.find_element_by_css_selector(".sc-fzoYHE.jmSFbi").click()
    # time.sleep(5)
    # validation_message = driver.find_element_by_css_selector("[class='sc-fzowVh epfSKh']:nth-child(1) span")
    # assert element.text == u'A valid user ID is required'
    # time.sleep(2)
    # validation_message = driver.find_element_by_css_selector("[class='sc-fzowVh epfSKh']:nth-child(2) span")
    # assert element.text == u'A valid password is required'
    # time.sleep(2)

    # # Log in by invalid email and password
    # username_field =  driver.find_element_by_css_selector("#emailInput").send_keys(Test_data['login'])
    # time.sleep(2)
    # password_field =  driver.find_element_by_css_selector("#password").send_keys(USER['invalid_password'])
    # time.sleep(2)
    # login_button =  driver.find_element_by_css_selector(".sc-fzoYHE.jmSFbi").click()
    # time.sleep(2)
    # validation_message = driver.find_element_by_css_selector("[class='sc-fzowVh epfSKh']:nth-child(1) span")
    # assert element.text == "Invalid User ID or Password. You have 5 remaining attempts before your account is locked for 24 hours."
    # time.sleep(2)
    # validation_message = driver.find_element_by_css_selector("[class='sc-fzowVh epfSKh']:nth-child(2) span")
    # assert element.text == "Invalid User ID or Password. You have 5 remaining attempts before your account is locked for 24 hours."
    # time.sleep(2)


def test_add_suspension_flow(driver):

    login_as_registered_user(driver, USER)
    driver.get("https://ca.wsu.retinatest.net/retailers/154035")
    time.sleep(2)

    add_suspension_button =  driver.find_element_by_css_selector('button[name~=Suspension]').click()
    time.sleep(1)
    agency_dropdown = driver.find_element_by_css_selector(".sc-AxheI.dlcpSc").click()
    time.sleep(1)
    select_agency = driver.find_element_by_css_selector('a[name~=CDTFA]').click()
    time.sleep(1)
    start_date = driver.find_element_by_css_selector("#StartDataPicker").send_keys("12/12/2012")
    time.sleep(1)
    end_date = driver.find_element_by_css_selector("#EndDataPicker").send_keys("12/13/2013")
    time.sleep(2)
    add_suspension_button = driver.find_element_by_css_selector(".sc-fznJRM.jYKXqE").click()
    time.sleep(5)


def test_add_license_flow(driver):

    login_as_registered_user(driver, USER)
    driver.get("https://ca.wsu.retinatest.net/retailers/154035")
    time.sleep(2)

    add_license_button = driver.find_element_by_css_selector('button[name~=License]').click()
    license_number_field = driver.find_element_by_css_selector('#licenseId').send_keys("12345678")
    licensing_agency_dropdown = driver.find_element_by_css_selector('#licensingAgency').click()
    licensing_agency_value = driver.find_element_by_css_selector('a[name~="CDTFA"]').click()
    start_date = driver.find_element_by_css_selector("#startLicenseCalendar").send_keys("10/10/2018")
    end_date = driver.find_element_by_css_selector("#endLicenseCalendar").send_keys("10/10/2019")
    time.sleep(2)
    comfirm_button =  driver.find_element_by_css_selector(".sc-fznJRM.jYKXqE").click()
    time.sleep(2)

def test_add_nforcement_flow(driver):

    login_as_registered_user(driver, USER)
    driver.get("https://ca.wsu.retinatest.net/retailers/154035")
    time.sleep(2)
    add_enforcement_button = driver.find_element_by_css_selector('button[name~=Enforcement]').click()
    survey_form_dropdown = driver.find_element_by_css_selector('.sc-AxheI.dlcpSc').click()
    survey_form_value = driver.find_element_by_css_selector('a[name~="Form#1"]').click()
    agency_dropdown = driver.find_element_by_css_selector(".sc-AxheI.dlcpSc").click()
    agency_value = driver.find_element_by_css_selector('a[name~="CDTFA"]').click()
    proceed_button = driver.find_element_by_css_selector(".sc-fznJRM.jYKXqE").click()
    time.sleep(2)

    # Enforcements survey step 1

    inspecion_date = driver.find_element_by_css_selector("#inspectionDate").send_keys("02/18/2020")
    next_button = driver.find_element_by_css_selector(".sc-fznJRM.ckICkf").click()
    time.sleep(1)

    # Enforcements survey step 2

    inspecion_type_dropdown = driver.find_element_by_css_selector(".sc-fzoMdx.uYzkI").click()
    inspecion_type_value = driver.find_element_by_css_selector("#Hookah").click()
    inspecion_type_dropdown = driver.find_element_by_css_selector(".sc-fzoMdx.uYzkI").click()
    time.sleep(2)
    next_button = driver.find_element_by_css_selector(".sc-fznJRM.ckICkf").click()
    time.sleep(1)

    # Enforcements survey step 3

    product_type_dropdown = driver.find_element_by_css_selector(".sc-fzoMdx.uYzkI").click()
    time.sleep(1)
    product_type_value = driver.find_element_by_css_selector('div[name~=Cigars]').click()
    product_type_dropdown = driver.find_element_by_css_selector(".sc-fzoMdx.uYzkI").click()
    next_button = driver.find_element_by_css_selector(".sc-fznJRM.ckICkf").click()

    # Enforcements survey step 4

    disposition_dropdown = driver.find_element_by_css_selector(".sc-AxgMl.dvwmNO").click()
    disposition_value = driver.find_element_by_css_selector('a[name=Pending]').click()
    next_button = driver.find_element_by_css_selector(".sc-fznJRM.ckICkf").click()
    driver.implicitly_wait(10)

    # Enforcements survey step 5

    penalty_dropdown = driver.find_element_by_css_selector('.sc-AxheI.dYwwAz').click()
    driver.implicitly_wait(10)
    # penalty_value = driver.find_element_by_css_selector('a[name~=Fine]').click()
    penalty_value = driver.find_element_by_css_selector('.sc-fzozJi.kcZzZD').click()
    time.sleep(1)
    next_button = driver.find_element_by_css_selector(".sc-fznJRM.ckICkf").click()

    # Enforcements survey step 6

    save_button = driver.find_element_by_css_selector('.sc-fznJRM.dUSeDF').click()