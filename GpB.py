import datetime as dt
import csv
import random

# 1, Check Digit
def checkDigit(staff_number,order_number,alphabet):
    if alphabet == 'A':
        modulus = 9
    elif alphabet == 'B':
        modulus = 8
    elif alphabet == 'C':
        modulus = 7
    elif alphabet == 'D':
        modulus = 6
    staff_number = str(staff_number)
    order_number = str(order_number)
    result = 0
    for i in range(len(staff_number)):
        result += int(staff_number[i]) * int(order_number[i])
    return modulus - (result % modulus)

def cal_sub_total(items):
    sub_total = 0
    for item in len(items):
        sub_total += item[3]
    return sub_total

# 2, Cost Verification Procedure
def Cost_Verification_Procedure(items, discount_1, discount_2):
    discount = 0
    sub_total = cal_sub_total(items)

    # calculate the total discount
    discount += discount_1
    discount += sub_total * discount_2

    # calculate the delivery_fees
    if sub_total >= 500:
        delivery_fees = 0
    else: delivery_fees = 50

    return sub_total - discount + delivery_fees

# 3, Hash Total:
# last two digital of the order number:
def hashTotal(item_numbers):
    total = 0
    for item_number in item_numbers:
        last_two_digits = int(item_number[0][-2:])
        total += last_two_digits
    return total

# 5, mall dollar:
def mallDollar(total):
    if total >= 1000:
        mall_dollar = total * 0.002
    else:
        mall_dollar = 0
    return mall_dollar
  
# input for each order,
def order_input():
    # Determine the order number from the order file
    # First, get the last order number
    with open('OrderFile.csv', encoding="utf-8-sig") as orders:
        csv_reader = csv.reader(orders)
        next(csv_reader) # skip the header
        for line in csv_reader:
            last_order_no = line[0]
    # Then, get the new order number
    alphabet = last_order_no[0]
    num_part = str(int(last_order_no[-6:]) + 1)
    if len(num_part) > 6:
        if alphabet == "Z": # If Z encountered change to A
            alphabet = chr(ord(alphabet)-25)
        else: # Next Letter in alphabet
            alphabet = chr(ord(alphabet) + 1)
        num_part = "000001"
    for zeroNum in range(6 - len(num_part)): # make sure 6 digit
        num_part = "0" + num_part
    new_order_no = alphabet + str("-") + num_part
    
    # Input staff number
    while True:
        try:
            staff_number = input("Enter your staff number(6 digit): ")
            staff_number = int(staff_number)
            if len(staff_number) == 6:
                break
            print("Staff number should in 6 digit. Enter again.")
        except:
            print("Please enter a number.")
            
    # Input numbers of items within the order 
    global ordersNum
    while True:
        try:
            numberOFItems = input("Enter number of items within this order (or 'q' to quit): ")
            numberOFItems = int(numberOFItems)
            if numberOFItems > 9:
                if ordersNum == 15:
                    print("The number of orders is 15.")
                    print("You are not allow to create another order.")
                    print("Enter number of items within 9 again.")
                else:
                    print("The number of items more than 9.")
                    print("One order can only have at most 9 items")
                    print("Another order will be created.")
                    numberOFItems = 9
                    ordersNum += 1
                    break
            elif numberOFItems <= 0:
                print("The number of items should not be 0 or less than 0. Enter again.")
            else: break
        except:
            print("Please enter a number.")

    # Input item number, quantity and price
    item_list = [] # create a list, for recording item in the order
    # fill item_list
    while True:
        item_number = input("Enter an item number (or 'q' to quit): ")
        isExist = False
        if len(item_list) == numberOFItems:
            break
        if item_number == 'q':   
            # if the number of item is less than number of items, 
            # then ask the user to confirm for ending input the order
            confirm = input("Confirm for ending this order? (y/n)  ")
            if confirm == 'y':
                break
            
        # check if the item exist
        with open('ItemFile.csv', encoding="utf-8-sig") as ItemFile:
            csv_reader = csv.reader(ItemFile)
            next(csv_reader) # skip the header
            for line in csv_reader:
                if item_number == line[0]:
                    item_list.append(line)
                    while True:
                        try:
                            quantity_number = input("Enter the quantity number of the item: ")
                            quantity_number = int(quantity_number)
                            if quantity_number <= 0:
                                print("Quantity number should not be 0 or negative.")
                                continue
                        except:
                            print("Invalid number.")
                        else:
                            break
                    item_list.append([line[0], line[1], quantity_number, quantity_number * line[2]])
                    isExist = True
                    break
            if not isExist:
                print("Failed to find the item.")

    # calculate the sub-total
    sub_total = cal_sub_total(item_list)

    # input the discount
    while True:
        try:
            discount_1 = input("Enter the 1st discount of the order in dollar($) (if no, enter 0): ")
            discount_1 = float(discount_1)
            if discount_1 / sub_total >= 1 / 100:
                print("Actual amount of discount can only be less than 1% of the sub-total.")
            elif discount_1 < 0:
                print("Discount can not be negative.")
            else: break
        except:
            print("Invalid amount of discount. Enter again.")
    while True:
        try:
            discount_2 = input("Enter the 2nd discount of the order in percentage(%) (0 to 5%): ")
            discount_2 = float(discount_2) / 100
            if discount_2 < 0 or discount_2 > 0.05:
                print("Invalid amount of discount. Enter again.")
            else: break
        except:
            print("Invalid amount of discount. Enter again.")

    # hash total
    global hash_total_list
    hash_total = hashTotal(item_list)
    hash_total_list.append(hash_total) # for calculate the new hash total

    # order total payment
    total = Cost_Verification_Procedure(item_list, discount_1, discount_2)

  
# Function 5, arbitrary assigned the customer name and adress with condition statement within the function
    return [new_order_no, hash_total, total]
def name_adress(customer_number):
    with open('CustomerAddress.csv', encoding="utf-8-sig") as customer:
        csv_reader = csv.reader(customer)
        # skip the header
        next(csv_reader)
        for line in csv_reader:
            if int(line[0]) == customer_number:
                customer_name = line[1]
                customer_address = line[2]
                return customer_number,customer_name, customer_address
            else:
                #add new customer, save into the csv and genereate a new customer number to the customer
                customer_name = input("Please input the customer name: ")
                customer_address = input("Please input the customer address: ")
                #generate random a new customer number 6 ditgis
                customer_number = random.randint(100000,999999)
                #save into the csv
                with open('CustomerAddress.csv', 'a', newline='') as customer:
                    csv_writer = csv.writer(customer)
                    csv_writer.writerow([customer_number, customer_name, customer_address])
                    # stop the loop and return the customer name and address
                    return customer_name, customer_address    
# name_adress(123456)

# main program
global ordersNum
while True:
    try:
        ordersNum = input("Number of orders (1-15): ")
        ordersNum = int(ordersNum)
        if ordersNum >= 1 and ordersNum <= 15:
            break
        print("Range from 1 to 15. Input again.")
    except:
        print("Please enter a number.")
for i in range(ordersNum):
    print("Order " + str(i+1) + " input:")
    order_input()
    print() # Empty line
    # output()
