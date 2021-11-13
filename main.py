from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# Setting up the WebDriver for Chrome, and open Health Declaration From website
CHROMEDRIVER_LOC = '/Users/Justin/Downloads/chromedriver_win32/chromedriver'
driver = Chrome(CHROMEDRIVER_LOC)
driver.get('https://hdf.chp.gov.hk/dhehd/hdf-hkia.jsp?lang=en-us')

# Passenger data, which will be retrieved as JSON objects/arrays in the real product
# Currently coded in for sake of functionality demonstration
passenger_data = [
    {
        "surname_0":"Doe", "givenname_0": "Johnathan",
        "birthyear_0": "1970", "birthmonth_0": "1", "birthday_0": "1",
        "nationality_0": "Hong Kong", "hkid_0": "Y123456", "hkidcd_0": "7",
        "flightno_0": "CX 250", "seatno_0": "49K",
        "telephone_0": "98765432", "flat_0": "A", "floor_0": "69",
        "address_0": "420 Cool Road"
    },
    {
        "sex_0": "a", "hkResident_0": "a",
        "aircrew_0": "b", "seacrew_0": "b", "otherExemptedPerson_0": "b",
        "transitPort_0": "b", "isVisitedHighRiskCountry_0": "a",
        "isChina_0": "b", "isForeign_0": "b",
        "isVaccinatedBeforeHK_0": "a", "qAddressType_0": "b"
    },
    [
        ["countryOriginal_0_1-button", "countryOriginal_0_1-menu", "211"],
        ["countryCode_0-button", "countryCode_0-menu", "1"],
        ["qDesignatedHotel_0-button", "qDesignatedHotel_0-menu", "13"]
    ]
]

# XPaths of main navigation buttons in the form
NEXT_BUTTON = '//*[@id="btnNext"]'
DECLARATION_CHECK = '//*[@id="declareTC"]'
COMPLETE_BUTTON = '//*[@id="goToFinal_0"]'

# To move past the Personal Information Collection Statement
driver.find_element(By.XPATH, NEXT_BUTTON).click()

def answer_text(driver):
    """Answer all text-input questions."""
    for key, datum in passenger_data[0].items():
        question = driver.find_element(By.ID, key)
        question.send_keys(datum)

    return driver

def answer_radio(driver):
    """Answer all radio button questions."""
    for key, val in passenger_data[1].items():
        field = driver.find_element(By.ID, key)
        field.find_element(By.CSS_SELECTOR, f"[for={key+val}]").click()

    return driver

# def answer_dropdowns(driver):
#     """Answer the long dropdown questions."""
#     for sublist in passenger_data[2]:
#         driver.find_element(By.ID, sublist[0]).click()
#         select_menu = driver.find_element(By.ID, sublist[1])
#         select_menu.find_element(By.CSS_SELECTOR, f"[dataset.optionIndex={sublist[2]}]").click()

#     return driver

# driver = answer_text(driver)
# driver = answer_radio(driver)
# driver = answer_dropdowns(driver)

# Declare that given information is correct/complete
driver.find_element(By.XPATH, NEXT_BUTTON).click()

# Submit form. Commented out to avoid accidental submission with fake data.
# driver.find_element(By.XPATH, NEXT_BUTTON).click()
