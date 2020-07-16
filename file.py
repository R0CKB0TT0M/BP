import os
import random

#returns the specified file from the questions folder
def readfile(n="q0"):
	f=open("questions/" + n, 'r')
	return f

#returns a random file from the questions folder
def readrandomfile():
	return readfile(random.choice(os.listdir('questions')))

#write question and answer to seperate lines in file q{0-200} 
def writefile(q,a):
    for n in range(0,200):
        b = True
        for i in os.listdir('questions'):
            if "q" + str(n) == i:
                b = False
                break
        if b:
            f = open("questions/q" + str(n), "w")
            f.write(q + "\n" + a)
            f.close()
            break
            

#tests to test if works
if __name__ == "__main__":
    for i in readrandomfile():
        print(i)

