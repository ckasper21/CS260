.PHONY : run

# run will call your test_post target, below
run : prob1

# we need this target to grade.  We will supply our own input.
prob1 : test-set.py
	python test-set.py

view :
	@\less test-set.py
	@\less set.py

clean :
	@\rm *.pyc
