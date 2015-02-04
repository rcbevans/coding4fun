; (= __ (for [x (range 40)
;     :when (= 1 (rem x 4))]
; x))

; (= __ (for [x (iterate #(+ 4 %) 0)
;             :let [z (inc x)]
;             :while (< z 40)]
;         z))

; (= __ (for [[x y] (partition 2 (range 20))]
;         (+ x y)))

(range 1 40 4)