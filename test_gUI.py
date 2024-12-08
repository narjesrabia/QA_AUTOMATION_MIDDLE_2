
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

class TestGUI():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_customercare(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.LINK_TEXT, "contact").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Customer Care"
  
  def test_homepage1(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.LINK_TEXT, "home").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Customer Login"
  
  def test_logotest(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".caption").text == "Experience the difference"
  
  def test_parademopage11(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.find_element(By.LINK_TEXT, "about").click()
    self.driver.set_window_size(634, 712)
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "ParaSoft Demo Website"
  
  def test_readmore(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.CSS_SELECTOR, ".more:nth-child(4) > a").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".heading:nth-child(4)").text == "Available Bookstore SOAP services:"
  
