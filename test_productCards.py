import pytest
from utils import get_driver, scroll_to_bottom, verify_product_cards


@pytest.fixture(scope="session")
# Funcion de configuración
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# Funciones para los test de la carga de las targetas de productos
def test_card_phones(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll/phones/touch")

    # Funcion de scroll hasta el final de la página
    scroll_to_bottom(driver)

    # Verificar que cada tarjeta de producto cumpla los requisitos
    verify_product_cards(driver)


def test_card_tablets(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets")
    scroll_to_bottom(driver)

    verify_product_cards(driver)


def test_card_laptops(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops")
    scroll_to_bottom(driver)

    verify_product_cards(driver)