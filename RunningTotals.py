#-------------------------------------------------------------------------------
# Name:        RunningTotals.py
# Purpose:     Assignment Day 6 #7
#
# Author:      Patrick Drapeau
#
# Created:     14/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    test_RuningTotals()

def RuningTotals(iteration):
    numlist = list()
    while ( True ) :
        a = iteration + 1
        while a >= 0:
            a -= 1
            value = int(a)
            numlist.append(value)
            total = sum(numlist)
        else:
            return 'total:' + str(total + 1)
            break

def test_RuningTotals():
    print RuningTotals(5)

if __name__ == '__main__':
    main()
