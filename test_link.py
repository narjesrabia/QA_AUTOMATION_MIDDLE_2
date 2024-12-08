
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

class TestTestlink():
  def setup_method(self, method):
    #self.driver = webdriver.Firefox()
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_admin(self):
    self.driver.get("https://parabank.parasoft.com/parabank/admin.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.LINK_TEXT, "Admin Page").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Administration"
  
  def test_aboutus(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.LINK_TEXT, "About Us").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "ParaSoft Demo Website"
  
  def test_location(self):
    self.driver.get("https://parabank.parasoft.com/parabank/admin.htm")
    self.driver.find_element(By.LINK_TEXT, "Locations").click()
    self.driver.set_window_size(634, 712)
    assert self.driver.find_element(By.CSS_SELECTOR, ".page-title").text == "SOLUTIONS"
  
  def test_product(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.LINK_TEXT, "Products").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".page-title").text == "PRODUCTS"
  
  def test_services(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.LINK_TEXT, "Services").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".heading:nth-child(4)").text == "Available Bookstore SOAP services:"
  
