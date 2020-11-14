(ns clojure-language.core)

(defn fib
  ([]  (fib 1))
  ([x]  (lazy-seq (cons x (fib x 2))))
  ([x y] (lazy-seq (cons y (fib y (+ x y))))))

(defn rem-zero? [x y] (= 0 (rem x y)))

(defn next-prime
  ([known-primes] (next-prime 
                    known-primes 
                    (+ 2 (last known-primes))))
  ([known-primes possible-prime]
   (if (some
         #((partial rem-zero? possible-prime) %)
         known-primes)
     (next-prime known-primes
                 (+ 2 possible-prime))
     possible-prime)))

(defn prime-seq
  ([]
   (prime-seq 2))
  ([x]
   (lazy-seq (cons x (prime-seq 3 [x]))))
  ([x pseq]
   (lazy-seq (cons x (prime-seq
                       (next-prime pseq (+ 2 x))
                       (conj pseq x))))))
