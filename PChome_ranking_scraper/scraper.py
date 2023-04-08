from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# tags = []
    
# def scraper_options():
#     tagsElements = driver.find_elements(By.CLASS_NAME, "l-header__tabItem ")
#     for tag in tagsElements:
#         tags.append(tag.text)
        
#     for tag in tags:
#         print(tag)
    
#     return tags
        

def scraper_products(chosen):
    result = []
    if(chosen!="No Selection"):
        driver.get("https://24h.pchome.com.tw/")

        link = driver.find_element(By.LINK_TEXT, chosen)
        link.click()

        bestSellers = driver.find_element(By.XPATH, '//*[@id="bestSellers"]/div[2]/div/ul')
        products = bestSellers.find_elements(By.TAG_NAME, "li")

        i = 1
        for product in products:
            product_title = product.find_element(By.CLASS_NAME, "o-prodInfo__title")
            product_price = product.find_element(By.CLASS_NAME, "o-prodInfo__price")
            result.append("No." + str(i) + " " + product_title.text + " " + product_price.text)
            i+=1

        driver.close()
        
    return result