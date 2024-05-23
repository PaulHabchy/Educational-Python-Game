import random

def dunkAttempt():
    print('Welcome to Basketball: Type "DUNK" to try to dunk the ball')
    i = random.randint(1,4)
    x = input('')
    if x == "DUNK":
        if i == 1:
            print('You just dunked!')
        else:
            print('You missed the dunk')
            print('Ouch that looked like quite the fall, heres a safety fact that could help you out next time')
            num = random.randint(1, 10)
            if num == 0:
                print('The best way to prevent bruises is to make sure our capillaries are strong and flexible')
            if num == 1:
                print('A way to help prevent sprains is just by warming up')
            if num == 2:
                print('A way to help prevent strains is to use proper technique')
            if num == 3:
                print('A way to help prevent joint injuries is to cross train muscles')
            if num == 4:
                print('Nose bleeds are pretty in-preventable but when you get one just take care of it')
            if num == 5:
                print('You should wear protective gear if you are very prone to wrist injuries and just watch out but it is pretty unpreventable')
            if num == 6:
                print('Building strength in your hand and using good form can prevent a lot of hand injuries')
            if num == 7:
                print('Warm and conditioning are good way to prevent ankle injuries ')
            if num == 8:
                print('Wearing the right shoes can help a lot preventing foot injuries')
            if num == 9:
                print('A good way to prevent collarbone injuries are wearing the right gear and strengthening your collarbone')
            print('Type "RETRY" to try again')
            if num == 10:
                print('The best way to prevent bruises is to make sure our capillaries are strong and flexible')
            y = input('')
            if y == 'RETRY':
                print('Everyone deserves a second chance!')
                dunkAttempt()
            else:
                "You gave up :("
    else:
        print('You did not attempt to dunk the ball')

dunkAttempt()