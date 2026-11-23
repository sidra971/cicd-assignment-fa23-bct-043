
import os
import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestWebApplication(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if os.path.exists("/usr/bin/chromium"):
            options.binary_location = "/usr/bin/chromium"

        self.driver = webdriver.Chrome(options=options)

        self.driver.get(
            Path(__file__).resolve().parent.joinpath("index.html").as_uri()
        )

    def test_button_click(self):
        self.driver.find_element(By.ID, "clickBtn").click()

        message = self.driver.find_element(
            By.ID, "clickMessage"
        ).text

        self.assertEqual(
            message, "Button clicked successfully!"
        )

        print("Button Click Test: PASSED")

    def test_text_input(self):
        input_box = self.driver.find_element(
            By.ID, "userInput"
        )

        input_box.send_keys("Selenium Testing")

        self.driver.find_element(
            By.ID, "submitBtn"
        ).click()

        output = self.driver.find_element(
            By.ID, "outputText"
        ).text

        self.assertEqual(output, "Selenium Testing")

        print("Text Input Test: PASSED")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
