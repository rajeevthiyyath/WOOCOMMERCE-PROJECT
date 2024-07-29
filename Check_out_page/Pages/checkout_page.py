import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class CheckoutPage:
    FIRST_NAME = (By.ID, "billing_first_name")
    LAST_NAME = (By.ID, "billing_last_name")
    COUNTRY = (By.ID, "select2-billing_country-container")
    COUNTRY_SEARCH = (By.CLASS_NAME, "select2-search__field")
    COUNTRY_OPTIONS = (By.XPATH, "//ul[@class='select2-results__options']/li")
    ADDRESS = (By.ID, "billing_address_1")
    CITY = (By.ID, "billing_city")
    STATE = (By.ID, "select2-billing_state-container")
    STATE_SEARCH = (By.CLASS_NAME, "select2-search__field")
    POSTCODE = (By.ID, "billing_postcode")
    PHONE_NUMBER = (By.ID, "billing_phone")
    EMAIL = (By.ID, "billing_email")
    DELIVERY_YES = (By.CSS_SELECTOR, "#product_delivery_no")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount")
    DELIVERY_DATE = (By.CSS_SELECTOR, "#date_delivery")
    DELIVERY_TIME = (By.ID, "time_delivery")
    PACKING = (By.ID, "packing")
    WOODEN_BOX = (By.ID, "packaging_wooden")
    PAYMENT_METHOD = (By.XPATH, '//*[@id="payment"]/ul/li[3]/label')
    PLACE_ORDER = (By.ID, "place_order")

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open(self):
        self.driver.get("https://woocommerce-850415-2933260.cloudwaysapps.com/checkout")

    def fill_form(self, first_name, last_name, country, address, city, state, postcode, phonenumber, email, delivery_date):
        # Fill in the form fields
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

        # Select country from dropdown
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COUNTRY)
        ).click()
        country_search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.COUNTRY_SEARCH)
        )
        country_search_box.send_keys(country)
        second_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.COUNTRY_OPTIONS)
        )[1]
        second_option.click()

        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.CITY).send_keys(city)

        # Select state from dropdown
        self.driver.find_element(*self.STATE).click()
        state_search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.STATE_SEARCH)
        )
        state_search_box.send_keys(state)
        state_search_box.send_keys(Keys.RETURN)

        self.driver.find_element(*self.POSTCODE).send_keys(postcode)
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phonenumber)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.DELIVERY_YES).click()


        date_picker_id = "date_delivery"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, date_picker_id))
        ).click()

        date_xpath = '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[3]/a'
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, date_xpath))
            ).click()
        except Exception as e:
            print(f"An error occurred while selecting the date: {e}")



    def select_second_delivery_time_option(self):
                time_input_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.DELIVERY_TIME)
                )
                time_input_element.click()
                time_input_element.send_keys(Keys.ARROW_DOWN)  # Navigate to the second option
                time_input_element.send_keys(Keys.RETURN)
                self.driver.find_element(*self.WOODEN_BOX).click()
                self.driver.find_element(*self.PAYMENT_METHOD).click()

    def order_details_page(self):
     order = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'class="woocommerce-notice woocommerce-notice--success woocommerce-thankyou-order-received'), "Thank you. Your order has been received.")
        )

