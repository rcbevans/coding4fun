;; (= (__ (map inc (take 3 (drop 2 [2 5 4 1 3 6]))))
;;   (->> [2 5 4 1 3 6] (drop 2) (take 3) (map inc) (__))
;;   11)

apply +