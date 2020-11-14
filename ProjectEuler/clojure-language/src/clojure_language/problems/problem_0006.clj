(ns project-euler.p.0006
  (:require [clojure.math.numeric-tower :as math]))

(defn sum-of-squares
  [lower upper]
  (reduce + (map
             #(math/expt % 2)
             (range lower (inc upper)))))

(defn square-of-sums
  [lower upper]
  (math/expt (reduce 
              + 
              (range lower (inc upper)))
             2))

(- (square-of-sums 1 100) (sum-of-squares 1 100))
