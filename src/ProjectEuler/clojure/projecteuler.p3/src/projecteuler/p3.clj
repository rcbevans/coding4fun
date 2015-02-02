(ns projecteuler.p3
  (:gen-class))

(defn get-lcf [candidate currfactor]
  (if (= candidate currfactor)
	candidate
	(if (zero? (mod candidate currfactor))
	  (get-lcf (/ candidate currfactor) currfactor)
	  (get-lcf candidate (inc currfactor)))))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (let [num 600851475143]
  (println 
  	(get-lcf num 2))))
