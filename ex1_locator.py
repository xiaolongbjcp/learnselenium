# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium import selenium
import time
import os
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Firefox()
file_path =  'file:///' + os.path.abspath('test.html')
driver.get(file_path)

username = driver.find_element_by_name('username')
print '\n',"driver.find_element_by_name('username')"
print username, '\n',type(username)


print '\n',"driver.find_element_by_xpath('/html/body/form[1]')"
login_form = driver.find_element_by_xpath("/html/body/form[1]")
print login_form
login_form = driver.find_element_by_xpath("//form[1]")
print login_form
login_form = driver.find_element_by_xpath("//form[@id='loginForm']")
print login_form


continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti')
print '\n',"driver.find_element_by_link_text('Continue')"
print continue_link


heading1 = driver.find_element_by_tag_name('h1')
print '\n',"driver.find_element_by_tag_name('h1')"
print heading1

content = driver.find_element_by_class_name('content')
print '\n',"driver.find_element_by_class_name('content')"
print content

content = driver.find_element_by_css_selector('p.content')
print '\n',"driver.find_element_by_css_selector('p.content')"
print content


element = driver.find_element_by_xpath("//form[@id='loginForm']")
all_options = element.find_elements_by_tag_name("input")
for option in all_options:
	print("Value is: %s" % option.get_attribute("name"))
	# option.send_keys(option.get_attribute("name"))
	t = option.get_attribute("type")
	if t == 'Login' or t == 'Clear' :
		print (t)
		option.click()
	if option.get_attribute("name") == 'username':
		option.send_keys('source')


element = driver.find_element_by_class_name('content')
target = driver.find_element_by_name("username1")
print element.text

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.double_click(element).drag_and_drop(element, target).perform()


# driver.quit()