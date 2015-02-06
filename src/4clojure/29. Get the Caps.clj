; (= (__ "HeLlO, WoRlD!") "HLOWRD")
; (empty? (__ "nothing"))
; (= (__ "$#A(*&987Zf") "AZ")

(fn [string]
  (->> (seq string)
   (filter #(Character/isUpperCase %))
   (apply str)))