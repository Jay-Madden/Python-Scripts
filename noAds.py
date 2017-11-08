#!/usr/bin/env python3
import webbrowser
import os
import urllib2
#clears screen
print(chr(27) + "[2J")

print("Go to streamlord and navigate to the page of the show/movie you want to watch and copy the URL\n")
print("Please Enter the web address")
web_address = raw_input()

response = urllib2.urlopen( str(web_address))
source = response.read()
#writes orig to file
f = open("streamlord.html", "w+")
f.write(str(source))
lines = f.readlines()
f.close()


f = open("streamlord.html", "r")
line = f.readlines()
f.close()

count = 0

f = open("streamlord.html", "w")
for line in line:
    count = count + 1
    if line == "<!-- START AD CODE -->":
        while line != "</body>":
            f.write(" ")
    else:
        f.write(line)

f.close()

webbrowser.open('file://' + os.path.realpath("streamlord.html"), new=1)

