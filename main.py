

'''
ATM Project for cash DRAWING for weekly Max Limit
'''

LIMIT = 600
drwaing_list = []
TOTAL_D = 0
DRAWING = 0

while TOTAL_D < LIMIT :
    try:
        DRAWING = int(input("Enter the amount: "))
    except ValueError:
        print("Not valid entry")
        continue

        if DRAWING > LIMIT or TOTAL_D > LIMIT:
            print('Operation Not Excuted over limit take your card ')
        break
    if DRAWING + TOTAL_D > LIMIT :
        print(f"Amount demanded is over limit, Available balance is :{LIMIT - TOTAL_D}  ")
    else:
        drwaing_list.append(DRAWING)
        TOTAL_D += DRAWING
        print('Available balance is :' )
        print(drwaing_list)
#**************************
#2nd fase(date)
'''
ATM Project for cash DRAWING for weekly Max Limit
'''

import datetime

LIMIT = 600
drawing_list = []
TOTAL_D = 0
list_date = []

while TOTAL_D < LIMIT:
    try:
        DRAWING = int(input("Enter the amount: "))
    except ValueError:
        print("Not a valid entry")
        continue
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp

    # Remove withdrawals older than 7 days
    # temporey in second for testing purposes
    while len(list_date) > 0 and (datetime.datetime.now() - datetime.datetime.
            strptime(list_date[0], "%Y-%m-%d %H:%M:%S")).seconds > 7:
        if len(drawing_list) > 0:
            # Subtract the first element from TOTAL_D and remove it from drawing_list
            TOTAL_D -= drawing_list.pop(0)
            list_date.pop(0)

    if DRAWING + TOTAL_D > LIMIT:
        print(f"Amount demanded is over the limit. Available balance is: {LIMIT - TOTAL_D}")
    else:
        drawing_list.append(DRAWING)
        TOTAL_D += DRAWING
        list_date.append(timestamp)
        print(f"Available balance is: {LIMIT - TOTAL_D}")
        print(drawing_list)
        print(list_date)
