# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Ex1Baidu1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ex1_baidu1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        now_handle = driver.current_window_handle #获取当前窗口句柄
        print now_handle   #输出当前获取的窗口句柄
        
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"李小龙")
        driver.find_element_by_id("su").click()
        driver.find_element_by_link_text(u"李小龙_百度百科").click()
        
        time.sleep(2)
        all_handles = driver.window_handles #获取所有窗口句柄


        for handle in all_handles:

            if handle != now_handle:
                print handle    #输出待选择的窗口句柄
                driver.switch_to_window(handle)
                
                driver.find_element_by_link_text(u"龙争虎斗").click()
                time.sleep(5)
                driver.close() #关闭当前窗口
        time.sleep(3)
        print now_handle   #输出主窗口句柄
        
        # driver.find_element_by_link_text(u"剧情简介").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
