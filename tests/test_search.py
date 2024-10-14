import logging
import os
from time import sleep

import pytest
import allure

from pages.home_page import HomePage
from utils.data_provider import DataProvider
from utils.reporting import Reporting

# Constants
EXCEL = "Iberia_Flight_Data.xlsx"
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excel_path = os.path.join(base_dir, 'data', EXCEL)
test_name = os.path.splitext(os.path.basename(__file__))[0]

# Logging the base directory and Excel path
logging.info(base_dir)
logging.info(excel_path)

@allure.epic("Busqueda de vuelos")
@allure.story("1.- Entrar en Iberia")
def test_enter_mainpage(home_page: HomePage):
    """
    Test to verify that the Iberia homepage can be navigated to and loaded correctly.
    """
    with allure.step("Dado que se navega a la web de Iberia"):
        home_page.navigate_home()

    with allure.step("Se comprueba que se ha abierto la URL correcta"):
        assert home_page.check_active_url()


@allure.epic("Busqueda de vuelos")
@allure.story("2.- Aceptar Cookies")
def test_accept_cookies(home_page: HomePage):
    """
    Test to accept cookies if the accept button is present.
    """
    with allure.step("Dado que existe el botón de aceptar cookies"):
        if home_page.find_object(home_page.COOKIE_BTN):
            with allure.step("Se comprueba que se hace click en el botón de aceptar cookies"):
                assert home_page.click(home_page.COOKIE_BTN)
                home_page.wait_to_darkfilter()


@allure.epic("Busqueda de vuelos")
@allure.story("3.- Introducir datos de vuelo")
def test_enter_fly_data(home_page: HomePage):
    """
    Test to enter flight data collected from an Excel file into the flight search form.
    """
    with allure.step("Dado que se recogen los datos de vuelo desde un Excel"):
        flydata = DataProvider.read_excel_to_dict(excel_path)

        with allure.step("Cuando introduzco esos datos en el formulario de búsqueda de vuelos"):
            for data in flydata:
                # Enter the flight origin
                home_page.enter_origin(data['Origin'])
                assert data['Origin'] == home_page.get_locator_attribute(home_page.ORIGIN_TXTBOX, home_page.ATR_VALUE)

                # Enter the flight destination
                home_page.enter_destiny(data['Destiny'])

                # Enter the start date
                home_page.enter_stardate(data['Start_Date'])

                # Enter the end date
                home_page.enter_enddate(data['End_Date'])

                # Enter the passenger count
                home_page.enter_passengers(data['Adult'], data['Child'], data['Baby'])

                with allure.step("Se comprueba que el número de pasajeros es el esperado y se guarda una captura"):
                    assert data['Adult'] == int(home_page.get_element_text(home_page.ADULT_COUNT))
                    assert data['Child'] == int(home_page.get_element_text(home_page.CHILD_COUNT))
                    assert data['Baby'] == int(home_page.get_element_text(home_page.BABY_COUNT))

                    # Take screenshot for reporting
                    reporting_instance = Reporting(home_page.driver)
                    reporting_instance.take_screenshot(test_name)



