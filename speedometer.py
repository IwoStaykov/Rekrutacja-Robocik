import math
import receiver #module of a receiver function

t = receiver.delay() #download time of delay and return in  an integer

sp = receiver.receiver() #download initial coordinates and return in a tuple

a = sp[0]
b = sp[1]
c = sp[2] #assign tuple (sp) values to variables a, b and c

coordinates = receiver.location() #download current coordinates and return in a tuple

x = coordinates[0]
y = coordinates[1]
z = coordinates[2] #assign tuple (coordinates) values to variables x, y and z
print(x, y, z)

speed = math.sqrt((a - x) ** 2 + (b - y) ** 2 + (c - z) ** 2) / t #calculate speed (units per seconds)
print(speed)