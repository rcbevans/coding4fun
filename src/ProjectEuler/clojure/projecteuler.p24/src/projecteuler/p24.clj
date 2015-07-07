(ns projecteuler.p24
  (:gen-class)
  (:require [clojure.math.combinatorics :as combo]))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (apply str (combo/nth-permutation '(0 1 2 3 4 5 6 7 8 9) 999999))))
