
(ns project-euler.p.0001
  (:require [clojure.set :as set]))

(def m3
  (range 0 1000 3))

(defn multiple-n
  [n max]
  (set (range 0 max n)))

(def multiple-3
  (multiple-n 3 1000))

(def multiple-5
  (multiple-n 5 1000))

(reduce +
 (set/union multiple-3 multiple-5))
