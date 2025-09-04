import pytest 


@pytest.mark.usefixtures("browser_setup")
class BaseClass:
    def __init__(self, driver):
            self.driver = driver

    