import pytest
from utils import get_driver, scroll_to_bottom, verify_products_details


@pytest.fixture(scope="session")
# Funcion de configuración
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_product_details_phones(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll/phones/touch")
    scroll_to_bottom(driver)
    verify_products_details(driver)


def test_product_details_tablets(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets")
    scroll_to_bottom(driver)
    verify_products_details(driver)


def test_product_details_laptops(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops")
    scroll_to_bottom(driver)
    verify_products_details(driver)




