;; Scheme ;;


; Q1 WWSD: List

; scm> (equal? '(1 . (2 . 3)) (list 1 (cons 2 3)))
; >>> #t
; scm> '(1 . (2 . 3))
; >>> (1 2 . 3)
; scm> (list 1 (cons 2 3))
; >>> (1 (2 . 3)) ; list will create a perfect list, by adding a nil at the end

; scm> (cons 1 '(list 2 3))
; >>> (1 list 2 3)

; scm> (cons (list 2 (cons 3 4)) nil)
; >>> ((2 (3 . 4)))

; scm> '(cons 4 (cons (cons 6 8) ()))
; >>> (cons 4 (cons (cons 6 8) ()))


; Q2 Over or Under

(define (over-or-under x y)
  (cond
    ((< x y)-1)
    ((> x y)1)
    ((= x y)0)
    )
)


; Q3 Filter

(define (filter f lst)
  (cond
    ((null? lst) nil)
    ((f (car lst))(cons (car lst) (filter f (cdr lst))))
    ((not (f (car lst)))(filter f (cdr lst)))
    )
)

; alternative
(define (filter f lst)
    (if (null? lst)       ; don't use if in cond!!!
      nil
      (if (f (car lst) )
        (cons (car lst) (filter f (cdr lst)))
          (filter f (cdr lst))
      )
    )
)


; Q4
(define (make-adder num)
  (lambda (x) (+ x num))
)
