all: directories bin/task2 bin/task3 transfer

directories:
	@mkdir -p bin

bin/task2: task2.lisp
	@sbcl --non-interactive --load task2.lisp

bin/task3: task3.lisp
	@sbcl --non-interactive --load task3.lisp 

transfer:
	@mv task2 bin/task2
	@mv task3 bin/task3

clean:
	rm -r bin
