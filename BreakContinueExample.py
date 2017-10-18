#-------------------------------------------------------------------------------
# Name:        BreakContinueExamples.py
# Purpose:     Day 6 #1
#
# Author:      Patrick Drapeau
#
# Created:     10/10/2017
# Copyright:   (c) MCE 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


x = 0
while x <= 4:
    x += 1
    if x == 2: continue
else:
    print "loop done"



for i in [1,2,3,4]:
    if i == 2: continue
    if i == 3: break
    print 1
else:
    print "loop done"