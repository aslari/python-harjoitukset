# sanastoa

- *tulostaminen* = print
- *merkkijono (string)* = lainausmerkeissä tekstiä
- *syöte (input)* = käyttäjän kirjoittama syöte
- *muuttuja (variable)* = inputin arvo
- *muuttujan arvo* = annetaan sijoituslauseessa 
- *concatenate* = yhdistää (virheissä)

## muuttujat (primitiivitietotyypit):
- *merkkijono (string)* = input heittomerkeissä
- *luku (number)* = kokonaisluku (int), liukuluku (float, esim. desimaali) tai kompleksiluku (complex) (vaikeita lukuja ok)
- *totuusarvo (boolean)* = True tai False, esim. onko lamppu päällä

Pythonin muuttujien tietorakenteita: lista (list), monikko (tuple), sanakirja (dictionary)

## laskutoimitukset
- muuttujilla ja vakioilla
- jakojäännösoperaatio eli modulus `(%)`: 
- pelkän kokonaisosan palauttava jakolasku `(//)`: a // b = kuinka monta kertaa b mahtuu a:han
- potenssiin korotus `(**)`

## tyyppimuunnosfunktiot
- merkkijonot (input) eivät voi olla lukuja
- `float()` = muunto liukuluvuksi (desimaali)
- `int()` = muunto kokonaisluvuksi
- `str()` = muunto kokonaisluvusta merkkijonoksi (string)

## muotoilu

- esim. :.5 

### kirjastot
- import esim. math tuo Piin ym.

## valinnat
### valintarakenne (if)
- ehdollinen suoritus suoritetaan, kun ehto on tosi
- sisäinen hierarkia (tab)

### vertailuoperaattorit
> ">" suurempi kuin \
> "<" pienempi kuin \
> ">=" suurempi tai yhtäsuuri kuin \
> "<=" pienempi tai yhtäsuuri kuin \
> "==" yhtä suuri kuin \
> "!=" eri suuri kuin \
-  henkilön pituus on vähintään 170
mutta alle 180 cm: 170 <= pituus < 180
- merkkijonot: m1 < m2 on tosi silloin, jos m1 on aakkosjärjestyksessä ennen m2

### loogiset operaattorit

> "and" ja (“molemmat”) \
> "or" tai (“jompikumpi tai molemmat”) \
> "not" negaatio (“ei”) \
- ```not```-operaattoria sovelletaan ensin, sitten ```and```, sitten ```or```
- ```a and b``` on tosi täsmälleen silloin, kun sekä lauseke ```a``` että lauseke ```b``` ovat tosia.
- ```a or b``` on tosi täsmälleen silloin, kun vähintään jompikumpi lausekkeista ```a``` ja ```b``` on tosi.
- ```not a``` on tosi täsmälleen silloin, kun lauseke ```a``` on epätosi.
- ```a or b and c``` on tosi silloin, kun joko ```a``` on tosi tai sekä ```b``` että ```c``` ovat tosia.
- ```(a or b) and c``` on tosi silloin, kun vähintään jompikumpi lausekkeista ```a``` tai ```b``` on tosi ja sen lisäksi lauseke ```c``` on tosi.
- ```a and not b``` on tosi silloin, kun ```a``` on tosi ja ```b``` on epätosi.

### kaksi toisensa poissulkevaa vaihtoehtoa
- jos alkuperäinen ehto ```if``` on epätosi: ```else```
> if (ehto):\
>   lohko, joka suoritetaan, jos ehto on tosi\
>else:\
>   lohko, joka suoritetaan, jos ehto on epätosi\
- useita vaihtoehtoja, joilla jokaisella oma ehto: ```elif```
- ehdot eivät täyty: ```else```

## toistorakenteet
- ohjelmakoodin sama osa suoritetaan useampaan kertaan
- alkuehdollinen toistorakenne (while)
- iteroiva toistorakenne (for)


### alkuehdollinen toistorakenne (while)

- alkuehto testataan rakenteeseen saavuttaessa
- jos ehto on tosi, suoritetaan sisennetty lohko
- suoritettua testataan, onko alkuehto yhä voimassa
- jos on, suoritetaan sisennetty lohko uudelleen
- toistosta pois, kun alkuehto on epätosi
> while ehto:\
> ___ toistettava lohko\
> ___ while ehto: \
> ________ toistettava lohko
- ```break```-lause poistuu toistorakenteesta välittömästi
- toistoehto kannattaa rakentaa siten, että break-lausetta ei tarvita
- while-rakenteeseen voidaan liittää ```
else```- haara
- suoritus siirtyy, kun toistoehto on epätosi

### listarakenne

- lista: järjestetty joukko alkioita
- rakenteen avulla voi tallentaa useita arvoja yhteen listamuuttujaan
- muuttujan läpikäynti ```for```-toistorakennetta käyttäen
- alkiot ovat määrätyssä järjestyksessä jonossa
- numerointi alkaa nollasta
- listojen alkoihin viittaaminen:
> ```nimet = ["A", "B", "C", "D", "E"]```\
> indeksit: 0, 1, 2, 3, 4 \
> ```print(nimet[3])``` tulostaa D \
> ```print(nimet[1])``` tulostaa B \
> ```print(nimet[-2])``` tulostaa D \
> ```print(nimet[1:3])``` tulostaa B, C \
> ```print(nimet[2:])``` tulostaa C, D, E \
> ```print(nimet)``` tulostaa A, B, C, D, E \
> ```print(len(nimet))``` tulostaa 5
- [numero] = alkio, jonka indeksi on numero. huom! alkaa nollasta
- [-numero] = alkio, laskenta aloitetaan listan lopusta: -1 on viimeinen alkio
- [num1:num2] = indeksiväli, alkiot indeksistä numero 1 alkaen (alkupiste mukaan lukien) ja numeroon 2 päättyen (päätepiste pois lukien)
- [num1:] = indeksiväli alkupisteellä listan loppuun asti
- ```len```-funktio = listan pituus, yhtä suurempi kuin viim. alkion indeksi

#### listaoperaatiot

- listaan usein lisätään ja poistetaan alkioita ohjelman suorituksen aikana

- ```append```: lisää alkion listan loppuun: ``` nimet.append(“Matti”)```
- ```remove```: poistaa alkion ensimmäisen ilmentymän listasta: ```nimet.remove(“Pekka”)```
- ```insert```: lisää alkion haluttuun kohtaan, ennen alkiota, jonka indeksi
vastaa ensimmäistä argumenttia: ```nimet.insert(4, “Teppo”)```
- ```extend```: liittää toisen listan ensimmäiseen listaan: ```toisetNimet = [“Allu”,”Ninni”]```
```nimet.extend(toisetNimet)```
- ```index```: palauttaa alkion ensimmäisen sijainnin indeksin: ```monesko = nimet.index(“Olga”)```
- ```in``` testaa, esiintyykö alkio listassa: ```if “Matti” in nimet:```
```“Matti löytyi”```
- ```sort``` lajittelee listan alkiot aakkos- tai suuruusjärjestykseen: ```luvut.sort()```

#### for-toistorakenne

- lista voidaan läpikäydä ```for```-toistorakenteen avulla:
> ```for``` n ```in``` nimet: \
> ____```print```(f"{n}!")
- kierrosmuuttuja ```n``` saa arvokseen kunkin listan alkion

#### range-funktio

- ```range(1,4)``` nmäärittää arvot 1, 2, 3
- ```range(5,0,-1)``` määrittää arvot 5, 4, 3, 2, 1
- ```range(10,21,2)``` määrittää arvot 10, 12, 14, 16, 18, 20
- ```range```-funktion ensimmäinen argumentti on välin alkupiste
- toinen argumentti on välin loppupiste
- kolmas (valinnainen) argumentti on askeleen suuruus. ilman argumenttia askel = 1
- yksi argumentti tulkitaan loppupisteeksi: alkupiste = 0, askel = 1