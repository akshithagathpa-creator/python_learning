#attendence checkin sys
def check_attendance (attended_classes, total_classes):

    return attended_classes /total_classes * 100

attended_classes = int(input("enter the number of classes you attended: "))
total_classes = int(input("enter the total classes: "))

attendance = check_attendance(attended_classes, total_classes)
if attendance <= 75.0:
    print("not eligible")
else:
    print("eligible!")

print("attendance percent is: ", attendance)

#cateen part 2 thing
items = ['pizza', 'hotdogs', 'ice cream']
price = [100, 120, 100]
print(items, price)
def calculate_bill(no_of_items, price):
    return no_of_items * price
no_of_items = int(input("enter the number of items: "))
price = int(input("enter the price: "))

bill = calculate_bill(no_of_items, price)
if bill >= 500:
    grand_total = bill
    discount = grand_total*0.20
    final_amount = grand_total-discount
    print("your order is applicable for 20% discount: ",final_amount )
elif bill >= 300 and bill <=499:
    grand_total = bill
    discount = grand_total*0.10
    final_price = grand_total-discount
    print("your order gets a 10% discount: ", final_price)
else:
    print("your total is: ", bill)

#library part 2
