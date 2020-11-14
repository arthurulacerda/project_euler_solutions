(ns project-euler.p.0002
  (:require [clojure-language.core :refer [fib
                                           rem-zero?]]))

(reduce
  +
  (filter
    #((partial rem-zero? %) 2)
    (take-while #(< % 4000000) (fib))))
