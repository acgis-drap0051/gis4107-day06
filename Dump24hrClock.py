#-------------------------------------------------------------------------------
# Name:        Dump24hrClock.py
# Purpose:     Assignment Day 6 #5
#
# Author:      Patrick Drapeau
#
# Created:     10/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

for hh in range(00,24,1):
    for mm in range(00,60,15):
        print "{:02}:{:02}".format (hh,mm)



