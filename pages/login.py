from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils import BaseClass

class BaseClass:
    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self,by_locator,text):
            WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).text

    def save_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0, 500);")   # scroll down 500px


class LoginPage(BaseClass):

    userName = (By.ID, 'username')
    password = (By.ID, 'password')
    signIn = (By.ID,'log-in')


    def __init__(self, driver):
            self.driver = driver

    def getUserName(self,userName):
        userName = self.do_send_keys(self.userName,userName)
        return userName
    
    def getPassword(self,password):
        password = self.do_send_keys(self.password,password)
        return password
    
    def doSignIn(self):
        self.do_click(self.signIn)


class MenuPage(BaseClass):

    creditCards =(By.XPATH,"//span[text()='Credit cards']")
    debitCards = (By.XPATH,"//span[text()='Debit cards']")
    loans = (By.XPATH,"//span[text()='Loans']")
    mortgages = (By.XPATH,"//span[text()='Mortgages']")

    def __init__(self, driver):
        self.driver = driver

    def clickCreditCards(self):
        self.do_click(self.creditCards)

    def clickDebitCards(self):
        self.do_click(self.debitCards)

    def clickLoans(self):
        self.do_click(self.loans)

    def clickMortgages(self):
        self.do_click(self.mortgages)



class FigurePage(BaseClass):

    totalBalance = "//span[text()='{}']"
    creditAmount = "//div[contains(text(),'{}')]"
    dueToday = "//div[contains(text(),'{}')]"

    def __init__(self, driver):
        self.driver = driver

    def getTotalBalance(self, expected_value):
        locator = (By.XPATH, self.totalBalance.format(expected_value))
        return self.get_element_text(locator)

    def getCreditAmount(self, expected_value):
        locator = (By.XPATH, self.creditAmount.format(expected_value))
        return self.get_element_text(locator)

    def getDueToday(self, expected_value):
        locator = (By.XPATH, self.dueToday.format(expected_value))
        return self.get_element_text(locator)







    

