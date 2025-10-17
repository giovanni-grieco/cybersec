# Meme Shop

http://meme_shop.challs.olicyber.it/cart.php

## Spiegazione

Possiamo forse attaccare modificando i cookie.

Nel codice sorgente la componente vulnerarible è la funzione nelle Utils di "get_cart()"

Cambiando il cookie mettendo l'id della flag che ha Id 1, otteniamo la flag a checkout.

Oppure si possono anche aumentare la quantità di soldi.

mettendo il costo negativo

```
{"Videogame":{"price":-10000,"qty":1,"item_id":1}}
```
