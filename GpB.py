import datetime as dt
import csv
import random

#1. Function 1, Check Digit
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
# Testing, checkDigit()
#print(checkDigit(123456,567878,'B'))

# Function 2, Cost Verification Procedure (ask professor)
def Cost_Verification_Procedure(items, discount_1, discount_2):
    sub_total = 0
    discount = 0
    # calculate the sub_total
    for item in len(items):
        sub_total += item[1] * item[2]

    # calculate the total discount
    discount += sub_total * discount_1
    discount += sub_total * discount_2

    # calculate the delivery_fees
    if sub_total >= 500:
        delivery_fees = 0
    else: delivery_fees = 50

    return sub_total - discount + delivery_fees

# Function 3 Hash Total:
# last two digital of the order number:
def hashTotal(item_numbers):
    total = 0
    for item_number in item_numbers:
        last_two_digits = int(item_number[-2:])
        total += last_two_digits
    return total
# ask user to input the order number, if number of order is more than 15, then go to another hash total function:
item_numbers = []
item_number = input("Input an item number (or 'q' to quit): ")
while item_number != 'q' and len(item_numbers) <= 9:
    item_numbers.append(item_number)
    item_number = input("Input an item number (or 'q' to quit): ")
print(hashTotal(item_numbers))

# Function 4 mall dollar:
def mallDollar(total):
    if total >= 1000:
        mall_dollar = total * 0.002
    else:
        mall_dollar = 0
    return mall_dollar

# input for each order
# def order_input():
#   global a, b, c, d, e, f, g, h, items
#   itemNum = 4
#   discount_1 = 1 / 100
#   discount_2 = 5 / 100
#   for item in itemNum:
#       items[item][0] = input("Input item no: ")
#       items[item][1] = input("Input qty:")
#       items[item][2] = input("Input cost: ")
#   total = Cost_Verification_Procedure(items, discount_1, discount_2)
  
# input for each order, each order must less than or equal to 9 items: 
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
        num_part = "000000"
    for zeroNum in range(6 - len(num_part)): # make sure 6 digit
        num_part = "0" + num_part
    new_order_no = alphabet + str("-") + num_part
        
            
    # ask the users to input the item number, quantity and price
    # create a temp item_list, if the number of item is more than 9, go to next oder
    item_list = []
    item_number = input("Input an item number (or 'q' to quit): ")
    while item_number != 'q' and len(item_list) <= 9:
        item_list.append(item_number)
        item_number = input("Input an item number (or 'q' to quit): ")

    # if the number of item is more than 9, then cauculate the total
    if len(item_list) > 9:
        sub_total = Cost_Verification_Procedure(items, discount_1, discount_2)
        hash_total = hashTotal(item_list)
        print("Hash Total: ", hash_total)
        print("Sub Total: ", sub_total)
    else:
        # if the number of item is less than 9, then ask the user if it is enough for this order
        enough = input("Is it enough for this order? (y/n)")
        if enough == 'y':
            # if the user said it is enough, then calculate the total
            sub_total = Cost_Verification_Procedure(items, discount_1, discount_2)
            hash_total = hashTotal(item_list)
            print("Hash Total: ", hash_total)
            print("Sub Total: ", sub_total)
        else:
            return
        ## needed to be adjusted and continue

  
# Function 5, arbitrary assigned the customer name and adress with condition statement within the function
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
    
name_adress(123456)
# main program
try:
    while True:
        ordersNum = int(input("Number of orders (1-15): "))
        if type(ordersNum) == int:
            if ordersNum >= 1 and ordersNum <= 15:
                break
            print("Range from 1 to 15. Input again.")
        else: print("Please enter a number.")
except:
    print("Unknown error occur.")
else:
    for i in range():
        order_input()
        

        
# read csv file
"""
with open('ItemFile.csv', encoding="utf-8-sig") as item:
    csv_reader = csv.reader(item)
    # skip the header
    next(csv_reader)
    for line in csv_reader:
        sub_total += float(line[3])
"""
