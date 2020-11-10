import urllib.request
import urllib.parse

def receiver(): #download initial coordinates from the server
    url_SP = 'http://localhost:8888/StartingPoint.txt' #url of a page with coordinates of a submarine at the beginning
    a = float(urllib.request.urlopen(url_SP).readline().decode('UTF-8')) #convert string to float (unfortunately it doesn't work in general program)
    b = float(urllib.request.urlopen(url_SP).readline().decode('UTF-8'))
    c = float(urllib.request.urlopen(url_SP).readline().decode('UTF-8'))
    return a, b, c
    


def location(): #download current coordinates from the server
    url_c = 'http://localhost:8888/coordinates.txt' #url of a page with current coordinates
    x = float(urllib.request.urlopen(url_c).readline().decode('UTF-8')) #convert string to float (same problem as above)
    y = float(urllib.request.urlopen(url_c).readline().decode('UTF-8'))
    z = float(urllib.request.urlopen(url_c).readline().decode('UTF-8'))
    return x, y, z


def delay(): #download time of delay from the server
    url_t = 'http://localhost:8888/delay.txt' #url of a page with given time of delay
    t = int(urllib.request.urlopen(url_t).readline().decode('UTF-8')) #convert string to integer
    return t