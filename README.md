# cumparare-in-masa-iabilet.ro
 Program de cumparat bilete automat cu cod de voucher gratis pe iabilet.ro

Dupa ce downlodati codul, adaugati un fisier pe nume .env in care se scrieti variabile in formatul:
Daca e mai greu cu kktu asta puteti sa va uitati in cod sa scrieti direct 
```bash
URL = EMAILULVOSTRU
CODE = CODUL_DE_FORMULAR
EMAIL = DUH
PASSWORD = EVIDENT
```
dupa care copiati aceste 4 linii impreuna si paste-utile in terminalul deschis pe folderul cu fisierele:
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