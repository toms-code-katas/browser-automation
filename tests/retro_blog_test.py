# pylint: disable=C0114
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.remote.webelement import WebElement


# pylint: disable=C0115
class TestRetroBlog(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--headless")
        current_path = pathlib.Path(__file__).parent.resolve()
        service = Service(executable_path=f"{current_path}/../bin/chromedriver")
        cls.driver = webdriver.Chrome(options=options, service=service)
        cls.driver.get("https://tom1299.github.io/retro-blog/")

    # pylint: disable=C0116
    @classmethod
    def assert_element(cls, xpath, text):
        elem: WebElement = cls.driver.find_element(by=by.By.XPATH, value=xpath)
        assert text in elem.text

    # pylint: disable=C0116
    def test_heading(self):
        self.__class__.assert_element(
            "//html/body/div[contains(@id,'content')]/div[contains(@class,'row-fluid')]"
            "/div[contains(@class,'page-header')]/h1",
            "TOM'S SOFTWARE ENGINEERING & AGILE BLOG")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
