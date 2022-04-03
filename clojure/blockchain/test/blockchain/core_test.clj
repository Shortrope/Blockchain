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


(deftest verify-blockchain-test
  (testing "Happy path:"
    (testing "Empty blockchain "
      (reset! blockchain [])
      (is (verify-blockchain)))
    (testing "Single item blockchain"
      (reset! blockchain [[[0] 1]])
      (is (verify-blockchain)))
    (testing "Multi item blockchain"
      (reset! blockchain [[[0] 1] [[[0] 1] 2] [[[[0] 1] 2] 3] [[[[[0] 1] 2] 3] 4]])
      (is (verify-blockchain))))
  (testing "Sad path:"
    (testing "Altered blockchain should return false"
      (reset! blockchain [[[0] 1] [[[0] 1] 2] [[[[0] 1] 2] 3] [[[[[0] 1] 2] -1111] 4]])
      (is (not (verify-blockchain))))
    (testing "Another Altered blockchain should return false"
      (reset! blockchain [[[-1111] 1] [[[0] 1] 2] [[[[0] 1] 2] 3] [[[[[0] 1] 2] 3] 4]])
      (is (not (verify-blockchain))))))


;(deftest get-user-input-test
  ;(println "Enter 2.0")
  ;(is (= 2.0 (get-user-input))))
