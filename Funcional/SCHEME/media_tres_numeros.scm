(define (sum_of_three_numbers a b c)
    (+ a b c))
; soma_tres_numeros.scm

(define (average_numbers a b c)
   (/ (sum_of_three_numbers a b c) 3.0) ;dividir por número decimal? '3.0' ao ínves de 3
)

(display (average_numbers 1 3 7)) 