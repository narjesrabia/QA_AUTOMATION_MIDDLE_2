
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

class TestLanguagetest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_englishtest(self):
    self.driver.get("https://parabank.parasoft.com/parabank/about.htm")
    self.driver.set_window_size(634, 712)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".visit a").click()
    self.vars["win3547"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win3547"])
    self.driver.find_element(By.CSS_SELECTOR, ".gt_selector").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".b-frame:nth-child(2) > .content span").text == "When Software Is Critical"
  
  def test_deutschtest(self):
    self.driver.get("https://parabank.parasoft.com/parabank/about.htm")
    self.driver.set_window_size(634, 712)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["root"])
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".visit a").click()
    self.vars["win1204"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win1204"])
    self.driver.find_element(By.CSS_SELECTOR, ".gt_selector").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".gt_selector")
    dropdown.find_element(By.XPATH, "//option[. = 'Deutsch']").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".b-frame:nth-child(2) > .content span").text == "Wenn Software kritisch ist"
  
  def test_espanoltest(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "www.parasoft.com").click()
    self.vars["win5798"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win5798"])
    self.driver.find_element(By.CSS_SELECTOR, ".gt_selector").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".gt_selector")
    dropdown.find_element(By.XPATH, "//option[. = 'Español']").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".b-frame:nth-child(2) > .content span").text == "Cuando el software es crítico"
  
  def test_frenchtest(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "www.parasoft.com").click()
    self.vars["win3962"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win3962"])
    self.driver.find_element(By.CSS_SELECTOR, ".gt_selector").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".gt_selector")
    dropdown.find_element(By.XPATH, "//option[. = 'Français']").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".b-frame:nth-child(2) > .content span").text == "Quand le logiciel est critique"
  
  def test_selectlangtest2(self):
    self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
    self.driver.set_window_size(634, 712)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "www.parasoft.com").click()
    self.vars["win9267"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win9267"])
    self.driver.find_element(By.CSS_SELECTOR, ".gt_selector").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".gt_selector")
    dropdown.find_element(By.XPATH, "//option[. = 'Select Language']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".b-frame:nth-child(2) > .content span").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".b-frame:nth-child(2) > .content span").text == "When Software Is Critical"
  
