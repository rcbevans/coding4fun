;; (= (__ '(1 2 3 3 1)) 5)
;; (= (__ "Hello World") 11)
;; (= (__ [[1 2] [3 4] [5 6]]) 3)
;; (= (__ '(13)) 1)
;; (= (__ '(:a :b :c)) 3)

(fn [coll]
  (loop [cnt 0
         coll (apply list coll)]
    (if-not (= '() coll)
      (recur (inc cnt) (rest coll))
      cnt)))