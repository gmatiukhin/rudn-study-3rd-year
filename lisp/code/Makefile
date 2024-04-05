all: task2 task3

task2: task2.lisp
	@sbcl --non-interactive --load task2.lisp

task3: task3.lisp
	@sbcl --non-interactive --load task3.lisp 

sdraw:
	@sbcl --load sdraw.generic

clean:
	@rm task2 task3
