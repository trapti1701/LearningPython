list=['apple', 'banana', 16, 1, 11.2, 22, 22, 22, 55, 0, 'bye bye']

for item in list :
    if str(item).isnumeric() and item>6:
        print(item)

    elif str(item).isnumeric() and item < 6:
            print('this is number less than 6')

    else :
        print('this is not a number')