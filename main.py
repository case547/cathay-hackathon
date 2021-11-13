from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

CHROMEDRIVER_LOC = '/Users/Justin/Downloads/chromedriver_win32/chromedriver'
driver = Chrome(CHROMEDRIVER_LOC)
driver.get('https://hdf.chp.gov.hk/dhehd/hdf-hkia.jsp?lang=en-us')

passenger_data = [{ "surname_0":"Doe", "givenname_0": "Johnathan",
                    "nationality_0": "Hong Kong", "hkid_0": "Y123456", "hkidcd_0": "7",
                    "flightno_0": "CX 250", "seatno_0": "49K",
                    "telephone_0": "98765432", "flat_0": "A", "floor_0": "69",
                    "address_0": "420 Cool Road", "qaddress_0": "Empire Hotel Hong Kong"
                  },
                  {}
                ]

NEXT_BUTTON = '//*[@id="btnNext"]'

# INPUT_SELECTOR = ".ui-input-text input"
# RADIO_SELECTOR = ".ui-radio input"
# DROPDOWN_SELECTOR = ".ui-select select"
# CHECKBOX_SELECTOR = ".ui-checkbox input"

DECLARATION_CHECK = '//*[@id="declareTC"]'
COMPLETE_BUTTON = '//*[@id="goToFinal_0"]'

driver.find_element_by_xpath(NEXT_BUTTON).click()

def answer_text(driver):
    """Answer all text-input questions"""
    for key, datum in passenger_data[0].items():
        question = driver.find_element(By.ID, key)
        question.send_keys(datum)

    return driver

# def answer_radio(driver, ele):
#     """Answer all radio button questions"""
#     radio_qs = 
#     for datum, question in zip(passenger_data[0], radio_qs):
#         question.send_keys(datum)