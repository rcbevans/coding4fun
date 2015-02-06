; (= (__ '((1 2) 3 [4 [5 6]])) '(1 2 3 4 5 6))
; (= (__ ["a" ["b"] "c"]) '("a" "b" "c"))
; (= (__ '((((:a))))) '(:a))

(fn myflatten [coll]
  (let [f (first coll)
        n (next coll)]
    (concat 
      (if (sequential? f)
        (myflatten f)
        [f])
      (when (sequential? n)
        (myflatten n)))))