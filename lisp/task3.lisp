(declaim #+sbcl(sb-ext:muffle-conditions style-warning))

(defun main ()
  (print "Task 3")
  (let ((exps
          (list 
            '((lambda (x) x) 'atom)
            '((lambda (y) y) '('list))
            '((lambda (j) (car j)) '('three 'elements 'list))
            '((lambda (k) (cdr k)) '('three 'elements 'list))
            '((lambda (u v) (cons u v)) 'very 'good)
            '((lambda (y x) (cons y x)) 'first '(cons 'then 'second))
            '((lambda (a) (caadr a)) (list 'a '(cons 'b '77Q2)))
            '((lambda (var) (cdar var)) (list (list 'a 'b)))
            '((lambda (j) 3.14159) NIL)
            '((lambda (we-break-here) 3.14159) '())
            '((lambda (u v) u) 'alpha 'beta)
            '((lambda (u v) u) 'beta 'alpha)
            '((lambda (u v) v) 'alpha 'beta)
            '((lambda (v u) v) 'alpha 'beta)
            '((lambda (one two) (car one)) '('one) 'two))))
      (mapc (lambda (x) (pprint x) (write '->) (pprint '->) (write (eval x))) exps)))

(sb-ext:save-lisp-and-die "task3"
       :toplevel 'main
       :executable t)
