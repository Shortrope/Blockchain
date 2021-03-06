(ns blockchain.core)

(def blockchain (atom []))

(defn get-last-transaction []
  (if (< (count @blockchain) 1)
    [0]
    (last @blockchain)))

(defn add-transaction [transaction-amount]
  (let [last-transaction (get-last-transaction)]
    (swap! blockchain #(conj % [last-transaction transaction-amount]))))

(defn get-user-input []
  (print "Enter transaction amount: ")
  (flush)
  (Float/parseFloat (read-line)))

(defn manipulate-blockchain []
  (reset! blockchain (assoc @blockchain 0 [-1])))

(defn verify-blockchain []
  (loop [bc @blockchain]
    (if (< (count bc) 2)
      true
      (let [tx1 (first bc)
            tx2 (second bc)]
        (if (not (= tx1 (first tx2)))
          false
          (recur (rest bc)))))))


(defn display-blockchain []
  ;(let [bc @blockchain]
  (println @blockchain))

(def menu "  a: Add Transaction
  p: Print Blockchain
  m: Manipulate Blockchain
  q: Quit
Your choice: ")

(defn -main [& args]
  (def choice (atom ""))
  (while (not (= @choice "q"))
    (print menu)
    (flush)
    (reset! choice (read-line))
    (cond
      (= @choice "a") (let [new-transaction (get-user-input)]
                        (add-transaction new-transaction))
      (= @choice "p") (display-blockchain)
      (= @choice "m") (manipulate-blockchain)
      (= @choice "q") (println "Quiting..."))
    (when (not (verify-blockchain))
      (reset! choice "q")
      (println "INVALID BLOCKCHAIN!!!")
      (display-blockchain)
      (println "Done..."))))