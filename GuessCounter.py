#-------------------------------------------------------------------------------
# Name:        GuessCounter.py
# Purpose:     Assignment Day 6 #9
#
# Author:      Patrick Drapeau
#
# Created:     16/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import numpy

def main():
    get_guess_count_test()


def get_guess_count(number_to_guess, min_bound, max_bound):
     if number_to_guess > max_bound or number_to_guess < min_bound:
        return 0
     count = 1

     while random.randint(min_bound, max_bound) != number_to_guess:
        count += 1
        if count <= 100000: continue
        if count > 100000: break

     else:
        return count

def get_guess_count_test():
    for i in range(10):
        print (get_guess_count(50,0,100))


if __name__ == '__main__':
    main()