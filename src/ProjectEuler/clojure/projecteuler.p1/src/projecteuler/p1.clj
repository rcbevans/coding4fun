(ns projecteuler.p1
  (:gen-class))

(defn generate-predicate
	""
	[factors]
	(fn [x]
		(some #(= 0 (mod x %1)) factors)))

(defn sum-of-multiples
	""
	[maxValue factors]
	(->> (range 1 maxValue)
		(filter (generate-predicate factors))
		(reduce +)))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (->> (sum-of-multiples 1000 '(3 5))
  	(str "Sum of Multiples: ")
  	(println)))
