import pandas as pd
import datetime as dt

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
#    while check_digit % modulus != 0:
#        check_digit += 1
#        check_digit_1 += 1
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


# Function 3 Hash Toal:
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
def order_input():
  global a, b, c, d, e, f, g, h, items
  itemNum = 4
  discount_1 = 1 / 100
  discount_2 = 5 / 100
  for item in itemNum:
      items[item][0] = input("Input item no: ")
      items[item][1] = input("Input qty:")
      items[item][2] = input("Input cost: ")
  total = Cost_Verification_Procedure(items, discount_1, discount_2)

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

