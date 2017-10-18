#-------------------------------------------------------------------------------
# Name:        RunningTotalsStrange.py
# Purpose:     Assignment Day 6 #8
#
# Author:      Patrick Drapeau
#
# Created:     10/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from operator import truediv

def main():
    test_strange_sum()

def strange_sum(number):
    a = number
    lista = range(1,a +1)
    listb = range(a,0,-1)
    div = sum(map(truediv, lista, listb))
    return div

def test_strange_sum():
    print strange_sum(1)
    print strange_sum(10)
    print strange_sum(100)

if __name__ == '__main__':
    main()




