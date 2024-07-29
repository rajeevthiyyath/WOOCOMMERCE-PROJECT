from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://woocommerce-850415-2933260.cloudwaysapps.com/shop"

    def load(self):
        self.driver.get(self.url)

    def click_quick_view(self, product_name):
        quick_view_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#content > article > ul > li.entry.has-media.has-product-nav.col.span_1_of_3.owp-content-center.owp-thumbs-layout-horizontal.owp-btn-normal.owp-tabs-layout-horizontal.has-no-thumbnails.product.type-product.post-145.status-publish.last.instock.product_cat-uncategorized.has-post-thumbnail.shipping-taxable.purchasable.product-type-variable > div > ul > li.btn-wrap.clr > a"))
        )
        quick_view_button.click()