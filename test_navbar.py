import pytest
from utils import get_driver
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="session")
# Funcion de configuración
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

# Funciones para los test del menú de navegación
def test_home_link(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll")
    try:
        home_link = driver.find_element(by="xpath", value="//ul[@id='side-menu']//a[@href='/test-sites/e-commerce/scroll']")
    except NoSuchElementException:
        assert False, "No se encontró el elemento 'Home' en el menú de navegación"

    assert home_link.text == 'Home'
    home_link.click()
    assert driver.current_url == 'https://webscraper.io/test-sites/e-commerce/scroll'


def test_phones_link(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll")
    try:
        phones_link = driver.find_element(by="xpath", value="//ul[@id='side-menu']//a[@href='/test-sites/e-commerce/scroll/phones']")
    except NoSuchElementException:
        assert False, "No se encontró el elemento 'Phones' en el menú de navegación"

    assert phones_link.text == 'Phones'
    phones_link.click()
    assert driver.current_url ==  'https://webscraper.io/test-sites/e-commerce/scroll/phones'


def test_phones_touch_link(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll")
    driver.find_element(by="xpath", value="//ul[@id='side-menu']//a[@href='/test-sites/e-commerce/scroll/phones']").click()
    try:
        phones_touch_link = driver.find_element(by="xpath", value="//ul[@id='side-menu']//a[@href='/test-sites/e-commerce/scroll/phones/touch']")
    except NoSuchElementException:
        assert False, "No se encontró el elemento 'Touch' en el menú de navegación"

    assert phones_touch_link.text == 'Touch'
    phones_touch_link.click()
    assert driver.current_url == 'https://webscraper.io/test-sites/e-commerce/scroll/phones/touch'


def test_computers_link(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll")
    try:
        computers_link = driver.find_element(by="xpath", value="//ul[@id='side-menu']//a[@href='/test-sites/e-commerce/scroll/computers']")
    except NoSuchElementException:
        assert False, "No se encontró el elemento 'Computers' en el menú de navegación"

    assert  computers_link.text == 'Computers'
    computers_link.click()
    assert driver.current_url == 'https://webscraper.io/test-sites/e-commerce/scroll/computers'


def test_computers_tablets_link(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll")
    driver.find_element(by="xpath", value="//ul[@id='side-menu']//a[@href='/test-sites/e-commerce/scroll/computers']").click()
    try:
        computers_tablets_link = driver.find_element(by="xpath", value="//ul[@id='side-menu']//a[@href='/test-sites/e-commerce/scroll/computers/tablets']")
    except NoSuchElementException:
        assert False, "No se encontró el elemento 'Tablets' en el menú de navegación"

    assert computers_tablets_link.text == 'Tablets'
    computers_tablets_link.click()
    assert driver.current_url == "https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets"


def test_computers_laptops_link(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll")
    driver.find_element(by="xpath", value="//ul[@id='side-menu']//a[@href='/test-sites/e-commerce/scroll/computers']").click()
    try:
        computers_laptops_link = driver.find_element(by="xpath", value="//ul[@id='side-menu']//a[@href='/test-sites/e-commerce/scroll/computers/laptops']")
    except NoSuchElementException:
        assert False, "No se encontró el elemento 'Laptops' en el menú de navegación"

    assert computers_laptops_link.text == 'Laptops'
    computers_laptops_link.click()
    assert driver.current_url == "https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops"

