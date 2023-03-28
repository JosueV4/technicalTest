import pytest
from utils import get_driver, scroll_to_bottom


@pytest.fixture(scope="session")
# Funcion de configuración
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# Funciones para los test de precios de los productos
def test_price_phones(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll/phones/touch")

    # Funcion de scroll hasta el final de la página
    scroll_to_bottom(driver)

    # Obtener todos los precios de los phones
    price_phones = driver.find_elements(by="xpath", value="//div[@class='col-sm-4 col-lg-4 col-md-4']//h4[@class='pull-right price']")
    # Verificar que la cantidad de elementos sea mayor que cero
    assert len(price_phones) > 0

    # Verificar que los precios sean valores positivos
    for price_phone in price_phones:
        price_text = price_phone.text.replace("$", "")  # Remover el signo de dólar del precio
        price_float = float(price_text)  # Convertir el precio en un float
        assert price_float > 0, f"El precio {price_float} no es ún número positivo"


def test_price_tablets(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets")
    scroll_to_bottom(driver)

    price_tablets = driver.find_elements(by="xpath", value='//div[@class="col-sm-4 col-lg-4 col-md-4"]//h4[@class="pull-right price"]')
    assert len(price_tablets) > 0

    for price_tablet in price_tablets:
        price_text = price_tablet.text.replace("$", "")
        price_float = float(price_text)
        assert price_float > 0, f"El precio {price_float} no es ún número positivo"


def test_price_laptops(driver):
    driver.get("https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops")
    scroll_to_bottom(driver)

    price_laptops = driver.find_elements(by="xpath", value='//div[@class="col-sm-4 col-lg-4 col-md-4"]//h4[@class="pull-right price"]')
    assert len(price_laptops) > 0

    for price_laptop in price_laptops:
        price_text = price_laptop.text.replace("$", "")
        price_float = float(price_text)
        assert price_float > 0, f"El precio {price_float} no es ún número positivo"