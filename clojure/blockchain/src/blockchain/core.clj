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

(defn display-blockchain []
  ;(let [bc @blockchain]
  (println @blockchain))


(defn -main [& args]
  (let [new-transaction (get-user-input)]
    (add-transaction new-transaction))
  (print @blockchain))