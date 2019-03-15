import random
import time
answers=[]
answers.append("Yes")
answers.append("Just do it")
answers.append("No")
answers.append("Maybe")
answers.append("Try again")
answers.append("Never")
answers.append("Another day")
answers.append("Perhaps")
answers.append("42")
answers.append("Of course")
answers.append("Turn left")
answers.append("Go ahead")
answers.append("Nope")

def magic8ball():
	question=raw_input("What is your Question? ")
	print "Thinking...."
	time.sleep(3)
	return answers[random.randint(0,len(answers)-1)]

still_asking = True

while (still_asking):
	print magic8ball()
	a=raw_input("Another question? (Y/N) ")
	if (a.lower()=="n"):
		print "Goodbye!"
		still_asking=False
