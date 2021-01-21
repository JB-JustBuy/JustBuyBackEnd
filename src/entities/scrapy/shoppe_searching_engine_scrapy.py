from src.entities.scrapy.search_engine_scrapy import SearchEngineScrapy


class ShoppeSearchingEngineScrapy(SearchEngineScrapy):
    def __init__(self, driver=None):
        super().__init__(driver)
        self.url = "https://shopee.tw/search?keyword="
        self.platform = "shoppe"

    def parse(self):
        main = self.driver.find_element_by_xpath("//div[@id='main']")
        self._wait("shopee-search-item-result__items")
        elem_row = main.find_element_by_xpath("//div[@class='row shopee-search-item-result__items']")
        names = self.parse_names(elem_row)
        elem_ads = elem_row.find_elements_by_xpath('//div[@data-sqe="ad"]')
        links, prices = self.parse_links_and_prices(elem_row)

        products = []
        for index, (name, link, price) in enumerate(zip(names, links, prices)):
            print("Index:", index)
            print(' name:{}, platform:{}, price:{}\n link:{}\n'.format(name, self.platform, price, link))
            if index >= len(elem_ads):
                product = {
                    "name": name,
                    "price": price,
                    "url": link,
                    "platform": self.platform
                }
                products.append(product)
        return products

    def parse_names(self, elem_row):
        elem_names = elem_row.find_elements_by_xpath('//div[@class="_1NoI8_ _2xHE6C _1co5xN"]')
        names = []
        for elem_name in elem_names:
            name = elem_name.get_attribute("innerHTML").splitlines()[0]
            print('name: ', name)
            names.append(name)
        return names

    def parse_links_and_prices(self, elem_row):
        elem_links = elem_row.find_elements_by_xpath('//a[@data-sqe="link"]')
        links = []
        prices = []
        for elem_link in elem_links:

            link = elem_link.get_attribute("href")
            price = self.parse_price(elem_link)
            links.append(link)
            prices.append(price)
        return links, prices

    def parse_price(self, elem_link):
        elem_price = elem_link.find_element_by_xpath('.//span[@class="_1xk7ak"]')
        price = elem_price.get_attribute("innerHTML")
        return price


if __name__ == '__main__':
    import json
    driver = ShoppeSearchingEngineScrapy.get_driver()
    dc = ShoppeSearchingEngineScrapy(driver)
    dc.search(['魔物獵人'])
    print(json.dumps(dc.result, indent=1))
