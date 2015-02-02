(ns projecteuler.p2
  (:gen-class))

(defn even-fib-to
	[max]
	(let [lazy-fib ((fn rfib [a b] 
     					(lazy-seq (cons a (rfib b (+ a b))))) 0 1)
		  fib-to-n (take-while #(< %1 max) lazy-fib)]
		  (->> fib-to-n
		  	(filter #(= 0 (mod %1 2)))
		  	(reduce +))))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println 
  	(even-fib-to 4000000)))