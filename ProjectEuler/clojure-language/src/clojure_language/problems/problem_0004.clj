
(ns project-euler.p.0004
  (:require [clojure.string :as s]))

(defn is-palindrom?
  [number]
  (let [number-string  (str number)
        reverse-number (s/reverse number-string)]
    (= number-string reverse-number)))

(defn find-palindroms
  [x y palindroms]
  (let [mult        (* x y)
        palindroms* (if (is-palindrom? mult) (cons mult palindroms) palindroms)]
    (if (> y 1)
      (recur x (dec y) palindroms*)
      (if (> x 1)
        (recur (dec x) (dec x) palindroms*)
        palindroms*))))

(apply max (find-palindroms 999 999 []))
