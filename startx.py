#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 01:02:31 2020

@author: davidm
"""

import tkinter as tk
from tkinter import StringVar
import file

# init values
score = 0
r = -1
n = 10
initq = "Wie viele Fragen willst du beantworten?"
a = "" 

# called whenever an answer is submited
def submitfun():
	global r
	global questionStr
	global score
	r = r + 1
	print(answerBox.get())
	if questionStr.get() == initq:
		initn()
	else:
		if answerBox.get().strip() == a:
			score = score + 1
			statusStr.set("Richtig, Score ist: " + str(score) )
			nextq()
		else:
			statusStr.set("Falsch, Score ist: "+ str(score))

#loads next question
def nextq():
	if r == n:
		tk.messagebox.showinfo("Game Over", "Your final score is: " + str(score))
		root.destroy()
	global a
	f = file.readrandomfile()
	questionStr.set(f.readline())
	a = f.readline().strip()

#sets amount of questions
def initn():
	global n
	try:
		n = int(answerBox.get())
		nextq()
	except ValueError:
		print("Error: naN in Entry")
		
#shows answer to question in messagebox
def showfun():
	tk.messagebox.showinfo("Antwort", a)
	
#passes return key-event to submitfun()
def func(event):
	print("You hit return.")
	submitfun()
	
#main	
if __name__ == "__main__":   
	root = tk.Tk()
	root.geometry("300x200")
	root.title("Burschenpruefungs SIM")
	questionStr = StringVar()
	question = tk.Label(root, textvariable = questionStr, wraplength=280)
	question.pack()
	questionStr.set(initq)
	answerBox = tk.Entry(root, width=40)
	answerBox.pack()
	statusStr = StringVar()
	status = tk.Label(root, textvariable=statusStr)
	status.pack()
	statusStr.set("Correct")
	root.bind('<Return>', func)
	Submit = tk.Button(root, text="Submit", command=submitfun )
	Submit.pack()
	showAns = tk.Button(root, text="Antwort anzeigen", command=showfun)
	showAns.pack()
#keep this at the bottom
	root.mainloop()				   