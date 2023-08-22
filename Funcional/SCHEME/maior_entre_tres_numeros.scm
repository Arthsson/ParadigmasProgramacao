(define (max-of-three-numbers a b c) ; deinindo a função
    (if (> a b) ; analisa se a é maior que b
        (if (> a c)a c) ; se a for maior que b, verifica se a é maior que c, se sim retorna a, se não retorna c
        (if (> b c)b c))) ;se a nao for maior que b, verifica se b é maior que c, se sim retorna b, se não retorna c

(display (max-of-three-numbers 7 29 300))