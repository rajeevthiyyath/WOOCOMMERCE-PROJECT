from selenium.webdriver.common.by import By

class OrdersPage:
    MY_ORDERS_LINK = (By.LINK_TEXT, "Orders")
    VIEW_ORDER = (By.CSS_SELECTOR, "a.view")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://woocommerce-850415-2933260.cloudwaysapps.com/my-account/orders")

    #def view_order(self):
        #self.driver.find_element(*self.VIEW_ORDER).click()