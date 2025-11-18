# Esercizi

1. Configura sudo affinchè un utente possa eseguire solo un comando specifico (e.s: nmap) [FATTO]
    
1. Configura sudo affinchè un utente possa eseguire solo un comando specifico ma senza un parametro (e.s: si puo eseguire nmap ma non nmap -p)
Nota: si possono mettere espressioni regolari nel file sudoers [DA FARE]

1. Cercare tutti gli eseguibili con SUID [FATTO]

1. Cercare tutti gli eseguibili con SGID [FATTO]

1. Creare uno unit file di Systemd per permettere una shell aperta a tutti sulla rete (netcat in modalità listen con il processo /bin/bash) e provare a connettersi dalla propria macchina usando netcat [FATTO]

1. Installare e configurare un modulo PAM per richiedere caratteristiche minime alla password (min 8 caratteri, maiuscole, minuscole e simboli)

1. Imposta una password a GRUB così da non permettere l'avvio del sistema operativo con parametri del kernel non standard

1. Rendi la cartella /var/log leggibile solo da root

1. Configura un utente per poter fare cat dei logs ma non essere amministratore (va configurato sudoers in modo opportuno)

1. Trova tutti i processi che hanno un file descriptor aperto dentro la cartella /var/log (il comando lsof tornerà comodo)

1. Usa docker per effettuare un privilege escalation

1. Cercare se esiste un qualche file all'interno della home di un utente che sia scrivibile da tutti gli utenti

1. Cercare se esiste una cartella all'interno della home di un utente che sia scrivibile da tutti gli utenti

1. Creare un utente con la password che scade ogni giorno

1. Imposta Iptables affinchè sia permesso l'accesso alla macchina solo via SSH (TCP port 22)

1. Imposta Iptables affinchè sia permesso l'accesso alla macchina solo via SSH (TCP port 22) dall'IP 1.2.3.4 e ad un webserver da qualunque IP (TCP port 80 e 443)

1. Imposta Iptables affinchè sia bloccato tutto il traffico Internet sulla macchina (gli utenti non possono navigare) ma sia funzionante il webserver (TCP port 80 e 443)

1. Imposta Iptables affinchè sia permesso l'accesso alla macchina solo via SSH (TCP port 22) e ad un webserver (TCP port 80 e 443)

# Risorse
1. Restrict sudo to only certain commands, dobbiamo specificare il percorso di nmap però dobbiamo prima capire dove si trova nmap. Lo capiamo con ``` which nmap ``` e ci da ```/usr/bin/nmap``` che applichiamo al file sudoer con ```giovanni ALL=(ALL) /usr/bin/nmap``` possiamo fare una black list volendo con il ```!```

1. Cerchiamo di impedire nmap -p ma nmap normale si. TODO

1. Cerchiamo tutti gli eseguibili che hanno il set user id a 1. ```find / -perm -u=s -type f 2>/dev/null```    
[SORGENTE](https://unix.stackexchange.com/questions/180867/how-to-search-for-all-suid-sgid-files)

1. Cerchiamo tutti gli eseguibili che hanno il set group id a 1. ```find / -perm -g=s -type f 2>/dev/null```

1. Creaiamo uno unit file di systemd. Payload: ```netcat -p 8023 -l | /bin/bash```. Server lo unit file