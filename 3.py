
grocery_item = {}
grocery_history = []

stop = False

while not stop:
  name = input("Item name:\n")
  quantity = input ("Quantity purchased:\n")
  cost = input("Price per item:\n")
  tax = input ("Tax:\n")
  grocery_item = {'item_name':name, 'quantity':int(quantity), 'cost':float(cost),  'tax':float(tax)}
  
  grocery_history.append(grocery_item)

  response = input("Would you like to enter another item?\n 'c' for continue or for continue or 'q' to quit: \n")

  if response == 'q':
    stop = True



grand_total = 0

for item in grocery_history:

  item_total = item['quantity'] * item['cost']
  item_total += item_total * item['tax']

  grand_total += item_total

 
  item_total = 0


print("Grand total: €%f" % grand_total)