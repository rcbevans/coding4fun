(ns projecteuler.p19
  (:gen-class)
  (require [clj-time.core :as time]
		   [clj-time.periodic :as time-period]
		   [clj-time.predicates :as pr]))

(defn get-time-range
	[start end step]
	(let [inf-range (time-period/periodic-seq start step)
		below-end? #(time/within? (time/interval start end) %1)]
		(take-while below-end? inf-range)))

(defn number-of-sundays
	[start end]
	(let [dates (get-time-range start end (time/days 1))]
		(->> dates 
			(filter #(and (pr/sunday? %1) (pr/first-day-of-month? %1)))
			(count))))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println 
  	(number-of-sundays 
  		(time/date-time 1901 01 01) 
  		(time/date-time 2000 12 31))))
