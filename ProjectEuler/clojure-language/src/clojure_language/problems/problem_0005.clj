(ns project-euler.p.0005
  (:require [clojure-language.core :refer [rem-zero?]]))

(defn evenly-divisible
  ([lower upper] (evenly-divisible lower upper upper))
  ([lower upper value]
   (if (every?
         #((partial rem-zero? value) %)
         (range lower (inc upper)))
     value
     (recur lower upper (+ value upper)))))
  
(evenly-divisible 1 20)
