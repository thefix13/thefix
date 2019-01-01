#!/usr/bin/env python3

import os

os.system("clear")
print("")
print("")
print("Use this script to remove the random junk characters that youtube-dl")
print("               adds to the end of mp3 filenames.") 
print("")
print("                      ____________________")
print("                      |                   |")
print("                      |     Drop your     |")
print("                      |     mp3 folder    |")
print("                      |     here and      |")
print("                      |     Press Enter   |")
print("                      |___________________|")

dir = input("")
os.system("clear")

#If the directory name has spaces in it, the drag and drop will put the 
#entire path in single quotes, which need to be removed.
test = "'" in dir

if test == True:
    dir = dir[1:-1]
#The path needs to have forward slash at the end in order for the script
#to be able to properly rename the files.
dir = dir + "/"

count = 0
files = os.listdir(dir)
for entry in files:
    if entry.endswith(".mp3"): 
        os.rename(dir + entry, dir + entry[:-16] + ".mp3")
        print("changing " + entry)
        count += 1
count = str(count)
print("")
print("")
print(count + " file(s) renamed.")
print("")
print("")
