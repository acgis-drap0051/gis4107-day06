#-------------------------------------------------------------------------------
# Name:        GuessCounterWithHint.py
# Purpose:     Assignment Day 6 #10
#
# Author:      Patrick Drapeau
#
# Created:     16/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import math


def main():

    max1 = 0
    min1 = 100000
    sum = 0

    def get_guess_count(number_to_guess, min_bound, max_bound):
     global count
     count = 1
     maximum = 100000

     if number_to_guess > max_bound or number_to_guess < min_bound:
        return 0
     firstGuess = random.randint(min_bound, max_bound)

     while random.randint(min_bound, max_bound) != number_to_guess:
        count += 1
        firstGuess = random.randint(min_bound, max_bound)

        if firstGuess > number_to_guess:
            max_bound = firstGuess
        else:
            min_bound = firstGuess
        if count <= maximum: continue
        if count > maximum: break

     else:
        return count

    for i in range(10):
        print get_guess_count(50,0,100)
        if count >= max1:
            max1 = count
        if count <= min1:
            min1 = count
        sum = (sum + count)
        avg = sum/float(i+1)


    print "Maximum number of guesses is: " + str(max1)
    print "Minimum number of guesses is: " + str(min1)
    print "Average number of guesses is: " + str(avg)

if __name__ == '__main__':
    main()