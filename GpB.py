import pandas as pd
import datetime as dt

#1. Fucntion 1 Check Digit:
def checkDigit(staff_number,order_number,alphabet):
    if alphabet == 'A':
        alphabet = 9
    elif alphabet == 'B':
        alphabet = 8
    elif alphabet == 'C':
        alphabet = 7
    elif alphabet == 'D':
        alphabet = 6
    staff_number = str(staff_number)
    order_number = str(order_number)
    check_digit = 0
    check_digit_1 = 0
    for i in range(len(staff_number)):
        check_digit += int(staff_number[i]) * int(order_number[i])
    while check_digit % alphabet != 0:
        check_digit += 1
        check_digit_1 += 1
    return check_digit_1

# Function 2 Cost Verification Procedure: (ask professor)
def costVerificationProcedure(discount_1, discount_2):
    if discount_1 != 0:
        if sub_total >= 500 and num_of_items <= 9:
            delivery_fees = 0
        else:
            delivery_fees = 50
    elif discount_2 != 0:
        sub_total = sub_total * 0.95


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
  
