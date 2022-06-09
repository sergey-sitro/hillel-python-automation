# Go to https://www.saucedemo.com and log in as standard user

# 1st item:
# Find name of 1st item: //*[text()='Sauce Labs Backpack']
# Find description of 1st item: //*[text()='Sauce Labs Backpack']/../following-sibling::div[@class='inventory_item_desc']
# Find price of 1st item: //*[text()='Sauce Labs Backpack']/../../following-sibling::div[@class='pricebar']/div[@class='inventory_item_price']
# Find 'Add to Cart' button of 1st item: //button[@data-test='add-to-cart-sauce-labs-backpack']
# Find picture of 1st item: //img[@alt='Sauce Labs Backpack']

# 2nd item:
# Find name of 2nd item: //*[text()='Sauce Labs Bike Light']
# Find description of 2nd item: //*[text()='Sauce Labs Bike Light']/../following-sibling::div[@class='inventory_item_desc']
# Find price of 2nd item: //*[text()='Sauce Labs Bike Light']/../../following-sibling::div[@class='pricebar']/div[@class='inventory_item_price']
# Find 'Add to Cart' button of 2nd item: //button[@data-test='add-to-cart-sauce-labs-bike-light']
# Find picture of 2nd item: //img[@alt='Sauce Labs Bike Light']

# 3rd item:
# Find name of 3rd item: //*[text()='Sauce Labs Bolt T-Shirt']
# Find description of 3rd item: //*[text()='Sauce Labs Bolt T-Shirt']/../following-sibling::div[@class='inventory_item_desc']
# Find price of 3rd item: //*[text()='Sauce Labs Bolt T-Shirt']/../../following-sibling::div[@class='pricebar']/div[@class='inventory_item_price']
# Find 'Add to Cart' button of 3rd item: //button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]
# Find picture of 3rd item: //img[@alt='Sauce Labs Bolt T-Shirt']

# 4th item:
# Find name of 4th item: //*[text()='Sauce Labs Fleece Jacket']
# Find description of 4th item: //*[text()='Sauce Labs Fleece Jacket']/../following-sibling::div[@class='inventory_item_desc']
# Find price of 4th item: //*[text()='Sauce Labs Fleece Jacket']/../../following-sibling::div[@class='pricebar']/div[@class='inventory_item_price']
# Find 'Add to Cart' button of 4th item: //button[@data-test="add-to-cart-sauce-labs-fleece-jacket"]
# Find picture of 4th item: //img[@alt='Sauce Labs Fleece Jacket']

# 5th item:
# Find name of 5th item: //*[text()='Sauce Labs Onesie']
# Find description of 5th item: //*[text()='Sauce Labs Onesie']/../following-sibling::div[@class='inventory_item_desc']
# Find price of 5th item: //*[text()='Sauce Labs Onesie']/../../following-sibling::div[@class='pricebar']/div[@class='inventory_item_price']
# Find 'Add to Cart' button of 5th item: //button[@data-test="add-to-cart-sauce-labs-onesie"]
# Find picture of 5th item: //img[@alt='Sauce Labs Onesie']

# 6th item:
# Find name of 5th item: //*[text()='Test.allTheThings() T-Shirt (Red)']
# Find description of 5th item: //*[text()='Test.allTheThings() T-Shirt (Red)']/../following-sibling::div[@class='inventory_item_desc']
# Find price of 5th item: //*[text()='Test.allTheThings() T-Shirt (Red)']/../../following-sibling::div[@class='pricebar']/div[@class='inventory_item_price']
# Find 'Add to Cart' button of 5th item: //button[@data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]
# Find picture of 5th item: //img[@alt='Test.allTheThings() T-Shirt (Red)']


# CSS locators:
# Find name of 1st item: $$('#item_4_title_link div')
# Find description of 1st item: $$('#item_4_title_link ~ div')
# Find price of 1st item: $$('#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar > div')
# Find 'Add to Cart' button of 1st item: $$('#add-to-cart-sauce-labs-backpack')
# Find picture of 1st item: $$('#item_4_img_link > img')

# Find name of 2nd item: $$('#item_0_title_link div')
# Find description of 2nd item: $$('#item_0_title_link ~ div')
# Find price of 2nd item: $$('#inventory_container > div > div:nth-child(2) > div.inventory_item_description > div.pricebar > div')
# Find 'Add to Cart' button of 2nd item: $$('#add-to-cart-sauce-labs-bike-light')
# Find picture of 2nd item: $$('#item_0_img_link > img')
