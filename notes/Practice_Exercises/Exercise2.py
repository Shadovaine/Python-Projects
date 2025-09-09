# Exercise 2: Shopping Cart Program to calculate total cost of items in a cart

item = input("What item would you like to buy? ")
price = float(input(f"What is the price of {item}? "))
quantity = int(input(f"How many {item}s would you like to buy? "))
total_cost = price * quantity
print(f"The total cost for {quantity} x {item}/s")
print(f"Your total is: ${total_cost}")

