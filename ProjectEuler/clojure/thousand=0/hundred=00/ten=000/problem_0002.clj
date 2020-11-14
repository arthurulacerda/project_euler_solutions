
(ns project-euler.p.0002)

(defn fib
  ([]  (fib 1))
  ([x]  (lazy-seq (cons x (fib x 2))))
  ([x y] (lazy-seq (cons y (fib y (+ x y))))))

(reduce
  +
  (filter
    #(= 0 (rem % 2))
    (take-while #(< % 4000000) (fib))))
