
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

class TestLogin1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginnoexist(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.driver.find_element(By.NAME, "username").send_keys("sajasaja")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("sajasaja")
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Error!"
 
  @pytest.mark.exist
  def test_loginexist(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    self.driver.set_window_size(1280, 712)
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("narjes")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("narjes")
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").send_keys(Keys.ENTER)
    time.sleep(30)
    assert self.driver.find_element(By.CSS_SELECTOR, ".smallText").text == "Welcome Narjes Abu Rabia"
  
  def test_loginnopass(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(1280, 712)
    self.driver.find_element(By.NAME, "username").send_keys("pass")
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".error").text == "Please enter a username and password."
  
  def test_loginnouser(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(1280, 712)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("pass")
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Error!"
  