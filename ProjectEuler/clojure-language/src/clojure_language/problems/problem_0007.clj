(ns project-euler.p.0007
  (:require [clojure-language.core :refer [prime-seq]]))

(last (take 10001 (prime-seq)))
