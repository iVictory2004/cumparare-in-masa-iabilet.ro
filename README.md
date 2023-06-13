# Japca la bilete în masă pe iabilet.ro
 Program de cumparat bilete automat cu cod de voucher gratis pe iabilet.ro

Dupa ce downlodati codul, adaugati un fisier pe nume .env in care se scrieti variabile in formatul:

```bash
URL = Linku_de_la_ce_venue_vrei  #exemplu e https://www.iabilet.ro/bilete-concert-guns-n-roses-pe-arena-nationala-din-bucuresti-81171/?utm_source=HpTopWeb
CODE = CODUL_DE_FORMULAR
EMAIL = DUH
PASSWORD = EVIDENT
```
Daca e mai greu cu kktu asta puteti sa va uitati in cod sa scrieti direct 
Dupa care copiati aceste 4 linii impreuna si paste-utile in terminalul deschis pe folderul cu fisierele:

Pe windows:
```bash
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt 
python webscraper.py
```
Pe MacOS/Linux
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
python webscraper.py
```

Si de acum daca vreti sa rulati programu nu aveti nevoie decat de ultima comanda, anume:

```bash
python webscraper.py
```

Asigurati-va ca aveti google chrome inchis inainte sa rulați 🥦🌿! 