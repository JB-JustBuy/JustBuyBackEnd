from src.scraper.pchome_data_controller import PChomeDataController
from src.scraper.shoppe_data_controller import ShoppeDataController
from src.merchandise.merchandise import Merchandise
from src.feedback_method.feedback_method import FeedBackMethod
from src.feedback_constraint.single_full import SingleFull
from src.feedback_form.cash import Cash
from src.payment.credit_card import CreditCard
keyword = input("Please input the product name and mode:")

pchome = PChomeDataController()
pchome.search(keyword)
pchome_products = pchome.products

shoppe = ShoppeDataController()
shoppe.search(keyword)
shoppe_products = shoppe.products

merchandises = Merchandise.generate_merchandises(shoppe_products)
shoppe_merchandise = Merchandise.find_the_cheapest(merchandises)
print("The cheapest merchandise(pick from shoppe):\n  name:{}\n   price:{}\n  platform:{}\n url:{}".format(
    shoppe_merchandise.name,
    shoppe_merchandise.price,
    shoppe_merchandise.platform,
    shoppe_merchandise.url
))

merchandises = Merchandise.generate_merchandises(pchome_products)
pchome_merchandise = Merchandise.find_the_cheapest(merchandises)
print("The cheapest merchandise(pick from pchome):\n  name:{}\n   price:{}\n  platform:{}\n url:{}".format(
    pchome_merchandise.name,
    pchome_merchandise.price,
    pchome_merchandise.platform,
    pchome_merchandise.url
))


form1 = Cash(amount=100)
form2 = Cash(pct=0.03)
constraint1 = SingleFull(amount=1000)
constraint2 = SingleFull(amount=900, platform='shoppe')
method1 = FeedBackMethod(constraint1, form1)
method2 = FeedBackMethod(constraint2, form2)

print("Shoppe Merchandise in Method(001) feedback:", method1.feedback([shoppe_merchandise]))
# 這個怪怪的 單筆超過900回饋0.03, 但目前僅以900*0.03計算=27, 未考慮(超過部分）
print("Shoppe Merchandise in Method(002) feedback:", method2.feedback([shoppe_merchandise]))

print("PChome Merchandise in Method(001) feedback:", method1.feedback([pchome_merchandise]))
# 這個怪怪的 單筆超過900回饋0.03, 但目前僅以900*0.03計算=27, 未考慮(超過部分）
print("PChome Merchandise in Method(002) feedback:", method2.feedback([pchome_merchandise]))

# New Payment
credit_card = CreditCard("fuck", "玉山銀行")
credit_card.add_method()
