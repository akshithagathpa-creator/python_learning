#college cateen ordering system

menu = ['pizza', 'hotdogs', 'chocolate cake', 'macaroni']
price =[100, 100, 150, 120]

orders = []
total = 0

#def display_menu():
print("------MENU-------")

for i in range(len(menu)):
 print(menu [i], '-', price[i])

 #def take_orders():

while True:
    order = input("\n enter your order(or type 'done' when over):  ").lower()

    if order == "done":
        break

    if order not in menu:
        print("item not available")
        continue
    orders.append(order)

    #return orders
  #def calculate_total(orders):

    if order == 'pizza':
        total += 100
    elif order == 'hotdogs':
        total += 100
    elif order == 'chocolate cake':
        total += 150
    elif order == 'macaroni':
        total += 120
    #return total


#def print_receipet(orders, total):
     
    print("\n-------Receipt------")
    count = 1
    for item in orders:
        print(count, '-', item)
        count += 1

    print("Total Amount: ",total)

#it doesn't let 2 items enter at once how to do that 
      
    


 