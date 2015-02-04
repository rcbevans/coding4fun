; (= (__ 0 [:a :b :c]) {:a 0 :b 0 :c 0})
; (= (__ "x" [1 2 3]) {1 "x" 2 "x" 3 "x"})
; (= (__ [:a :b] [:foo :bar]) {:foo [:a :b] :bar [:a :b]})

(fn [val keys] (zipmap keys (repeat (count keys) val)))