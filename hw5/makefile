# this is a gnu-extension.  Don't worry about it.  Delete it, if you're
# not using gnu-make
.PHONY : run

# run will call your test_post target, below
run : prob1

# we need this target to grade.  We will supply our own input.
prob1 : make_heap.py
	python make_heap.py

view :
	@\less make_heap.py

clean :
	@\rm *.pyc
