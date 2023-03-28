import pytest
from utils import get_driver
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="session")
# Funcion de configuración
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# Funcion para comprobar la existencia de la barra de búsqueda
def test_search_bar(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll")

    try:
        driver.find_element(by="xpath", value='//input[@type="search"]')
    except NoSuchElementException:
        raise AssertionError("La página no tiene una barra de búsqueda")



