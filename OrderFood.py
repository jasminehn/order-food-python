import re #regular expressions library (like in CS242); for validating input

running = True #loop used to run each request; loop breaks when a valid input for the user is input, then moves onto the next loop
#I'm using global variables because multiple methods need to access the same variable; global variables are needed to print all the values at the end of the program
global menu #list containing each menu item
global prices #list containing prices for each menu item
deliveryCost = 2 #$2 delivery fee

menu = ["Egg McMuffin", "Sausage McGriddle", "Hash Browns", "Big Mac", "McDouble", "Cheeseburger", "McChicken", "Filet-O-Fish", "Chicken McNuggets", "Iced Coffe", "Soft Drink", "Water", "Happy Meal", "French Fries", "Salad"]
prices = [2.79, 2.79, 1.09, 3.99, 1.39, 1.00, 1.29, 3.79, 4.49, 1.79, 1.29, 1.00, 3.00, 1.79, 4.59]
cost = [] #for keeping track of the cost of each item
customerOrder = [] #for keeping track of each item in the customer order

def fillInfo(): #method to tget the user's information
  print("Welcome to the McDonald's Python ordering service!")
  print("Please fill out the following information. Press enter after each entry. Also, keep in mind that there is a $2 delivery fee.")
  print("")
  while running == True: #loop for getting user's name
    global customer_name
    customer_name = input("Name:") #input statement; sets the variable customer_name to whatever the user enters
    if not re.match("^[a-zA-Z ]*$", customer_name): #checks whether input is letters only
      print("Please use letters only")
    elif len(customer_name) == 0: #user entered nothing
      print("Please enter a valid input")
    else:
      customer_name = customer_name.title()
      break #repeats when invalid input is entered; breaks the loop when valid input has been entered
  while running == True: #loop for getting user's phone number
    global phone
    phone = input("Phone number:")
    if not re.match("^[0-9 ]*$", phone): #checks whether input is numbers only
      print("Please use numbers only")
    elif len(phone) == 0:
      print("Please enter a valid input")
    else:
      break
  while running == True: #loop for getting user's address
    global address
    address = input("Street address:")
    if len(address) == 0:
      print("Please enter a valid input")
    else:
      address = address
      break
  while running == True: #loop for getting user's city
    global city
    city = input("City:")
    if not re.match("^[a-zA-Z ]*$", city): #checks whether input is letters only
      print("Please use letters only")
    elif len(city) == 0:
      print("Please enter a valid input")
    else:
      city = city.title()
      break
  while running == True: #loop for getting user's zipcode
    global zipcode
    zipcode = input("Zipcode:")
    if not re.match("^[0-9 /]*$", zipcode): #checks whether input is numbers only
      print("Please use numbers only")
    elif len(zipcode) == 0 or len(zipcode) > 5:
      print("Please enter a valid zipcode (no more than 5 digits)")
    else:
      break

fillInfo() #execute the actual method

def print_menu():
  print ("""
  -----------------------------------------------
  |               MCDONALD'S MENU               |
  |                                             |
  |                  Breakfast                  |
  |        -----------------------------        |
  |         1. Egg McMuffin       $2.79         |
  |         2. Sausage McGriddle  $2.79         |
  |         3. Hash Browns        $1.09         |
  |                                             |
  |                    Burgers                  |
  |        -----------------------------        |
  |         4. Big Mac            $3.99         |
  |         5. McDouble           $1.39         |
  |         6. Cheeseburger       $1.00         |
  |                                             |
  |             Chicken & Sandwiches            |
  |        -----------------------------        |
  |         7. McChicken          $1.29         |
  |         8. Filet-O-Fish       $3.79         |
  |         9. Chicken McNuggets  $4.49         |
  |                                             |
  |                   Drinks                    |
  |        -----------------------------        |
  |         10. Iced Coffee       $1.79         |
  |         11. Soft Drink        $1.29         |
  |         12. Water             $1.00         |
  |                                             |
  |                    Other                    |
  |        -----------------------------        |
  |         13. Happy Meal        $3.00         |
  |         14. French Fries      $1.79         |
  |         15. Salad             $4.59         |
  |                                             |
  -----------------------------------------------
  """)

print_menu() #execute the actual method

def order():
  global item_num
  while True: #loop for getting quanitiy of items the user wants to order
    try: #validate inputs
      item_num = int(input("How many items would you like to order? The minimum is 1 and the max is 5:"))
      if item_num < 1:
        print("Please order between 1 and 5 items")
        continue #starts back at the beginning of "try"
      if item_num > 5:
        print("Please order between 1 and 5 items")
        continue #starts back at the beginning of "try"
      else:
        break #breaks the loop when a valid input is entered
    except ValueError: #validate input; accepts only numbers and can't be left blank
      print("Please use numbers only")
      continue #starts back at the beginning of "try"

order() #execute the actual method

def itemChoice():
    for i in range(1,item_num+1): #repeats for how many items the user wants to order
      while True: #loop for getting user's item choice
        try:
          which_item = int(input("Enter the number of the item you would like to add to your order:"))
          if which_item < 1: #menu has 15 items, if the user enters
            print("Refer to menu for the item number")
            continue #starts back at the beginning of "try"
          if which_item > 15:#menu has 15 items, if the user enters a number above 15, print error
            print("Refer to menu for the item number")
            continue #starts back at the beginning of "try"
          else:
            item = which_item - 1 #because the items displayed on the menu start at 1, but the items in the lists start at 0
            cost.append(prices[item]) #adds new cost to the cost list
            customerOrder.append(menu[item]) #adds new item to the customerOrder list
            global total_cost
            total_cost = round(sum(cost),2) #adds up everything in the cost list, rounds decimal to 2 points
            global grandTotal
            grandTotal = round(total_cost + deliveryCost, 2) #adds $2 delivery fee
            break #breaks when a valid input is entered and when the for-loop is finished
        except ValueError: #rejects if user enters letter or levaes it blank
          print("Please use numbers only")
          continue #starts back at the beginning of "try"

itemChoice() #execute the actual method

def customerDetails(): #prints customer order and details
  print ("")
  print ("CUSTOMER and ORDER DETAILS")
  print ("")
  print ("Name:", customer_name)
  print ("Phone number:", phone)
  print ("Address:", address)
  print ("        ", city)
  print ("        ", zipcode)
  print ("ORDER:", customerOrder)
  print ("Total: $", total_cost)
  print ("Total + Delivery: $", grandTotal)

customerDetails() #execute the actual method

print ("")
def confirm(): #method to confirm the user's order
  confirmation = input("Enter Y to confirm your order, or enter N to reset the order:")
  confirmation = confirmation.upper() #changes the letter inputted to an uppercase
  if confirmation == "Y": #if Y is entered, order is confirmed
    print("ORDER CONFIRMED")
  elif confirmation == "N": #if N is entered, order is cancelled; goes through all the steps again
    print("ORDER CANCELLED - information has been reset")
    customerOrder[:] = []
    cost[:] = []
    print_menu()
    order()
    itemChoice()
    customerDetails()
    confirm()
  else:
    print("Please enter Y or N")
    confirm() #if invalid input is entered, call confirm() again to start the method over

confirm()#execute the actual method

def goodbye(): #needed for the program not to crash on "exit"
    print ("")
    print ("THANK YOU FOR YOUR ORDER")
    print ("Your order will be delivered in 15 minutes")
    bye = input("Type 'exit' to end the McDonald's Python ordering service:") #(anything can be typed here, the program just needs one more input to display the last of the text before closing)

print ("")
def orderAgain(): #method to determine if the user wants to add items to their order
  order_more = input("Enter Z to order more, or enter X to exit the program:")
  order_more = order_more.upper() #capitalizes the user's input
  #'''cost[:] = []'''
  if order_more == "Z": #runs through steps one more time so the user can add items
    print_menu()
    order()
    itemChoice()
    customerDetails()
    confirm()
    goodbye()
  elif order_more == "X": #calls method to end the program
    goodbye()
  else:
    print ("Please enter X or Z")
    orderAgain() #if invalid input is entered, call confirm() again to start the method over

orderAgain() #execute the actual method
