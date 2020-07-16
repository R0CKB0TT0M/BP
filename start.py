#!/usr/bin/env python
# import file for file access 
import file

# init values
score = 0
n = 10
# get number of questions
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Wie viele Fragen willst du beantworten?"))
            break
        except ValueError:
            print("naN Bitte noch einmal versuchen")
    
    for i in range(0,n):
        f = file.readrandomfile()
        a = input(f.readline())
        if str(a).strip() == str(f.readline()).strip():
            print("richtige Antwort")
            score = score + 1
        else:
            print("Falsche Antwort")
    print("your score is " + str(score))




