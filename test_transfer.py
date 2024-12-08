
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTransfer():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_transfer0(self):
    self.driver.get("https://parabank.parasoft.com/parabank/transfer.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "amount").click()
    self.driver.find_element(By.ID, "amount").send_keys("0")
    self.driver.find_element(By.ID, "fromAccountId").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#showResult > .title").text == "Transfer Complete!"
  
  def test_transfer200(self):
    self.driver.get("https://parabank.parasoft.com/parabank/transfer.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "amount").click()
    self.driver.find_element(By.ID, "amount").send_keys("-200")
    self.driver.find_element(By.ID, "fromAccountId").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#showResult > .title").text == "Transfer Complete!"
  
  def test_transfer1000(self):
    self.driver.get("https://parabank.parasoft.com/parabank/transfer.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "amount").click()
    self.driver.find_element(By.ID, "amount").send_keys("1000")
    self.driver.find_element(By.ID, "fromAccountId").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#showResult > .title").text == "Transfer Complete!"
  
  def test_transfer515(self):
    self.driver.get("https://parabank.parasoft.com/parabank/transfer.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "amount").click()
    self.driver.find_element(By.ID, "amount").send_keys("515")
    self.driver.find_element(By.ID, "fromAccountId").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#showResult > .title").text == "Transfer Complete!"
  
  def test_transfer200(self):
    self.driver.get("https://parabank.parasoft.com/parabank/transfer.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "amount").click()
    self.driver.find_element(By.ID, "amount").send_keys("200")
    self.driver.find_element(By.ID, "fromAccountId").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#showResult > .title").text == "Transfer Complete!"
  
def test_transfer10000000(self):
    self.driver.get("https://parabank.parasoft.com/parabank/transfer.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "amount").click()
    self.driver.find_element(By.ID, "amount").send_keys("10000000")
    self.driver.find_element(By.ID, "fromAccountId").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#showResult > .title").text == "Transfer Complete!"
  
