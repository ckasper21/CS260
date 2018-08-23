##### Makefile for hw2 #####
##### Author: Chris Kasper

run: problem1 problem2 problem3 view
.PHONY : run

problem1 :
	chmod u+x problem1.py
	python problem1.py $(arg)

problem2 :
	chmod u+x problem2.py
	python problem2.py $(arg)

problem3 :
	chmod u+x problem3.py
	python problem3.py
	gnuplot < plot-instructions
view :
	@\less problem1.py problem2.py problem3.py

clean :
	@\rm *.pyc
	@\rm data.out
	@\rm plot.png
