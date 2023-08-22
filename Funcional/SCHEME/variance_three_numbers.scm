; reto sigma ao quadrado: variância, xi: valor analisado, reto X em moldura superior: média aritmética do conjunto ,n: número de dados do conjunto
; verificar formula_vaiancia.png

(define (variance x y)
   (/ (+ (* (- x (/ (+ x y) 2.0)) (- x(/ (+ x y) 2.0))); Calcula o quadrado da diferença entre 'x' e a média de 'x' e 'y'
         (* (- y (/ (+ x y) 2.0)) (- y(/ (+ x y) 2.0)))) ; Calcula o quadrado da diferença entre 'y' e a média de 'x' e 'y'
        2.0)); Divide a soma dos quadrados pelo valor 2.0

(define (variance_three_numbers a b c); Calcula a variância entre 'a' e a variância de 'b' e 'c'
    (variance a (variance b c)))

(display (variance_three_numbers 2 4 6))