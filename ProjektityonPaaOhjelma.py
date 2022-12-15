#tämä on projektityön pääohjelma
from ProjektityonLuokka import SOTEpalkka

MunPalkka = SOTEpalkka()

#Kysellään tässä erillisessä funktiossa olion kaikille ominaisuuksille arvot käyttäjältä
# Arvot tallentuu listaan, tämä on määritelty jo SOTEpalkka.py metodeissa
def arvojenKysely():
    MunPalkka.tuntipalkka(float(input("Anna tuntipalkkasi: ")))
    MunPalkka.tyotunnit(float(input("Anna tehtyjen työtuntien määrä yhteensä: ")))
    MunPalkka.iltalisat(float(input("Anna iltatuntien määrä: ")))
    MunPalkka.yolisat(float(input("Anna yötuntien määrä: ")))
    MunPalkka.lauantailisat(float(input("Anna lauantaituntien määrä: ")))
    MunPalkka.sunnuntailisat(float(input("Anna sunnuntaituntien määrä: ")))

print("Tämä ohjelma laskee palkkasi perustuen yksityiseen sosiaali- ja terveysalan työehtosopimukseen!")

#Tässä varsinainen ohjelma, joka ensin käynnistää arvojenkyselyfunktion
#Seuraavaksi pyydetään käyttäjää tarkistamaan antamansa arvot, tehdään se tulostamalla listasta arvot nähtäväksi.
#Jos arvot ovat oikein, ohjelma jatkaa varsinaiseen palkan laskemiseen ja tulostamiseen. Käyttäjä valitsee haluaako lomakorvauksen näkyviin vai ei.
#Jos käyttäjä huomaa virheen syöttämissään tiedoissa, ohjelma palaa alkuun ja käyttäjä pääsee syöttämään arvot uudestaan.

while True:
    arvojenKysely()
    print("Tarkista vielä antamasi arvot")
    for i in range(len(MunPalkka.lista)):
        print(MunPalkka.lista[i])
    vastaus = input("Tuliko tunnit oikein [kyllä/ei]: ")
    if vastaus.upper() == "KYLLÄ":
        lomakorvaus = input("Lasketaanko lomakorvaus mukaan palkkaan? [kyllä/ei]: ")
        if lomakorvaus.upper()  == "KYLLÄ":
            MunPalkka.lomakorvaus()
        elif lomakorvaus.upper() == "EI":
            MunPalkka.palkkalaskelma()
    elif vastaus.upper() == "EI":
        print("Anna arvot uudestaan.")
        continue
    break

