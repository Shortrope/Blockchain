(ns blockchain.core)

(def blockchain (atom []))

(defn get-last-transaction []
  (if (< (count @blockchain) 1)
    [0]
    (last @blockchain)))

(defn add-transaction [transaction-amount]
  (let [last-transaction (get-last-transaction)]
    (swap! blockchain #(conj % [last-transaction transaction-amount]))))