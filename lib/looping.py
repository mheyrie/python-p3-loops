#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

    # code goes here!
    pass

def square_integers(int_list):
    square_list = [ num ** 2 for num in int_list ]
    return square_list 
    # code goes here!
    pass

def fizzbuzz():
    i = 1
    while i <= 100:
        if(i%3 == 0 and i%5 != 0):
            print("Fizz")
        elif(i%5 == 0 and i%3 != 0 ):
            print("Buzz")
        elif(i%3 == 0 and i%5 == 0 ):
            print("FizzBuzz")
        else:
            print(i)
        i+=1

    # code goes here!
    pass
