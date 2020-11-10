MAX = 1000
MIN = -1000 # limits of space

import os
import time
import random as r # to select random coordinates


n = int(input('Enter amount of signals\n')) #number of signals
t = int(input('Enter time (frequency of sending current coordinates\n')) #delay
a = float(input('Enter the 3 coordinates where the submarine should appear\n')) 
b = float(input())
c = float(input()) #initial coordinates


Time = open("delay.txt", "w+") 
Time.write(str(t)) #save time of dalay into delay file
Time.close()


start = [a, b, c] #coordinates to send to the history file
s = open("StartingPoint.txt", "w+") #coordinates of the submarine at the starting point
s.write(str(a) + "\n")
s.write(str(b) + "\n")
s.write(str(c)) #save coordinates into StartingPoint file
h = open("history.txt", "r+") #a text file with all the coordinates of a submarine 
h.write(str(start) + '\n') #save coordinates into history file
h.close()


for k in range(n):
    h = open("history.txt", "r+") # a text file with all coordinates of a submarine when the program is running
    c = open("coordinates.txt", "w+") # a text file with latest two coordinates
    x = r.uniform(MIN,MAX)
    y = r.uniform(MIN,MAX)
    z = r.uniform(MIN,MAX) # x, y and z are the current coordinates of the submarine
    c.write(str(x) + "\n")
    c.write(str(y) + "\n")
    c.write(str(z)) # saving coordinates to coordinates file
    c.close()
    os.system("speedometer.py") #start the program which calculates speed
    next = [x, y, z] # next coordinates to send to history file
    h.write(str(next) + "\n") # saving coordinates
    h.close()
    time.sleep(t) #delay