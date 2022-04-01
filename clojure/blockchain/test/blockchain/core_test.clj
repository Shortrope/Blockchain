(ns blockchain.core-test
  (:require [blockchain.core :refer :all]
            [clojure.test :refer :all]))

(deftest initial-blockchain-test
  (testing "Blockchain exists"
    (reset! blockchain [])
    (is (vector? @blockchain))
    (is (= [] @blockchain))))

(deftest get-last-transaction-of-empty-blockchain-test
  (reset! blockchain [])
  (is (= [0] (get-last-transaction))))

(deftest get-last-transaction-with-one-entry-test
  (reset! blockchain [[1]])
  (is (= [1] (get-last-transaction))))

(deftest get-last-transaction-with-two-entries-in-blockchain-test
  (reset! blockchain [[[0] 1.0]
                      [[[0] 1.0] 2.0]])
  (is (= [[[0] 1.0] 2.0] (get-last-transaction))))

(deftest add-item-to-empty-blockchain-test
  (reset! blockchain [])
  (add-transaction 1.0)
  (is (= [[[0] 1.0]] @blockchain)))

(deftest add-item-to-non-empty-blockchain-test
  (reset! blockchain [[[0] 1.0]])
  (add-transaction 2.0)
  (is (= [[[0] 1.0]
          [[[0] 1.0] 2.0]] @blockchain)))


(deftest get-user-input-test
  (println "Enter 2.0")
  (is (= 2.0 (get-user-input))))