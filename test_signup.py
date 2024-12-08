
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

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testsignupnopassword(self):
    self.driver.get("https://parabank.parasoft.com/parabank/register.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "customer.firstName").click()
    self.driver.find_element(By.ID, "customer.firstName").send_keys("narjes")
    self.driver.find_element(By.ID, "customer.lastName").click()
    self.driver.find_element(By.ID, "customer.lastName").send_keys("abu rabia")
    self.driver.find_element(By.ID, "customer.address.street").click()
    self.driver.find_element(By.ID, "customer.address.street").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.city").click()
    self.driver.find_element(By.ID, "customer.address.city").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.state").click()
    self.driver.find_element(By.ID, "customer.address.state").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.zipCode").click()
    self.driver.find_element(By.ID, "customer.address.zipCode").send_keys("23456")
    self.driver.find_element(By.ID, "customer.phoneNumber").click()
    self.driver.find_element(By.ID, "customer.phoneNumber").send_keys("0525167966")
    self.driver.find_element(By.ID, "customer.ssn").click()
    self.driver.find_element(By.ID, "customer.ssn").send_keys("8765")
    self.driver.find_element(By.ID, "customer.username").click()
    self.driver.find_element(By.ID, "customer.username").send_keys("mariam")
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.ID, "customer.password.errors").text == "Password is required."
  
  def test_testsignupexsistusername(self):
    self.driver.get("https://parabank.parasoft.com/parabank/register.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "customer.firstName").click()
    self.driver.find_element(By.ID, "customer.firstName").send_keys("narjes")
    self.driver.find_element(By.ID, "customer.lastName").click()
    self.driver.find_element(By.ID, "customer.lastName").send_keys("abu rabia")
    self.driver.find_element(By.ID, "customer.address.street").click()
    self.driver.find_element(By.ID, "customer.address.street").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.city").click()
    self.driver.find_element(By.ID, "customer.address.city").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.state").click()
    self.driver.find_element(By.ID, "customer.address.state").send_keys("rahat")
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(2)").click()
    self.driver.find_element(By.ID, "customer.address.zipCode").click()
    self.driver.find_element(By.ID, "customer.address.zipCode").send_keys("23456")
    self.driver.find_element(By.ID, "customer.phoneNumber").click()
    self.driver.find_element(By.ID, "customer.phoneNumber").send_keys("0525167966")
    self.driver.find_element(By.ID, "customer.ssn").click()
    self.driver.find_element(By.ID, "customer.ssn").send_keys("8765")
    self.driver.find_element(By.ID, "customer.username").click()
    self.driver.find_element(By.ID, "customer.username").send_keys("@@@@")
    self.driver.find_element(By.ID, "customer.password").click()
    self.driver.find_element(By.ID, "customer.password").send_keys("333")
    self.driver.find_element(By.ID, "repeatedPassword").click()
    self.driver.find_element(By.ID, "repeatedPassword").send_keys("333")
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.ID, "customer.username.errors").text == "This username already exists."
  
  def test_testsignupnousername1(self):
    self.driver.get("https://parabank.parasoft.com/parabank/register.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "customer.firstName").click()
    self.driver.find_element(By.ID, "customer.firstName").send_keys("narjes")
    self.driver.find_element(By.ID, "customer.lastName").click()
    self.driver.find_element(By.ID, "customer.lastName").send_keys("abu rabia")
    self.driver.find_element(By.ID, "customer.address.street").click()
    self.driver.find_element(By.ID, "customer.address.street").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.city").click()
    self.driver.find_element(By.ID, "customer.address.city").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.state").click()
    self.driver.find_element(By.ID, "customer.address.state").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.zipCode").click()
    self.driver.find_element(By.ID, "customer.address.zipCode").send_keys("23456")
    self.driver.find_element(By.ID, "customer.phoneNumber").click()
    self.driver.find_element(By.ID, "customer.phoneNumber").send_keys("0525167966")
    self.driver.find_element(By.ID, "customer.ssn").click()
    self.driver.find_element(By.ID, "customer.ssn").send_keys("8765")
    self.driver.find_element(By.ID, "customer.password").click()
    self.driver.find_element(By.ID, "customer.password").send_keys("444")
    self.driver.find_element(By.ID, "repeatedPassword").click()
    self.driver.find_element(By.ID, "repeatedPassword").send_keys("444")
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.ID, "customer.username.errors").text == "Username is required."
  
  def test_testsignupnousernamenopassword11(self):
    self.driver.get("https://parabank.parasoft.com/parabank/register.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "customer.firstName").click()
    self.driver.find_element(By.ID, "customer.firstName").send_keys("narjes")
    self.driver.find_element(By.ID, "customer.lastName").click()
    self.driver.find_element(By.ID, "customer.lastName").send_keys("abu rabia")
    self.driver.find_element(By.ID, "customer.address.street").click()
    self.driver.find_element(By.ID, "customer.address.street").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.city").click()
    self.driver.find_element(By.ID, "customer.address.city").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.state").click()
    self.driver.find_element(By.ID, "customer.address.state").send_keys("rahat")
    self.driver.find_element(By.ID, "customer.address.zipCode").click()
    self.driver.find_element(By.ID, "customer.address.zipCode").send_keys("23456")
    self.driver.find_element(By.CSS_SELECTOR, ".form2").click()
    self.driver.find_element(By.ID, "customer.phoneNumber").click()
    self.driver.find_element(By.ID, "customer.phoneNumber").send_keys("0525167966")
    self.driver.find_element(By.ID, "customer.ssn").click()
    self.driver.find_element(By.ID, "customer.ssn").send_keys("8765")
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.ID, "customer.username.errors").text == "Username is required."
    assert self.driver.find_element(By.ID, "customer.password.errors").text == "Password is required."
  
  def test_testsignupnoform(self):
    self.driver.get("https://parabank.parasoft.com/parabank/register.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "customer.username").click()
    self.driver.find_element(By.ID, "customer.username").send_keys("nour")
    self.driver.find_element(By.ID, "customer.password").click()
    self.driver.find_element(By.ID, "customer.password").send_keys("nour")
    self.driver.find_element(By.ID, "repeatedPassword").click()
    self.driver.find_element(By.ID, "repeatedPassword").send_keys("nour")
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.ID, "customer.firstName.errors").text == "First name is required."
  
