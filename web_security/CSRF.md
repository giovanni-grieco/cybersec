Il csrf token è una stringa randomica e assegnarla alla sessione di un'utenza
L'utente fa una prima GET, e riceve nell'header il csrf

L'utente successivamente re-invia il CSRF Token tramita una post magari
L'utente deve rimandare il CSRF token esattamente lo stesso token, così dimostra al server di essere sempre lo stesso.

La banca potrebbe rimandare una seconda pagina, e vi da un altro CSRF Token, che è diverso dal primo.
Quindi quando l'utente fa un'altra interazione, manda l'ultimo CSRF.

Se l'utente non fa esattamente quegli step in quell'ordine, non si fa niente.
Quindi volendo rompere il sistema, non posso fare lo step finale, se non ho fatto quelli prima.

Il sito è in grado di tracciare il flusso di operazioni. E' una difesa contro l'esecuzione diretta.


SOP Same Origin Policy Io mando i cookie solo al sito che me li ha chiesti.

Il cookie può essere impostato nel "Same party"