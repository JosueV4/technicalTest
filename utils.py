import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Funcion de configuración
def get_driver():
    path = r"C:\Users\ingyo\PycharmProjects\technicalTest\chromedriver"
    service = Service(executable_path=path)
    # headless-mode
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# Funcion de scroll hasta el final de la página
def scroll_to_bottom(driver):
    while True:
        scroll_height_before = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        scroll_height_after = driver.execute_script("return document.body.scrollHeight")
        if scroll_height_before == scroll_height_after:
            break


# Funcion para verificar que cada tarjeta de producto exista y contenga la información correspondiente
def verify_product_cards(driver):
    # Verificación de que se muestren las tarjetas de los productos
    product_cards = driver.find_elements(by="xpath", value='//div[@class="thumbnail"]')
    assert len(product_cards) > 0, "No se encontraron tarjetas de productos"

    # Verificación de imagen, enlace, nombre y precio de cada tarjeta
    for card in product_cards:
        image = card.find_element(by="xpath", value="//img")
        assert image.is_displayed(), "La imagen del producto no se muestra"

        link = card.find_element(by="xpath", value="//a")
        assert link.is_displayed(), "El enlace del producto no se muestra"

        name = card.find_element(by="xpath", value="//a[@class='title']").text
        assert len(name) > 0, "El nombre del producto no se muestra"

        price = card.find_element(by="xpath", value='//h4[@class="pull-right price"]').text
        assert len(price) > 0, "El precio del producto no se muestra"


def verify_products_details(driver):
    details_products = driver.find_elements(by="xpath", value='//div[@class="thumbnail"]//a[@class="title"]')
    assert len(details_products) > 0, "No se encontrarón detalles de la vista del producto"

    # Verificar vista de detalles de cada producto
    for details in details_products:
        try:
            details.click()

            # Verificar que la imagen del producto se muestre
            image = driver.find_element(by="xpath", value='//div[@class="thumbnail"]//img')
            assert image.is_displayed(), "La imagen del producto no se muestra"

            # Verificar que el nombre del producto se muestre
            name = driver.find_element(by="xpath", value='//div[@class="thumbnail"]//h4[2]')
            assert len(name.text) > 0, "El nombre del producto no se muestra"

            # Verificar que la descripción del producto se muestre
            description = driver.find_element(by="xpath", value='//div[@class="thumbnail"]//p[@class="description"]')
            assert len(description.text) > 0, "La descripción del producto no se muestra"

            # Verificar que el precio del producto se muestre
            price = driver.find_element(by="xpath", value='//div[@class="thumbnail"]//h4[@class="pull-right price"]')
            assert len(price.text) > 0, "El precio del producto no se muestra"

            rating = driver.find_element(by="xpath", value='//div[@class="ratings"]//p')
            assert len(rating.text) > 0, "Las reviews del producto no se muestran"

            # Volver a la página anterior
            driver.back()

        except:
            time.sleep(1)
            # Hacer scroll hacia abajo para evitar que el elemento anterior intercepte el clic
            driver.execute_script("window.scrollTo(0, window.scrollY + 100)")
            # Continuar con el siguiente elemento si no se puede hacer clic en el actual
            continue
