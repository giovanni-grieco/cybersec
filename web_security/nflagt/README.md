# NFlagT

http://nflagt.challs.cyberchallenge.it/


## Spiegazione

Si cambiano le cose nell'HTML.

Si mette prima la flag nel carrello mettendo il suo valore pari a 0.

E poi si fa il checkout con un valore superiore a 0 ma in modo tale che se il costo viene calcolato come total=qty*costo
allora con qty = 0.5, il prezzo è a metà e comunque qty >=0 quindi tutto ok

Ha dei check sul massimo e minimo del saldo disponibile.

Quindi non puoi darti troppi solid

Puoi usare i float, e l'acquisto va a buon fine senza decrementare il saldo dato che probabilmente prende parte intera.
CCIT{1nt_V41_1S_N0T_3NOUGH}
