from src.entities.scraper.pchome_data_controller import PChomeDataController
from src.entities.scraper.shoppe_data_controller import ShoppeDataController
from src.entities.merchandise.merchandise import Merchandise
from src.entities.feedback_method.feedback_method import FeedBackMethod
from src.entities.feedback_constraint.single_full import SingleFull
from src.entities.feedback_form.cash import Cash
from src.entities.payment.credit_card import CreditCard



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
