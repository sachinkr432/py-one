has_good_credit = True
price = 1000000
if has_good_credit:
    price -= price * 0.1
else:
    price -= price *0.2
print("Down payment is " + str(price))