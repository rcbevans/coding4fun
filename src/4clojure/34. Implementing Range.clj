; (= (__ 1 4) '(1 2 3))
; (= (__ -2 2) '(-2 -1 0 1))
; (= (__ 5 8) '(5 6 7))

(fn [start end]
  (loop [current (dec end)
        list-so-far '()]
    (if (< current start)
      list-so-far
      (recur (dec current) (conj list-so-far current)))))

 ; ALSO

 (fn [start end]
  (loop [current (dec end)
        list-so-far '()]
    (if (< current start)
      list-so-far
      (recur (dec current) (into list-so-far (list current))))))