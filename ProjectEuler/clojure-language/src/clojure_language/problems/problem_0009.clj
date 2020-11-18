(ns project-euler.p.0009
  (:require [clojure.math.numeric-tower :as math]))

(defn pythagorean-triplet
  ([solution]
   (pythagorean-triplet solution 1 2 (- solution 1 2)))
  ([solution a b c]
   (if (= (math/expt c 2)
          (+ (math/expt a 2) 
             (math/expt b 2)))
     [a b c]
     (if (>= (+ b 2) c)
       (recur solution (+ a 1) (+ a 2) (- solution a a 3))
       (recur solution a       (+ b 1) (- c 1))))))

(apply * (pythagorean-triplet 1000))
