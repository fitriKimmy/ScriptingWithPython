from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://sites.google.com/site/httpwwwseleniumhqorg/")

element = driver.find_element_by_xpath('//*[@id="sites-canvas-main-content"]/table/tbody/tr/td/div/div[2]/div[2]/table/tbody/tr/td[1]/center/a[1]/img')
element.click()
driver.back()

search_element = driver.find_element_by_id('jot-ui-searchInput')
search_element.send_keys('web driver')

go_button = driver.find_element_by_class_name('goog-inline-block')
go_button.click()

link_elements = driver.find_elements_by_tag_name('a')
for i in range (len(link_elements)):
    print(link_elements[i].get_attribute('href'))

driver.quit()