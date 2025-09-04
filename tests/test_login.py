import pytest,time
import BaseClass
from selenium import webdriver

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login import FigurePage, LoginPage, MenuPage

#test data
username = 'Text0012'
password = 'Text@001'
totalbalance ='$350'
creditamount = '$17,800'
duetoday = '$180'

@pytest.mark.usefixtures('browser_setup')  #browser invocation fixture is called
class TestLogin:

    def test_login(self):
        self.driver.get(self.urls["login"])  
        loginpage = LoginPage(self.driver) 
        time.sleep(3)
        loginpage.getUserName(username)
        loginpage.getPassword(password)
        loginpage.doSignIn()
        time.sleep(3)

    def test_creditcards(self):
        menupage = MenuPage(self.driver)
        menupage.clickCreditCards()
        time.sleep(5)
        menupage.scroll()
        menupage.save_screenshot(r"D:/shreya vethekar/Practice Automation/banking-website/creditcards.png")


    def test_debitcards(self):
        menupage = MenuPage(self.driver)
        menupage.clickDebitCards()
        time.sleep(5)
        menupage.scroll()
        menupage.save_screenshot(r"D:/shreya vethekar/Practice Automation/banking-website/debitcards.png")

    def test_loan(self):
        menupage = MenuPage(self.driver)
        menupage.clickLoans()
        time.sleep(5)
        menupage.scroll()
        menupage.save_screenshot(r"D:/shreya vethekar/Practice Automation/banking-website/loans.png")

    def test_mortgages(self):
        menupage = MenuPage(self.driver)
        menupage.clickMortgages()
        time.sleep(5)
        menupage.scroll()
        menupage.save_screenshot(r"D:/shreya vethekar/Practice Automation/banking-website/mortgages.png")

  
    def test_totalbalance(self):
        figurepage = FigurePage(self.driver)
        actual = figurepage.getTotalBalance(totalbalance)
        assert actual == totalbalance

    def test_creditamount(self):
        figurepage = FigurePage(self.driver)
        actual = figurepage.getCreditAmount(creditamount)
        assert actual == creditamount


    def test_duetoday(self):
        figurepage = FigurePage(self.driver)
        actual = figurepage.getDueToday(duetoday)
        assert actual == duetoday
