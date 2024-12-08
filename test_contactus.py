
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

class TestContactustest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_correctdeatils(self):
    self.driver.get("https://parabank.parasoft.com/parabank/contact.htm")
    self.driver.maximize_window()
    self.driver.find_element(By.LINK_TEXT, "Contact Us").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("narjes")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("narjes.rabia2@gmail.com")
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("0525267866")
    self.driver.find_element(By.ID, "message").click()
    self.driver.find_element(By.ID, "message").send_keys("i need help")
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#rightPanel > p:nth-child(3)").text == "A Customer Care Representative will be contacting you."
  
  def test_allempty(self):
    self.driver.get("https://parabank.parasoft.com/parabank/contact.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.ID, "name.errors").text == "Name is required."
  
  def test_emptymessage(self):
    self.driver.get("https://parabank.parasoft.com/parabank/contact.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("narjes")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("narjes.rabia2@gmail.com")
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("0525267866")
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.ID, "message.errors").text == "Message is required."
  
  def test_invalidemail(self):
    self.driver.get("https://parabank.parasoft.com/parabank/contact.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("narjes")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("----")
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("0525267866")
    self.driver.find_element(By.ID, "message").click()
    self.driver.find_element(By.ID, "message").send_keys("i need help")
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#rightPanel > p:nth-child(3)").text == "A Customer Care Representative will be contacting you."
  
  def test_invalidphone(self):
    self.driver.get("https://parabank.parasoft.com/parabank/contact.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("narjes")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("narjes.rabia2@gmail.com")
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("nnnnnnnnnn")
    self.driver.find_element(By.ID, "message").click()
    self.driver.find_element(By.ID, "message").send_keys("i need help")
    self.driver.find_element(By.CSS_SELECTOR, "td > .button").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#rightPanel > p:nth-child(3)").text == "A Customer Care Representative will be contacting you."
  