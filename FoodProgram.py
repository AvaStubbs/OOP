import FoodClass as fc
customer = fc.Customer(570, "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", False)
#customer = fc.Customer(569, "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", "ahimsworthfs@list-manage.com", "254-555-2273", True)

dict = {
    'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
    'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
    'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
    'trans4': ['2/15/2023', 'The Octoburger', 20, 570]
}

print("Customer Information")
print("--------------------")
print("Name:   ", customer.get_name())
print("Addr:   ", customer.get_address())
print("Email:  ", customer.get_email())
print("Phone:  ", customer.get_phone())
print("Member: ", "Yes" if customer.get_member_status() else "No")
print()

print("Order Information")
print("--------------------")

order_total = 0

for key in dict:
    if dict[key][3] == customer.get_customerid():
        trans = fc.Transaction(dict[key][0], dict[key][1], dict[key][2], dict[key][3])
        print(trans.get_date(), format(trans.get_item_name(), '20s'), "$", format(trans.get_cost(), '.2f'))
        order_total = order_total + trans.get_cost()

print()

if customer.get_member_status():
    discount = order_total * 0.2
    final_total = order_total - discount
    print("Subtotal:                   $", format(order_total, '.2f'))
    print("Discount:                   $", format(discount, '.2f'))
    print("Total:                      $", format(final_total, '.2f'))
else:
    print("Total:                      $", format(order_total, '.2f'))
