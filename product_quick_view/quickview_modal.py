from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QuickViewModal:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def select_variation_color(self, color):
        color_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-145 > div.summary.entry-summary > form > table > tbody > tr:nth-child(1) > td > div > ul > li.thwvs-wrapper-item-li.thwvs-label-li.thwvs-div.thwvs-checkbox.attribute_color.Red.attr_swatch_design_default > span"))
        )
        color_dropdown.click()

    def select_variation_orientation(self, orientation):
        orientation_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-145 > div.summary.entry-summary > form > table > tbody > tr:nth-child(2) > td > div > ul > li.thwvs-wrapper-item-li.thwvs-label-li.thwvs-div.thwvs-checkbox.attribute_orientation.Landscape.attr_swatch_design_default > span"))
        )
        orientation_dropdown.click()

    def enter_profile_description(self, description):
        profile_description = self.driver.find_element(By.ID, "profile_desc")
        profile_description.send_keys(description)

    def check_add_phone_number(self):
        add_phone_checkbox = self.driver.find_element(By.ID, "phone_number_checkbox")
        if not add_phone_checkbox.is_selected():
            add_phone_checkbox.click()

    def enter_phone_number(self, phone_number):
        phone_number_field = self.driver.find_element(By.ID, "phone_number_field")
        phone_number_field.send_keys(phone_number)



    def upload_logo(self, file_path):
        upload_logo_field = self.driver.find_element(By.ID, "logo")
        upload_logo_field.send_keys(file_path)

    def select_border1(self):
        border_field = self.driver.find_element(By.XPATH,
                                                '//*[@id="product-145"]/div[3]/form/div/div[2]/div[2]/div[3]/div[2]/div[1]/label/div/img')

        border_field.click()

    def select_borders2(self):
        border_field = self.driver.find_element(By.XPATH, '//*[@id="product-145"]/div[3]/form/div/div[2]/div[2]/div[3]/div[2]/div[2]/label/div/img')
        border_field.click()

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.CLASS_NAME, "single_add_to_cart_button")
        add_to_cart_button.click()

    def is_product_added_to_cart(self):
        cart_count = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content > article > div.woocommerce-notices-wrapper > div"), "“RF ID Card” has been added to your cart")
        )
        return cart_count