# i=1
#
# while (True) :
#     if i<5 :
#         i=i+1
#         print('hello', end =' ')
#         continue
#
#     print(i, end = ' ')
#     i=i+1
#     if i==45 :
#         break


# while (True):
#     a= int(input('enter your number: '))
#
#     if a>100 :
#         print('congratulations you have entered a number greater than 100 \n')
#         break
#
#     else :
#         print('try again!')
#         continue

#Guess the number

print('Welcome to number guessing game!!\nPlease note you will be give total 5 guesses to guess the number.')
i = 18
Guesses = 1
while (True):
    if Guesses > 5:
        print('Game over!!')
        break

    a = int(input('Guess the number :\n'))
    if a > i and Guesses <= 5:
        print('Your number is greater! \nPlease guess smaller one! \nNumber of guesses remaining is', 5-Guesses,'!')
        Guesses = Guesses +1
        continue

    if a < i and Guesses <= 5:
        print('Your number is smaller! \nPlease guess larger one! \nNumber of guesses remaining is', 5-Guesses,'!')
        Guesses = Guesses + 1
        continue

    if a == 18 and Guesses <= 5:
        print('Congratulations!!! Your guess is correct.\nYou won the game in', Guesses, 'guesses.')
        break








