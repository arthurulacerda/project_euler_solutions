(ns clojure-language.core)

(defn fib
  ([]  (fib 1))
  ([x]  (lazy-seq (cons x (fib x 2))))
  ([x y] (lazy-seq (cons y (fib y (+ x y))))))
