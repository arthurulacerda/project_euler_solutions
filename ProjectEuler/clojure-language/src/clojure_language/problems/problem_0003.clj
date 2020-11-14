(ns project-euler.p.0003)

(defn inc2 [x] (+ 2 x))

(defn rem0 [x y] (= 0 (rem x y)))

(defn largest-prime-factor
  ([value] (largest-prime-factor value [2] 3))
  ([value prime-numbers possible-prime]
   (if (some 
         #((partial rem0 possible-prime) %)
         prime-numbers)
     (recur value 
            prime-numbers 
            (inc2 possible-prime))
     (if (rem0 value possible-prime)
       (let [factored-value (/ value possible-prime)]
         (if (= 1 factored-value)
           possible-prime
           (recur factored-value
                  (conj prime-numbers possible-prime)
                  (inc2 possible-prime))))
       (recur value 
              (conj prime-numbers possible-prime) 
              (inc2 possible-prime))))))

(largest-prime-factor 600851475143)
