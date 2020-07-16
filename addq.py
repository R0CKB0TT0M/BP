#!/usr/bin/env python
# import file for file access 
import file

while True:
    file.writefile(input("input question here:"),input("input answer here:"))
    
    if "n" == input("do you wish to continue?[Y/n]").strip():
        break
