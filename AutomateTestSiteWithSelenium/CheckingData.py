from selenium import webdriver

driver = webdriver.Chrome();
driver.get("https://phptravels.net/offers")

price_element = driver.find_elements_by_class_name('text-secondary')

price_list = []
for price in price_element:
    price_list.append(price.text)

print(price_list)

clean_price_list=[]
for price in price_list:
    if price.startswith('$'):
        # removing first character that contains $
        price_number = price[1:]
        integer_price = int(price_number.replace(',',''))
        clean_price_list.append(integer_price)

print(sorted(clean_price_list))

driver.quit()