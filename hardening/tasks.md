# Esercizi

1. Configura sudo affinchè un utente possa eseguire solo un comando specifico (e.s: nmap) [FATTO]
    
1. Configura sudo affinchè un utente possa eseguire solo un comando specifico ma senza un parametro (e.s: si puo eseguire nmap ma non nmap -p)
Nota: si possono mettere espressioni regolari nel file sudoers [DA FARE]

1. Cercare tutti gli eseguibili con SUID [FATTO]

1. Cercare tutti gli eseguibili con SGID [FATTO]

1. Creare uno unit file di Systemd per permettere una shell aperta a tutti sulla rete (netcat in modalità listen con il processo /bin/bash) e provare a connettersi dalla propria macchina usando netcat [FATTO]

1. Installare e configurare un modulo PAM per richiedere caratteristiche minime alla password (min 8 caratteri, maiuscole, minuscole e simboli) [FATTO, cambiata solo il requisito della password, non installato altri moduli]

1. Imposta una password a GRUB così da non permettere l'avvio del sistema operativo con parametri del kernel non standard [WIP]

1. Rendi la cartella /var/log leggibile solo da root [FATTO]

1. Configura un utente per poter fare cat dei logs ma non essere amministratore (va configurato sudoers in modo opportuno) [FATTO]

1. Trova tutti i processi che hanno un file descriptor aperto dentro la cartella /var/log (il comando lsof tornerà comodo) [FATTO]

1. Usa docker per effettuare un privilege escalation [WIP]

1. Cercare se esiste un qualche file all'interno della home di un utente che sia scrivibile da tutti gli utenti [FATTO]

1. Cercare se esiste una cartella all'interno della home di un utente che sia scrivibile da tutti gli utenti [FATTO]

1. Creare un utente con la password che scade ogni giorno [FATTO]

1. Imposta Iptables affinchè sia permesso l'accesso alla macchina solo via SSH (TCP port 22) [FATTO]

1. Imposta Iptables affinchè sia permesso l'accesso alla macchina solo via SSH (TCP port 22) dall'IP 1.2.3.4 e ad un webserver da qualunque IP (TCP port 80 e 443) [FATTO]

1. Imposta Iptables affinchè sia bloccato tutto il traffico Internet sulla macchina (gli utenti non possono navigare) ma sia funzionante il webserver (TCP port 80 e 443) [FATTO]

1. Imposta Iptables affinchè sia permesso l'accesso alla macchina solo via SSH (TCP port 22) e ad un webserver (TCP port 80 e 443) [FATTO]

# Risorse
1. Restrict sudo to only certain commands, dobbiamo specificare il percorso di nmap però dobbiamo prima capire dove si trova nmap. Lo capiamo con ``` which nmap ``` e ci da ```/usr/bin/nmap``` che applichiamo al file sudoer con ```giovanni ALL=(ALL) /usr/bin/nmap``` possiamo fare una black list volendo con il ```!```

1. Cerchiamo di impedire nmap -p ma nmap normale si. TODO

1. Cerchiamo tutti gli eseguibili che hanno il set user id a 1. ```find / -perm -u=s -type f 2>/dev/null```    
[SORGENTE](https://unix.stackexchange.com/questions/180867/how-to-search-for-all-suid-sgid-files)

1. Cerchiamo tutti gli eseguibili che hanno il set group id a 1. ```find / -perm -g=s -type f 2>/dev/null```

1. Creaiamo uno unit file di systemd. Payload: ```netcat -p 8023 -l | /bin/bash```. Server lo unit file

1. basta andare in /etc/pam.d e li dentro ci sono i file come common-password che gestiscono le cose relative alla password

1. [RH](https://www.gnu.org/software/grub/manual/grub/grub.html#Security) e [StackExchange](https://askubuntu.com/questions/656206/how-to-password-protect-grub-menu) Non ho capito bene come fare ma più o meno ci sto

1. Basta fare chmod 700 /var/log come sudo. Però diciamo che questo ci rende impossibile lanciare un comando come sudo per leggere i log in quanto non possiamo manco vedere che file ci sono dentro la cartella. Quindi /var/log se impostata a 744 ci permette almeno di vedere cosa c'è dentro (anche per sfruttare l'auto suggestion).

1. Basta mettere una riga addizionale nel file sudoers che rende possibile leggere all'internod i var/log. ad esempio:
```henderson ALL=(ALL) /usr/bin/cat /var/log/*```. NOOO E' sbagliato. E' exploitable in quanto adesso dopo 7var/log possiamo mettere una qualsiasi cosa e anche "/etc/shadow". Bisogna restringere con ``` ^/var/log/[a-zA-Z0-9]+$``` dove ^ e ```$``` segnano rispettivamente inizio e fine della regex. Si aggiunge anche il punto così da consentira le specifica di stampe di file che hanno estensione ```^/var/log/[a-zA-Z0-9.]+$```

1. lsof ci riporta quali processi hanno quali file aperti specificando il percorso a lsof dei file che ci interessano. Ad esempio ```lsof /var/log/*``` ci ritornerà una lista di processi e file aperti! se non ritorna nulla, nessun processo sta usando quei file.

1. Usare docker per effettuare privilege escalation... ok ma che cazzo?

1. Sempre con find ```find /home/ -perm /002``` che sono scrivibili sia dal gruppo che dagli altri.

1. Sempre con find ma aggiungendo la flag di tipo ```find /home/ -perm /002 -type d``` si usa invece ```-type f``` per i file

1. Teoricamente basta fare ```passwd --maxdays 1 nome_utente``` [SORGENTE](https://askubuntu.com/questions/105040/how-do-i-force-a-user-to-change-the-password-periodically). Si può usare anche per fare l'expire delle password con ```passwd -e nome_utente```

1. [Guida semplice per robe iptables banali](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands) Si fa prima un accept per tutte le connessioni New e Established sulla porta 22 per la chain di input e poi un drop generale. NON FARE IL DROP GENERALE PRIMA DI fare l'accept su 22 altrimenti ci si taglia fuori. ```sudo iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT``` e poi ```sudo iptables -A INPUT -j DROP```

1. in questo caso bisogna specificare l'IP con la flag ```-s 1.2.3.4``` quindi facciamo ACCEPT su ssh con l'aggiunta di -s 1.2.3.4 e poi l'accept su --dport 80 e --dport 443 per tutti e DENY sul resto (ci taglia fuori ovviamente ma dobbiamo cambiare il nat). DATO che questo ci taglierebbe fuori, e che Virtualbox non fa nessuno sourceaddress natting, dobbiamo inserire anche una entry per consentire traffico con indirizzi 10.0.0.0/8 che sono quelli provenienti dall'hypervisor per conto del traffico host-guest e guest-host con ```-s 10.0.0.0/8``` [SORGENTE](https://cysec.pizzonia.it/cysec/study/slide_pratiche/07_Network-Security.pdf)

1. Bisogna aggiungere un elemento all'output di consentre traffico in uscita che sia già considerato "ESTABLISHED" per la --sport 80 e 443 (perchè adesso siamo in uscita) e droppare tutto il resto

1. Simile a quello fatto prima ma adesso dobbiamo consentire traffico in ingresso su dport 22 con ctstate NEW,ESTABLISHED e traffico in uscita con sport 22 con ctstate ESTABLISHED e droppare tutto il resto in Input e Output
