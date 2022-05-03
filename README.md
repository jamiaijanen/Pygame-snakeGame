# Matopeli
Mato peli tehty Pythonin Pygame kirjastoa käyttämällä.

## Asennus
Lataa ja asenna Python 3 asennuspaketti, jos sitä ei ole koneellasi entuudestaan.

Allaolevalla komennolla saat tarvittaessa ladattua itsellesi Pygame kirjaston
```
pip3 install pygame
```

## Ohjelman käynnistäminen
Lataa lähdekoodi tietokoneellesi ja aja alla oleva komento terminaalissa ladatun kansion sisällä käynnistääksesi pelin
```
python3 ohjelmistokehitys_lopputyo.py
```
## Pelin pelaaminen
Pelissä pelataan toista pelaajaa vastaan samalla näppäimistöllä. Toinen pelaa nuolinäppäimillä (punainen) ja toinen käyttää nappuloita w,a,s,d (keltainen).
Pelissä kerätään pelinäytölle satunnaisesti ilmestyviä sinisiä "karkkeja", joilla oma mato pitenee.
Pelin voittaa se kumpi pysyy hengissä pidempään. Peli loppuu joko toisen törmätessä laitaan tai törmätessä toisen matoon.
Uuden pelin saa käynnistettyä space-nappulaa painamalla ja pelin loputtua peli sammuu backspace-nappulaa painamalla.