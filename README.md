# Ohjelmistotekniikka, harjoitustyö

<p><b>Harjoitustyöidea:</b> <i>Budjetointisovellus</i></p>  

<p>Budjetointisovelluksessa asetetaan tulot ja kaikki menot lajiteltuna(laskut, harrastukset, yms)</p>  

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/vaatimusmaatittely.md)  

[Työaikakirjanpito](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/arkkitehtuuri.md)

[changelog](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/changelog.md)


## Asennus


1. Asenna riippuvuudet terminaalikomennolla:

    poetry install

2. Suorita alustustoiminpide:

    poetry run invoke build

3.  Käynnistä sovellus:

    poetry run invoke start

## Komentorivi toiminnot

Ohjelman käynnistys:

    poetry run invoke start

Ohjelman testaus:

    poetry run invoke test

Ohjelman testikattavuusraportti:

    poetry run invoke coverage-report