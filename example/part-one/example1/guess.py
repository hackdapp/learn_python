#!/usr/bin/python

guess = -1
number = 7

while(True):
    guess = input('input the guess number:')

    if guess == number:
        print 'right!'
        break
    elif guess < number:
        print 'it\'s not bigger'
    elif guess > number:
        print 'bigger'
