has_good_credit = True
price = 1000000
if has_good_credit:
    dwn_pmnt = price * 0.1
else:
    dwn_pmnt = price *0.2
print("Down payment is " + str(dwn_pmnt))