from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")

product_contianers = driver.find_elements_by_class_name('product-container')
for index, product_contianer in enumerate(product_contianers):
    hover = ActionChains(driver).move_to_element(product_contianer)
    hover.perform()

    add_chart_button = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1))
    add_chart_button.click()
    time.sleep(2)

    # Click continue shopping
    driver.find_element_by_css_selector('span.continue.btn.btn-default.button.exclusive-medium').click()
    time.sleep(1)
