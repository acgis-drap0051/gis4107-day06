#-------------------------------------------------------------------------------
# Name:        Dump12hrClock.py
# Purpose:     Assignment Day 6 #6
#
# Author:      Patrick Drapeau
#
# Created:     10/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

for ampm in ["AM", "PM"]:
    for hh in range(00,12,1):
        if hh == 0:
            hh = 12

        for mm in range(00,60,15):
            print "{:02}:{:02}{}".format (hh,mm,ampm)







