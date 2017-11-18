#!/usr/bin/python3
import os
import lybe
import sys
import signal
import time

def exo(signal,frame):
	print("\nGame is closing")
	time.sleep(1)
	print("Good bye!")
	sys.exit(0)

def Main():
	os.system("clear")
	print("\n\n")
	print("\t\t{}|||||||||||||||||||||||||||||||||||||||||||{}".format("\033[1;34m","\033[1;m"))
	print("\t\t{}|||||||||||||||||||||||||||||||||||||||||||{}".format("\033[1;34m","\033[1;m"))
	print("\t\t{0}|||||||{1}       Game             {0}||||||||||||".format("\033[1;34m","\033[1;33m"))
	print("\t\t{0}|||||||{1}          By            {0}||||||||||||".format("\033[1;34m","\033[1;33m"))
	print("\t\t{0}|||||||{1}           D1FF         {0}||||||||||||".format("\033[1;34m","\033[1;33m"))
	print("\t\t{}|||||||||||||||||||||||||||||||||||||||||||{}".format("\033[1;34m","\033[1;m"))
	print("\t\t{}|||||||||||||||||||||||||||||||||||||||||||{}".format("\033[1;34m","\033[1;m"))
	time.sleep(5)
	mq = input("Start/Restart/Stop : ")
	if mq == "Restart":
		with open("map_or.txt","r") as ff:
			with open("map.txt","w") as dada:
				for ffa	in ff.readlines():
					dada.write(ffa)			
	elif mq == "Stop":
		print("Good Bye")
		time.sleep(3)				
		exit(0)
	while True:
		signal.signal(signal.SIGINT,exo)
		os.system("clear")
		hu = open("map.txt","r")
		xoxo = []
		print("\n\n")
		for huhu in hu:
			print("\t\t\t",end="")
			xoxo.append(huhu)
			print("\033[1;38m",end="")
			for hi in huhu:
				print(hi,end=' ')	
		print("\n\n")		
		backup = sys.stdout
		wn = input("\033[1;38mEnter [N(up)/S(down)/W[left]/E[right] : ")
		if wn == "N":
		    lybe.Some("X","O").up()
		elif wn == "S":
			lybe.Some("X","O").down()		
		elif wn == "W":
			lybe.Some("X","O").left()	
		elif wn == "E":
			lybe.Some("X","O").right()	
		else:
			print("Please put correct letter")	
		sys.stdout = backup
		
		

		
Main()			
