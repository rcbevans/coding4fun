(ns projecteuler.p4
  (:gen-class))

(defn largest-pallendrome
	[]
	(let [three-digit-nums (range 100 1000)]
		(->> (for [a three-digit-nums
				   b three-digit-nums]
				   (* a b))
			(filter #(= (seq (str %1)) (reverse (str %1))))
			(apply max))))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (largest-pallendrome)))
