;; (= (__ 3) '(1 1 2))
;; (= (__ 6) '(1 1 2 3 5 8))
;; (= (__ 8) '(1 1 2 3 5 8 13 21))

#(loop [result [1 1]
        first 1
        second 1]
   (if (< (count result) %)
     (recur (conj result (+ first second)) second (+ first second))
     (apply list result)))

;; Assuming constraint that number of fib numbers desired >= 2.  Easy fix would be to add case for num == 0 or 1, in which case return '(1)