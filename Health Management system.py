#diet
#exercise
#three clients
#
# 3 files to log their food
# 3 files to log their exercise

# write a function that when executed takes client name as input
# one function to store data and one function to retrieve data

def log(b):

    if b==1:
        choice = int(input('Enter 1 for exercise and 2 for diet'))
        if choice==1:
            with open('Shubham_exercise.txt', 'a') as s:
                ex1=input('Enter the exercise name')
                s.write(ex1 + ",")
                print('Entry logged successfully')

        elif choice==2 :
            with open('Shubham_diet.txt', 'a') as s:
                d1 = input('Enter the food name')
                s.write(d1 + ",")
                print('Entry logged successfully')

        else :
            print('enter correct option')

    elif b==2:
        choice = int(input('Enter 1 for exercise and 2 for diet'))
        if choice == 1:
            with open('Trapti_exercise.txt', 'a') as s:
                ex1 = input('Enter the exercise name')
                s.write(ex1 + ",")
                print('Entry logged successfully')

        elif choice == 2:
            with open('Trapti_diet.txt', 'a') as s:
                d1 = input('Enter the food name')
                s.write(d1 + ",")
                print('Entry logged successfully')
        else:
            print('enter correct option')

    elif b==3 :
        choice = int(input('Enter 1 for exercise and 2 for diet'))
        if choice == 1:
            with open('Dipti_exercise.txt', 'a') as s:
                ex1= input('Enter the exercise name')
                s.write(ex1 + ",")
                print('Entry logged successfully')

        elif choice == 2:
            with open('Dipti_diet.txt', 'a') as s:
                d1= input('Enter the exercise name')
                s.write(d1 + ",")
                print('Entry logged successfully')

        else:
            print('enter correct option')

    else :
        print('enter correct option')


def retrieve(b):

    if b == 1:
        choice = int(input('Enter 1 for exercise and 2 for diet'))
        if choice == 1:
            with open('Shubham_exercise.txt') as s:
                print(s.readlines())

        elif choice == 2:
            with open('Shubham_diet.txt') as s:
                print(s.readlines())

        else:
            print('enter correct option')

    elif b == 2:
        choice = int(input('Enter 1 for exercise and 2 for diet'))
        if choice == 1:
            with open('Trapti_exercise.txt') as s:
                print(s.readlines())

        elif choice == 2:
            with open('Trapti_diet.txt') as s:
                 print(s.readlines())
        else:
            print('enter correct option')

    elif b == 3:
        choice = int(input('Enter 1 for exercise and 2 for diet'))
        if choice == 1:
            with open('Dipti_exercise.txt') as s:
                print(s.readlines())

        elif choice == 2:
            with open('Dipti_diet.txt') as s:
                print(s.readlines())
        else:
            print('enter correct option')

    else :
        print('enter correct option')

print('health management system')
a=int(input('enter 1 to log and 2 to retrieve'))
if a==1:
    b=int(input('enter 1 for Shubham, 2 for Trapti and 3 for Dipti'))
    log(b)

else :
    b=int(input('enter 1 for Shubham, 2 for Trapti and 3 for Dipti'))
    retrieve(b)

