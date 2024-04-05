(declaim (sb-ext:muffle-conditions cl:style-warning))

(defun main ()
  (print "Task 3")
  (let ((exps
          (list 
            '((lambda (x) x) 'atom)
            '((lambda (y) y) 'list)
            '((lambda (j) (car j)) '(трех элементный лист))
            '((lambda (k) (cdr k)) '(трех элементный лист))
            '((lambda (u v) (cons u v)) 'very 'good)
            '((lambda (y x) (cons y x)) 'один '(потом . другой))
            '((lambda (a) (caadr a)) '(a (b . 77Q2)))
            '((lambda (переменная) (cdar переменная)) '((a b)))
            '((lambda (j) 3.14159) NIL)
            '((lambda (j) 3.14159) ())
            '((lambda (j) 3.14159) 55) 
            '((lambda () 3.14159))
            '((lambda (u v) u) 'alpha 'beta)
            '((lambda (u v) u) 'beta 'alpha)
            '((lambda (u v) v) 'alpha 'beta)
            '((lambda (v u) v) 'alpha 'beta)
            '((lambda (первый второй) (car первый)) '(первый) 'второй))))
      (mapc (lambda (x) (pprint x) (write '->) (write (eval x))) exps)))

(sb-ext:save-lisp-and-die "task3"
       :toplevel 'main
       :executable t)
