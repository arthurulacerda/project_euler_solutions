(ns project-euler.p.0002
  (:require [clojure-language.core :refer [fib]]))

(reduce
  +
  (filter
    #(= 0 (rem % 2))
    (take-while #(< % 4000000) (fib))))
