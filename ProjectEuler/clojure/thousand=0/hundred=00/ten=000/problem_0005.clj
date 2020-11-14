(ns project-euler.p.0005)

(defn evenly-divisible
  ([lower upper] (evenly-divisible lower upper upper))
  ([lower upper value]
   (if (every?
         #(= 0 (rem value %)) 
         (range lower (inc upper)))
     value
     (recur lower upper (+ value upper)))))
  
(evenly-divisible 1 20)
